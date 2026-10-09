import os


def validate_file_path(working_directory: str, file_path: str, action: str) -> str:
    working_directory_absolute_path = os.path.abspath(working_directory)
    target_dir = os.path.normpath(
        os.path.join(working_directory_absolute_path, file_path)
    )
    valid_target_dir = (
        os.path.commonpath([working_directory_absolute_path, target_dir])
        == working_directory_absolute_path
    )
    if not valid_target_dir:
        return f'Error: Cannot {action} "{file_path}" as it is outside the permitted working directory'
    return target_dir
