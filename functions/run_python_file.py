import os
import subprocess

def run_file(working_directory, file_path, args=[]):
	abs_working = os.path.abspath(working_directory)
	abs_file_path = os.path.join(abs_working, file_path)
	if abs_file_path.startswith(abs_working) == False:
		return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

	if os.path.exists(abs_file_path) == False:
		return f'Error: File "{file_path}" not found.'

	if ".py" != abs_file_path[-3::]:
		return f'Error: "{file_path}" is not a Python file.'

	process = subprocess.run([abs_file_path, args], )
