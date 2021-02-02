# Pastefy CLI

## Installation

`INFO` The pip modules requests, argparse python-packages are required
```bash
git clone https://github.com/interaapps/pastefy-cli
cd pastefy-cli
sudo cp main.py /usr/local/bin/pastefy
# You may have to set the permission
sudo chmod 777 /usr/local/bin/pastefy

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

# Login with pastefy (https://pastefy.ga/apikeys)
pastefy --key {api-key}

pastefy --delete {paste_id}

pastefy -f README.md --folder {folder_id}
```