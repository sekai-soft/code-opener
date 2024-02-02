import unittest
import json
import sqlite3
import uuid
import os
import glob
import shutil
from typing import List
from unittest.mock import patch
from .list_vscode_shortcuts import list_vscode_shortcuts
from .create_vscode_shortcut import create_vscode_shortcut
from .loop import loop

def create_fake_vcsdb(path: str, folder_uris: List[str]):
    conn = sqlite3.connect(path)
    c = conn.cursor()
    c.execute('''CREATE TABLE ItemTable (key TEXT UNIQUE ON CONFLICT REPLACE, value BLOB)''')
    value = {
        "entries": list(map(lambda uri: {"folderUri": uri}, folder_uris))
    }
    c.execute(f"INSERT INTO ItemTable VALUES ('history.recentlyOpenedPathsList','{json.dumps(value, indent=None)}')")
    conn.commit()
    conn.close()


class LoopTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.start_menu_folder = f"test_start_menu_folder_{uuid.uuid4()}"
        os.mkdir(self.start_menu_folder)
        self.vscode_state_path = f"test_vscode_state_{uuid.uuid4()}.vscdb"

    @patch('codeopener.loop.is_vscode_running')
    @patch('codeopener.read_vscode_state.get_vscode_state_path')
    @patch('codeopener.list_vscode_shortcuts.ensure_start_menu_folder')
    @patch('codeopener.create_vscode_shortcut.ensure_start_menu_folder')
    @patch('codeopener.delete_vscode_shortcut.ensure_start_menu_folder')
    # the order of @patch decorators and order of parameters are reversed...
    def test_loop(self,
                  ensure_start_menu_folder_mock_for_delete,
                  ensure_start_menu_folder_mock_for_create,
                  ensure_start_menu_folder_mock_for_list,
                  get_vscode_state_path_mock,
                  is_vscode_running_mock):
        ensure_start_menu_folder_mock_for_delete.return_value = self.start_menu_folder
        ensure_start_menu_folder_mock_for_create.return_value = self.start_menu_folder
        ensure_start_menu_folder_mock_for_list.return_value = self.start_menu_folder
        get_vscode_state_path_mock.return_value = self.vscode_state_path
        is_vscode_running_mock.return_value = False

        desired_folder_uris = ["file:///c%3A/test1", "file:///c%3A/test2"]
        create_fake_vcsdb(self.vscode_state_path, desired_folder_uris)
        create_vscode_shortcut("file:///c%3A/test2", "test2")
        create_vscode_shortcut("file:///c%3A/test3", "test3")

        loop()
        # test1 should be added; test2 should be retained; test3 should be removed
        self.assertEqual(list_vscode_shortcuts(), desired_folder_uris)


    @classmethod
    def tearDownClass(cls) -> None:
        test_start_menu_folders = glob.glob("test_start_menu_folder_*")
        for folder in test_start_menu_folders:
            shutil.rmtree(folder)
        test_vscode_state_files = glob.glob("test_vscode_state_*.vscdb")
        for f in test_vscode_state_files:
            os.remove(f)
