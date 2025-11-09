import os
from pathlib import Path 
CHAR_LIMIT = 10000

def get_file_content(current_directory, filepath):
    dest_path = os.path.join(current_directory, filepath)
    pwd = Path(current_directory).resolve()
    dest = Path(dest_path).resolve()

    if pwd not in dest.parents and pwd != dest:
        return f'Error: Cannot read "{filepath}" as it is outside the permitted working directory'
    if not dest.is_file():
        return f'Error: File not found or is not a regular file: "{filepath}"'
    with open(dest, "r") as f:
        content = f.read(CHAR_LIMIT)
    return content
    