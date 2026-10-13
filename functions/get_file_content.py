import os

from config import ALLOWED_ACTIONS, MAX_READ_CHARS
from helpers import validate_file_path

schema_get_file_content = {
    "type": "function",
    "function": {
        "name": "get_file_content",
        "description": "Get content of a file in specified directory relative to the working directory",
        "parameters": {
            "type": "object",
            "required": ["file_path"],
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "Get content of a file in specified directory relative to the working directory",
                },
            },
        },
    },
}

def get_file_content(working_directory: str, file_path: str) -> str:
    target_dir = validate_file_path(
        working_directory, file_path, action=ALLOWED_ACTIONS[0]
    )
    if "Error:" in target_dir:
        return target_dir
    is_directory = os.path.isfile(target_dir)
    if not is_directory:
        return f'Error: File not found or is not a regular file: "{file_path}"'
    else:
        with open(target_dir, "r") as f:
            file_content_str = f.read(MAX_READ_CHARS)
            if f.read(1):
                file_content_str += (
                    f'[...File "{file_path}" truncated at {MAX_READ_CHARS} characters]'
                )
        return file_content_str
