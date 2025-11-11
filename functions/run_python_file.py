from pathlib import Path
import subprocess
import os
from google.genai import types

schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Runs a python script with a 30s timeout and returns result.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        propterties={
            "filepath": types.Schema(
                type=types.Type.STRING,
                description="The path to python script, relative to pwd."
            ),
        },
    ),
)
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
    try:
        output = subprocess.run(["python", dest, *args], cwd=pwd, timeout=30, capture_output=True)
        returnstring = f"""
            STDOUT: {output.stdout},
            STDERR: {output.stderr},
            Process returned with return code {output.returncode}
    """
        return returnstring
    except Exception as e:
        return f'Error: Error executing {filepath}: {e}'