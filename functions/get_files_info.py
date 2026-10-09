import os

from config import ALLOWED_ACTIONS
from helpers import validate_file_path


def get_files_info(working_directory: str, directory: str = ".") -> str:
    target_dir = validate_file_path(
        working_directory, directory, action=ALLOWED_ACTIONS[-1]
    )
    if "Error:" in target_dir:
        return target_dir

    is_directory = os.path.isdir(target_dir)
    if not is_directory:
        return f'Error: "{directory}" is not a directory'
    else:
        files_list = os.listdir(target_dir)
        files_info = []

        for file in files_list:
            try:
                files_info.extend(
                    [
                        f"- {file}: file_size= {os.path.getsize(os.path.join(target_dir, file))} bytes, is_dir={os.path.isdir(os.path.join(target_dir, file))}"
                    ]
                )
            except Exception as e:
                pass
                files_info.append(f"- Error: {e}")
        return "\n".join(files_info)
