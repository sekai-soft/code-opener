from .exception import CodeOpenerException


def parse_workspace_name(folder_uri: str) -> str:
    splits = folder_uri.split("/")
    if len(splits) < 2:
        raise CodeOpenerException(f"Encountered an invalid folder_uri: {folder_uri}")
    workspace_name = splits[-1]
    workspace_name = workspace_name.replace("%20", " ")
    return workspace_name
