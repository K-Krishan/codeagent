from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file
from functions.run_python_file import run_python_file

def test_files_info():
    print(get_files_info("calc", "."))
    print()
    print(get_files_info("calc", "pkg"))
    print()
    print(get_files_info("calc", "/bin"))
    print()
    print(get_files_info("calc", "../"))
    print()

def test_file_content():
    print(get_file_content("calc", "main.py"))
    print()
    print(get_file_content("calc", "pkg/calculator.py"))
    print()
    print(get_file_content("calc", "/bin/cat"))
    print()
    print(get_file_content("calc", "pkg/does_not_exist.py"))
    print()
def test_file_write():
    print(write_file("calc", "lorem.txt", "wait, this isn't lorem ipsum"))
    print(write_file("calc", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"))
    print(write_file("calc", "/tmp/temp.txt", "this should not be allowed"))
def test_run_python():
    print(run_python_file("calc", "main.py"))
    print(run_python_file("calc", "main.py", ["3 + 5"]))
    print(run_python_file("calc", "tests.py"))
    print(run_python_file("calc", "../main.py"))
    print(run_python_file("calc", "nonexistent.py"))
    print(run_python_file("calc", "lorem.txt"))
# test_files_info()
# test_file_content()
# test_file_write()
test_run_python()