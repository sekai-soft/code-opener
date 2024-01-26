import time
from typing import Callable
from codeopener.create_vscode_shortcut import create_vscode_shortcut
from codeopener.list_vscode_shortcuts import list_vscode_shortcuts
from codeopener.delete_vscode_shortcut import delete_vscode_shortcut    
from codeopener.is_vscode_running import is_vscode_running
from codeopener.read_vscode_state import read_vscode_state
from codeopener.parse_workspace_name import parse_workspace_name

def loop(callback: Callable[[int, int], None] = None):
    print("Running loop...")

    # make sure VSCode is not running
    if is_vscode_running():
        print("VSCode is running, please close it first")
        return
    print("VSCode is not running, proceeding...")
    
    # read from VSCode state
    vscode_folder_uris = read_vscode_state()

    # read list of existing shortcuts
    existing_shortcuts = list_vscode_shortcuts()

    # reconcile: create and delete (needs sudo)
    added_folder_uris = []
    for vscode_folder_uri in vscode_folder_uris:
        if vscode_folder_uri not in existing_shortcuts:
            added_folder_uris.append(vscode_folder_uri)
    deleted_folder_uris = []
    for existing_shortcut in existing_shortcuts:
        if existing_shortcut not in vscode_folder_uris:
            deleted_folder_uris.append(existing_shortcut)
    for added_folder_uri in added_folder_uris:
        # TODO: duplicate workspace names?
        create_vscode_shortcut(
            added_folder_uri,
            parse_workspace_name(added_folder_uri),
        )
    for deleted_folder_uri in deleted_folder_uris:
        delete_vscode_shortcut(deleted_folder_uri)

    # callback
    if callback:
        callback(len(added_folder_uris), len(deleted_folder_uris))


def simple_print_callback(added_count: int, deleted_count: int):
    print(f"Added {added_count} shortcuts and deleted {deleted_count} shortcuts")


def win10_native_notification_callback(added_count: int, deleted_count: int):
    from win10toast import ToastNotifier
    toaster = ToastNotifier()

    if added_count > 0 and deleted_count > 0:
        msg = f"Code Opener added {added_count} shortcuts and deleted {deleted_count} shortcuts"
    elif added_count > 0:
        msg = f"Code Opener added {added_count} shortcuts"
    elif deleted_count > 0:
        msg = f"Code Opener deleted {deleted_count} shortcuts"
    else:
        msg = None

    if msg is not None:
        # TODO: this does not seem to work yet
        # https://stackoverflow.com/questions/76254003/wndproc-return-value-cannot-be-converted-to-lresult-typeerror-wparam-is-simple
        toaster.show_toast("Code Opener", msg, duration=5, threaded=True)
        while toaster.notification_active(): time.sleep(0.1)


def main():
    # TODO: tests
    # TODO: as a tray app
    # TODO: run once mode & run forever mode (need to allow forever sudo)
    # TODO: see logs and CodeOpenerException and other exceptions in a log window
    loop(simple_print_callback)


if __name__ == '__main__':
    main()
