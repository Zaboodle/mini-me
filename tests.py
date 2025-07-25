from functions.run_python_file import run_python_file


def test():
	result = run_python_file("calculator", "main.py")
	print("Result for main.py (no arguments):")
	print(result)

	result = run_python_file("calculator", "main.py", ["3 + 5"])
	print("Result for main.py (3 + 5):")
	print(result)

	result = run_python_file("calculator", "tests.py")
	print("Result for tests.py:")
	print(result)

	result = run_python_file("calculator", "../main.py")
	print("Result for relative path to main.py:")
	print(result)

	result = run_python_file("calculator", "nonexistent.py")
	print("Result for running a nonexistent file:")
	print(result)


if __name__ == "__main__":
	test()
