from pathlib import Path
import os
def write_file(current_directory, filepath, content):
    dest_path = os.path.join(current_directory, filepath)
    pwd = Path(current_directory).resolve()
    dest = Path(dest_path).resolve()

    if pwd not in dest.parents and pwd != dest:
        return f'Error: Cannot write to "{filepath}" as it is outside the permitted working directory'
    if dest.exists() and not dest.is_file():
        return f'Error: Path already exists as a non-file: "{filepath}"'
    with open(dest, "w") as file:
        file.write(content)
    return f'Successfully wrote to "{filepath}" ({len(content)} characters written)'