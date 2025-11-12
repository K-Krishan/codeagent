import sys
import os
import argparse

from dotenv import load_dotenv
from google import genai
from google.genai import types
load_dotenv()

from functions.get_files_info import get_files_info, schema_get_files_info
from functions.get_file_content import get_file_content, schema_get_files_content
from functions.write_file import write_file, schema_write_file
from functions.run_python_file import run_python_file, schema_run_python_file

KEY = os.environ.get("GEMINI")
MODEL="gemini-2.0-flash"

def main(prompt, verbose):
    # history = [types.Context(role="user", parts=[types.Part(text=prompt)])]
    history = [{"role": "user", "parts": [{"text": prompt}]}]
    system = """
    You are a helpful AI coding agent.

    When a user asks a question or makes a request, make a function call plan. You can perform the following operations:

    - List files and directories
    - Read file contents
    - Execute Python files with optional arguments
    - Write or overwrite files

    All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
    """
    available_functions = types.Tool(
        function_declarations=[
            schema_get_files_info,
            schema_get_files_content,
            schema_run_python_file,
            schema_write_file,
        ]
    )
    client = genai.Client(api_key=KEY)
    
    response = client.models.generate_content(
        model=MODEL,
        contents=history,
        config=types.GenerateContentConfig(
            system_instruction=system,
            tools=[available_functions],
        )
    )

    if verbose:
        print(f"User: {prompt}")
    print('Inspecting Project:')
    for func in response.function_calls:
        # print(f'Using function: {func.name}({func.args})')
        resp = function_handler(func, verbose)
        try:
            print(f"-> {resp.parts[0].function_response.response}")
        except:
            raise "fatal exception: function returned did not have parts"
    print(f"CodeBuddy: {response.text}")
    if verbose:
        print(f"Prompt Tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response Tokens: {response.usage_metadata.candidates_token_count}")
        # print(response)

    client.close()

def function_handler(func : types.FunctionCall, verbose=False):
    if verbose:
        print(f'Calling function: {func.name}({func.args})')
    else:
        print(f" - Calling function: {func.name}")
    func_list = {
        "get_files_content":get_file_content,
        "get_files_info":get_files_info,
        "run_python_file":run_python_file,
        "write_file":write_file,
    }
    if func not in func_list.keys():
        return types.Content(
            role="tool",
            parts=[
                types.Part.from_function_response(
                    name=func.name,
                    response={"error": f"Unknown function: {func.name}"},
                )
            ],
        )
    resp = func_list[func.name]("calc", **func.args )   # replace calc with working directory (TODO to find a viable solution that doesn't hardcode this and doesnt need passing directory every query)
    return types.Content(
        role="tool",
        parts=types.Part.from_function_response(
            name=func.name,
            response={'result':resp}
        )
    )

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
                    prog='CodingBuddy',
                    description='Your friendly AI that helps you code',
                    epilog='Help-\nhelp description')
    parser.add_argument("prompt")
    parser.add_argument("-v", "--verbose", action="store_true")
    args = parser.parse_args()
    # print(args.prompt, args.verbose)
    # print(args)
    main(args.prompt, args.verbose)