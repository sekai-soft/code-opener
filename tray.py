import time
import multiprocessing
import subprocess
# hack required for infi.systray to work with pyinstaller
# because it imports pkg_resources :(
import pkg_resources
from infi.systray import SysTrayIcon
from codeopener.loop import loop
from codeopener.windows_native_notification import windows_native_notification
from codeopener.logger import log_file

loop_interval = 10

def _loop():
        while True:
            windows_native_notification(loop())
            time.sleep(loop_interval)


def open_logs(_):
    subprocess.run(["PowerShell", "Get-Content", "-Path", log_file, "-Wait"])

menu_options = (("Logs", None, open_logs),)


def main():
    loop_process = multiprocessing.Process(target=_loop)
    loop_process.start()

    def on_quit(_):
        loop_process.terminate()

    systray = SysTrayIcon("icon.ico", "Code Opener", menu_options, on_quit=on_quit)
    systray.start()


if __name__ == '__main__':
    # https://github.com/pyinstaller/pyinstaller/wiki/Recipe-Multiprocessing
    multiprocessing.freeze_support()
    main()
