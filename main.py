import argparse
import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

parser = argparse.ArgumentParser(description="Instruction for thanker")
parser.add_argument("user_prompt", type=str, help="User prompt for the model")
parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
args = parser.parse_args()

api_key = os.getenv("OPENROUTER_API_KEY")
base_url = os.getenv("BASE_URL")

if not all((api_key, base_url)):
    raise RuntimeError(
        "Missing required environment variables: OPENROUTER_API_KEY and BASE_URL"
    )

client = OpenAI(base_url=base_url, api_key=api_key)

messages = [{"role": "user", "content": args.user_prompt}]

response = client.chat.completions.create(model="openrouter/free", messages=messages)


def main() -> None:
    usage_response = response.usage
    if not usage_response:
        raise RuntimeError("Response usage is None. Cannot access token counts.")

    prompt_token = usage_response.prompt_tokens
    completion_token = usage_response.completion_tokens

    if args.verbose:
        print(f"User prompt: {args.user_prompt}")
        print(f"\nPrompt tokens: {prompt_token}")
        print(f"\nResponse tokens: {completion_token}")

    print(response.choices[0].message.content)


if __name__ == "__main__":
    main()
