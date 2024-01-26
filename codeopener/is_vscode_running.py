import psutil
from .find_vscode import find_vscode_exe_path


def is_vscode_running() -> bool:
    for proc in psutil.process_iter():
        try:
            exe = proc.exe()
            if exe == find_vscode_exe_path():
                return True
        except psutil.AccessDenied:
            pass
    return False
