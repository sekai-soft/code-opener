from typing import Callable
from dataclasses import dataclass
from .create_vscode_shortcut import create_vscode_shortcut
from .list_vscode_shortcuts import list_vscode_shortcuts
from .delete_vscode_shortcut import delete_vscode_shortcut    
from .is_vscode_running import is_vscode_running
from .read_vscode_state import read_vscode_state
from .parse_workspace_name import parse_workspace_name
from .logger import logger


@dataclass
class LoopResult:
    added_count: int = 0
    removed_count: int = 0

def _loop() -> LoopResult:
    logger.info("Running loop...")

    # make sure VSCode is not running
    if is_vscode_running():
        logger.info("VSCode is running, please close it first")
        return LoopResult()
    logger.info("VSCode is not running, proceeding...")
    
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

    return LoopResult(
        added_count=len(added_folder_uris),
        removed_count=len(deleted_folder_uris),
    )

def loop() -> LoopResult:
    try:
        return _loop()
    except Exception as e:
        logger.exception(e)
        return LoopResult()
