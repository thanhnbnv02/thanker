import os

from config import ALLOWED_ACTIONS
from helpers import validate_file_path


def write_file(working_directory: str, file_path: str, content: str) -> str:
    target_dir = validate_file_path(
        working_directory, file_path, action=ALLOWED_ACTIONS[1]
    )
    if "Error:" in target_dir:
        return target_dir
    is_directory = os.path.isdir(target_dir)
    if is_directory:
        return f'Error: Cannot write to "{file_path}" as it is a directory'
    else:
        os.makedirs(file_path, exist_ok=True)
        with open(target_dir, "w") as f:
            f.write(content)
        return (
            f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
        )
