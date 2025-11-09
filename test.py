from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file

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
def test_file_write():
    print(write_file("Calc", "lorem.txt", "wait, this isn't lorem ipsum"))
    print(write_file("Calc", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"))
    print(write_file("Calc", "/tmp/temp.txt", "this should not be allowed"))
# test_files_info()
# test_file_content()
test_file_write()