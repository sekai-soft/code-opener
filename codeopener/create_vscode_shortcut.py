import os
import pylnk3
from .find_vscode import find_vscode_cmd_path, find_vscode_bin_path, find_vscode_exe_path
from .ensure_start_menu_folder import ensure_start_menu_folder

def create_vscode_shortcut(folder_uri: str, workspace_name: str):
    pylnk3.for_file(
        rf"{find_vscode_cmd_path()}",
        rf"{os.path.join(ensure_start_menu_folder(), workspace_name + '.lnk')}",
        arguments=rf"--folder-uri {folder_uri}",
        description=rf"Opens {workspace_name} in VSCode",
        icon_file=rf"{find_vscode_exe_path()}",
        work_dir=rf"{find_vscode_bin_path()}",
        window_mode=r"Minimized"
    )
