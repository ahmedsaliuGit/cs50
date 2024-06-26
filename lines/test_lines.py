from lines import validate_input

def main():
    test_argument_is_one()
    test_too_few_arguments()
    test_too_many_arguments()
    test_not_python_file()

def test_argument_is_one():
    assert validate_input("hello.txt") == True

def test_too_few_arguments():
    assert validate_input() == "Too few command-line arguments"

def test_too_many_arguments():
    assert validate_input() == "Too many command-line arguments"

def test_not_python_file():
    assert validate_input() == "Not a Python file"

if __name__ == "__main__":
    main()
