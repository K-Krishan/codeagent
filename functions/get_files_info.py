import os
from pathlib import Path

def get_dir_size(path: str | Path) -> int:
    path = Path(path).resolve(strict=True)
    total = 0
    for p in path.rglob('*'):
        if p.is_file():
            total += p.stat().st_size
    return total

def get_files_info(current_directory, directory="."):
    dest_dir = os.path.join(current_directory, directory)
    pwd = Path(current_directory).resolve()
    dest = Path(dest_dir).resolve()

    if pwd not in dest.parents and pwd != dest:
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    if not dest.exists():
        return f'Error: destination "{directory}" doesn\'t exist'
    if not dest.is_dir():
        return f'Error: destination "{directory}" is not a directory'
    info = [f'Result for {directory} directory:']
    for next in os.listdir(dest): # change code to calc dir size seperately
        filepath = os.path.join(dest, next)
        isdir = os.path.isdir(filepath)
        size = get_dir_size(filepath) if isdir else os.path.getsize(filepath)
        info.append(f"{next}: file_size={size / (1024):.2f} KB, is_dir={isdir}")
    return "\n".join(info)