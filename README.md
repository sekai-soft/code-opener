# Code Opener
Syncs your VSCode workspaces to Start Menu on Windows 10/11

## Development
Developed on Python 3.12.1 on Windows 11

#### Install dependencies
```
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements
```

#### Run unit tests
```
.\venv\Scripts\activate
python -m unittest discover
```

#### Build Windows app
```
.\venv\Scripts\activate
pyinstaller --windowed --uac-admin --clean .\tray.py
```

Then find the built app in `dist` folder
