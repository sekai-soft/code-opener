import time
from codeopener.loop import loop


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
    # TODO: on-device tests and test on Windows 10
    loop(simple_print_callback)


if __name__ == '__main__':
    main()
