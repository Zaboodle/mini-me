import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types
from config import MAX_CHARS
from schemas import *

def main():
	load_dotenv()
	args = sys.argv[1:]
	system_prompt = ("""
		You are a helpful AI coding agent.
		When a user asks a question or makes a request, make a function call plan.
		You can perform the following operations:
		- List files and directories
		- Read file contents
		- Execute Python files with optional arguments
		- Write or overwrite files
		All paths you provide should be relative to the working directory.
		You do not need to specify the working directory in your function calls
		as it is automatically injected for security reasons.
		"""
	)
	if not args:
		print("AI Code Assistant")
		print('Usage: python main.py "your prompt here"')
		print('Example: python main.py "How do I build a calculator app?"')
		sys.exit(1)

	available_functions = types.Tool(function_declarations=[schema_get_files_info, schema_get_file_content, schema_run_python_file, schema_write_file])
	user_prompt = " ".join(args)
	messages = [types.Content(role="user", parts=[types.Part(text=user_prompt)]),]
	api_key = os.environ.get("GEMINI_API_KEY")
	client = genai.Client(api_key=api_key)
	response = client.models.generate_content(
		model='gemini-2.0-flash-001',
		contents=messages,
		config=types.GenerateContentConfig(tools=[available_functions],
		system_instruction=system_prompt)
	)
	prompt_tokens = response.usage_metadata.prompt_token_count
	response_tokens = response.usage_metadata.prompt_token_count

	if '--verbose' in args:
		print(f"User prompt: {user_prompt}")
		print(f"Prompt tokens: {prompt_tokens}")
		print(f"Response tokens: {response_tokens}\n")
	if not response.function_calls:
		return response.text
	for function_call_part in response.function_calls:
		print(f'Calling function: {function_call_part.name}({function_call_part.args})')


if __name__ == "__main__":
	main()
