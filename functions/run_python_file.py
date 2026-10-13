import os
import subprocess

from config import ALLOWED_ACTIONS
from helpers import validate_file_path


schema_run_python_file = {
    "type": "function",
    "function": {
        "name": "run_python_file",
        "description": (
            "Execute a Python file located within the permitted "
            "working directory, optionally passing command-line arguments."
        ),
        "parameters": {
            "type": "object",
            "required": ["file_path"],
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": (
                        "Path to the Python file relative to the working directory."
                    ),
                },
                "args": {
                    "type": "array",
                    "items": {
                        "type": "string",
                    },
                    "description": (
                        "Optional command-line arguments to pass to the Python file."
                    ),
                },
            },
        },
    },
}



def run_python_file(
    working_directory: str, file_path: str, args: list[str] | None = None
) -> str:
    target_dir = validate_file_path(
        working_directory, file_path, action=ALLOWED_ACTIONS[3]
    )
    if "Error:" in target_dir:
        return target_dir
    try:
        is_file = os.path.isfile(target_dir)
        if not is_file:
            return f'Error: "{file_path}" does not exist or is not a regular file'
        elif not target_dir.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file'
        else:
            command = ["python", target_dir]
            if args:
                command.extend(args)

            sub_process_run = subprocess.run(
                args=command,
                capture_output=True,
                text=True,
                timeout=30,
            )
            if sub_process_run.returncode != 0:
                return f"Process exited with code {sub_process_run.returncode}"
            else:
                if not sub_process_run.stdout and not sub_process_run.stderr:
                    return "No output produced"

                return (
                    f"STDOUT: {sub_process_run.stdout}"
                    if sub_process_run.stdout
                    else f"STDERR:{sub_process_run.stderr}"
                )

    except Exception as e:
        return f"Error: executing Python file: {e}"
