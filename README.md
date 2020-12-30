# Pastefy CLI

## Installation

### Linux
Installing it via moving file into /usr/bin
`INFO` requests, argparse python-packages are required
```bash
sudo cp main.py /usr/local/bin/pastefy
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