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
