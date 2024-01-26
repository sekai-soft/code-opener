import os
from .exception import CodeOpenerException


"""
Finds the default installation path for VSCode (User) on Windows
"""
def find_vscode_installation_path() -> str:
    if "USERPROFILE" not in os.environ:
        raise CodeOpenerException("USERPROFILE is not found in environment variables")
    p = os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "Programs", "Microsoft VS Code")
    if not os.path.exists(p):
        raise CodeOpenerException("VSCode installation path is not found")
    return p

"""
Finds the default bin path for VSCode (User) on Windows
"""
def find_vscode_bin_path() -> str:
    p = os.path.join(find_vscode_installation_path(), "bin")
    if not os.path.exists(p):
        raise CodeOpenerException("VSCode bin path is not found")
    return p


"""
Finds the default executable path for VSCode (User) on Windows
"""
def find_vscode_exe_path() -> str:
    p = os.path.join(find_vscode_installation_path(), "Code.exe")
    if not os.path.exists(p):
        raise CodeOpenerException("VSCode executable path is not found")
    return p


"""
Finds the default cmd path for VSCode (User) on Windows
"""
def find_vscode_cmd_path() -> str:
    p = os.path.join(find_vscode_bin_path(), "code.cmd")
    if not os.path.exists(p):
        raise CodeOpenerException("VSCode cmd path is not found")
    return p
