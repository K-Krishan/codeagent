from pathlib import Path
import os
from google.genai import types

schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="writes onto a python file, given its path and content",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        propterties={
            "filepath": types.Schema(
                type=types.Type.STRING,
                description="The file path to write content onto, relative to pwd."
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="Content to write onto the python file,"
            )
        },
    ),
)
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