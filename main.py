from codeopener.loop import loop


def simple_print_callback(added_count: int, deleted_count: int):
    print(f"Added {added_count} shortcuts and deleted {deleted_count} shortcuts")


def windows_native_notification_callback(added_count: int, deleted_count: int):
    from win11toast import notify

    if added_count > 0 and deleted_count > 0:
        msg = f"Added {added_count} shortcuts and deleted {deleted_count} shortcuts"
    elif added_count > 0:
        msg = f"Added {added_count} shortcuts"
    elif deleted_count > 0:
        msg = f"Deleted {deleted_count} shortcuts"
    else:
        msg = None

    if msg is not None:
        notify("Code Opener", msg)


def main():
    # TODO: as a tray app
    # TODO: run once mode & run forever mode (need to allow forever sudo)
    # TODO: see logs and CodeOpenerException and other exceptions in a log window
    # TODO: on-device tests and test on Windows 10
    loop(windows_native_notification_callback)


if __name__ == '__main__':
    main()
