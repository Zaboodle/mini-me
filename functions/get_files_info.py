import os

def get_files_info(working_directory, directory="."):
	working_path = os.path.abspath(working_directory)
	target_path = os.path.abspath(os.path.join(working_path, directory))

	if os.path.commonpath([working_path, target_path]) != working_path:
		return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

	if os.path.isdir(target_path) == False:
		return f'Error: "{directory}" is not a directory'

	try:
		files_info = []
		for filename in os.listdir(target_path):
			filepath = os.path.join(target_path, filename)
			file_size = 0
			is_dir = os.path.isdir(filepath)
			file_size = os.path.getsize(filepath)
			files_info.append(
				f"- {filename}: file_size={file_size} bytes, is_dir={is_dir}"
			)
		return "\n".join(files_info)
	except Exception as e:
		return f"Error listing files: {e}"
