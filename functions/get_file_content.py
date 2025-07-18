import os
from config import MAX_CHARACTER_LIMIT

def get_file_content(working_directory, file_path):
	abs_directory = os.path.abspath(working_directory)
	abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))

	if abs_file_path.startswith(abs_directory) == False:
		return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

	if os.path.isfile(abs_file_path) == False:
		return f'Error: File not found or is not a regular file: "{file_path}"'

	try:
		with open(abs_file_path, "r") as f:
			content = f.read(MAX_CHARACTER_LIMIT)
			if os.path.getsize(abs_file_path) > MAX_CHARACTER_LIMIT:
				content += f'[...File "{file_path}" truncated at {MAX_CHARACTER_LIMIT} characters]'
		return content
	except Exception as e:
		return f'Error reading file "{file_path}": {e}'
