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

### Windows
/

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