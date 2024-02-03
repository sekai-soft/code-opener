from codeopener.loop import loop
from codeopener.windows_native_notification import windows_native_notification


def main():
    # TODO: see logs and CodeOpenerException and other exceptions in a log window
    # TODO: on-device tests and test on Windows 10
    windows_native_notification(loop())


if __name__ == '__main__':
    main()
