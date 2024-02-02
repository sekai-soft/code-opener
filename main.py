from codeopener.loop import loop, LoopResult


def windows_native_notification(res: LoopResult):
    from win11toast import notify

    added_count = res.added_count
    removed_count = res.removed_count

    if added_count > 0 and removed_count > 0:
        msg = f"Added {added_count} shortcuts and deleted {removed_count} shortcuts"
    elif added_count > 0:
        msg = f"Added {added_count} shortcuts"
    elif removed_count > 0:
        msg = f"Deleted {removed_count} shortcuts"
    else:
        msg = None

    if msg is not None:
        notify("Code Opener", msg)


def main():
    # TODO: as a tray app
    # TODO: run once mode & run forever mode (need to allow forever sudo)
    # TODO: see logs and CodeOpenerException and other exceptions in a log window
    # TODO: on-device tests and test on Windows 10
    res = loop()
    windows_native_notification(res)


if __name__ == '__main__':
    main()
