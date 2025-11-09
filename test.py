from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content

def test_files_info():
    print(get_files_info("Calc", "."))
    print()
    print(get_files_info("Calc", "pkg"))
    print()
    print(get_files_info("Calc", "/bin"))
    print()
    print(get_files_info("Calc", "../"))
    print()

def test_file_content():
    print(get_file_content("Calc", "main.py"))
    print()
    print(get_file_content("Calc", "pkg/calculator.py"))
    print()
    print(get_file_content("Calc", "/bin/cat"))
    print()
    print(get_file_content("Calc", "pkg/does_not_exist.py"))
    print()

# test_files_info()
test_file_content()