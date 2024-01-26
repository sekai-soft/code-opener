import os
from .exception import CodeOpenerException

def ensure_start_menu_folder() -> str:
    if 'SYSTEMDRIVE' not in os.environ:
        raise CodeOpenerException('SYSTEMDRIVE environment variable is not found')
    p = os.path.join(
        os.environ['SYSTEMDRIVE']+os.sep,
        'ProgramData', 'Microsoft', 'Windows', 'Start Menu', 'Programs', 'Code Opener Shortcuts'
    )
    if not os.path.exists(p):
        os.makedirs(p)
    return p
