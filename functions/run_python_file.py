import os
import subprocess

def run_python_file(working_directory, file_path, args=[]):
	abs_working = os.path.abspath(working_directory)
	abs_file_path = os.path.abspath(os.path.join(abs_working, file_path))
	if os.path.commonpath([abs_working, abs_file_path]) != abs_working:
		return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

	if os.path.exists(abs_file_path) == False:
		return f'Error: File "{file_path}" not found.'

	if abs_file_path.endswith(".py") == False:
		return f'Error: "{file_path}" is not a Python file.'

	try:
		process = (
			subprocess.run(["python", abs_file_path] + args, cwd=abs_working,
			timeout=30, capture_output=True, text=True)
		)
		stdout = process.stdout.strip()
		stderr = process.stderr.strip()
		exitcode = process.returncode

		if not stdout and not stderr:
			return 'No output produced.'

		result = f'STDOUT:\n{stdout}\nSTDERR:\n{stderr}'

		if exitcode != 0:
			return result + f'\nProcess exited with code {exitcode}'

		return result

	except Exception as e:
		return f'Error: executing Python file: {e}'
