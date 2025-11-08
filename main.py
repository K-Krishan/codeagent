import sys
import os
import argparse

from dotenv import load_dotenv
from google import genai
from google.genai import types
load_dotenv()

KEY = os.environ.get("GEMINI")
MODEL="gemini-2.0-flash"

def main(prompt, verbose):
    history = [types.Context(role="user", parts=[types.Part(text=prompt)])]

    client = genai.Client(api_key=KEY)
    response = client.models.generate_content(
        model=MODEL,
        contents=history,
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