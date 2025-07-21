import os

def write_file(working_directory, file_path, content):
	abs_work_path = os.path.abspath(working_directory)
	abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))

	if abs_file_path.startswith(abs_work_path) == False:
		return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

	if os.path.exists(file_path) == False:
		try:
			os.makedirs(os.path.dirname(abs_file_path), exist_ok=True)
		except Exception as e:
			return f'Error: Directory not found. Creating directory: {e}'

	if os.path.exists(abs_file_path) and os.path.isdir(abs_file_path):
		return f'Error: "{file_path}" is a directory, not a file'
	try:
		with open(abs_file_path, "w") as f:
			f.write(content)
		return f'Successfuly wrote to "{file_path}" ({len(content)} characters written)'
	except Exception as e:
		return f'Error: writing to file: {e}'
