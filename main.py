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
    print(f"CodeBuddy: {response.text}")
    if verbose:
        print(f"Prompt Tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response Tokens: {response.usage_metadata.candidates_token_count}")
        # print(response)

    client.close()

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