import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types
from config import MAX_CHARACTER_LIMIT

def main():
	load_dotenv()
	args = sys.argv[1:]
	if not args:
		print("AI Code Assistant")
		print('Usage: python main.py "your prompt here"')
		print('Example: python main.py "How do I build a calculator app?"')
		sys.exit(1)

	user_prompt = " ".join(args)
	messages = [types.Content(role="user", parts=[types.Part(text=user_prompt)]),]
	api_key = os.environ.get("GEMINI_API_KEY")
	client = genai.Client(api_key=api_key)
	response = client.models.generate_content(
		model='gemini-2.0-flash-001',
		contents=messages,
	)
	prompt_tokens = response.usage_metadata.prompt_token_count
	response_tokens = response.usage_metadata.prompt_token_count

	if '--verbose' in args:
		print(f"User prompt: {user_prompt}")
		print(f"Prompt tokens: {prompt_tokens}")
		print(f"Response tokens: {response_tokens}\n\n")
	print(response.text)


if __name__ == "__main__":
	main()
