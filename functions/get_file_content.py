import os

from config import MAX_READ_CHARS


def get_file_content(working_directory: str, file_path: str) -> str:
    working_directory_absolute_path = os.path.abspath(working_directory)
    target_dir = os.path.normpath(
        os.path.join(working_directory_absolute_path, file_path)
    )
    valid_target_dir = (
        os.path.commonpath([working_directory_absolute_path, target_dir])
        == working_directory_absolute_path
    )
    if not valid_target_dir:
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

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
