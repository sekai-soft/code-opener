from .loop import LoopResult


def windows_native_notification(res: LoopResult):
    from win11toast import notify

    added_count = res.added_count
    removed_count = res.removed_count
    print(f"Added {added_count} shortcuts and deleted {removed_count} shortcuts")

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
