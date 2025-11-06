import os
from dotenv import load_dotenv
from google import genai
load_dotenv()

KEY = os.environ.get("GEMINI")
MODEL="gemini-2.0-flash"

client = genai.Client(api_key=KEY)
response = client.models.generate_content(
    model=MODEL,
    contents='What\'s agentic AI? Answer within 5 sentences.',
)

print(response.text)
print(f"prompt tokens: {response.usage_metadata.prompt_token_count}")
print(f"response tokens: {response.usage_metadata.candidates_token_count}")
# print(response)

client.close()