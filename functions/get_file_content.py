import os
from pathlib import Path 
CHAR_LIMIT = 10000
from google.genai import types

schema_get_files_content = types.FunctionDeclaration(
    name="get_files_content",
    description="returns content in a python file as string, if the file exists.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        propterties={
            "filepath": types.Schema(
                type=types.Type.STRING,
                description="The file path to return content from, relative to pwd."
            ),
        },
    ),
)
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
    