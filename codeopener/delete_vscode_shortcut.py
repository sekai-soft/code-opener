import os
import pylnk3
from .ensure_start_menu_folder import ensure_start_menu_folder


def delete_vscode_shortcut(folder_uri: str):
    for _, _, files in os.walk(ensure_start_menu_folder()):
        for f in files:
            if f.endswith(".lnk"):
                lnk_f = os.path.join(ensure_start_menu_folder(), f)
                lnk = pylnk3.parse(lnk_f)
                # splits out the uri in arguments "--folder-uri <uri>"
                found_folder_uri = lnk.arguments.split(" ")[1]
                if found_folder_uri == folder_uri:
                    os.remove(lnk_f)
