import os


def get_files_info(working_directory: str, directory: str = ".") -> str:
    working_directory_absolute_path = os.path.abspath(working_directory)

    target_dir = os.path.normpath(
        os.path.join(working_directory_absolute_path, directory)
    )
    valid_target_dir = (
        os.path.commonpath([working_directory_absolute_path, target_dir])
        == working_directory_absolute_path
    )
    if not valid_target_dir:
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

    is_directory = os.path.isdir(directory)
    if not is_directory:
        return f'Error: "{directory}" is not a directory'
    else:
        return f'Success: "{directory}" is within the working directory'
