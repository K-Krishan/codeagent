from pathlib import Path
import os

def run_python_file(current_directory, filepath, args=[]):
    dest_path = os.path.join(current_directory, filepath)
    pwd = Path(current_directory).resolve()
    dest = Path(dest_path).resolve()

    if pwd not in dest.parents and pwd != dest:
        return f'Error: Cannot execute "{filepath}" as it is outside the permitted working directory'
    if not dest.exists():
        return f'Error: File doesn\'t exist: "{filepath}"'
    if not dest.is_file() or dest.suffix != '.py':
        return f'Error: "{filepath}" is not a python file'
