# Pastefy CLI

## Installation

### Linux
Installing it via moving file into /usr/bin
`INFO` requests, argparse python-packages are required
```bash
git clone https://github.com/interaapps/pastefy-cli
cd pastefy-cli
sudo cp main.py /usr/local/bin/pastefy
# You may have to set the permission
sudo chmod 777 /usr/local/bin/pastefy
```
or move the linux-build from https://github.com/interaapps/pastefy-cli/releases into the /usr/local/bin folder as pastefy (Filename)

### Windows
Go to https://github.com/interaapps/pastefy-cli/releases and download the windows build. Unzip the folder (Rightclick, extract all), go into it, copy the path and add it into the path variables. (Search in windows-search for environment variables, click on the environment variables button and double-click on Path and add it.)

### Compile it your own
```bash
pip install pyinstaller
pyinstaller --hidden-import requests main.py
```

## Usage
```bash
# Paste a file
pastefy -f README.md

# Set title
pastefy -f README.md -t Test.md

# Paste contents
pastefy -c "Hello world"

# Paste contents with title
pastefy -c "print('Hello')" -t "test.py"
```