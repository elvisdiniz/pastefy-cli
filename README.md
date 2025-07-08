# Pastefy CLI

A command-line interface for Pastefy, an open-source pastebin service.

## Installation

To install the Pastefy CLI, run the following command:

```bash
make install
```

This will build the `pastefy-cli` executable and install it in `~/.local/bin`.

## Usage

The Pastefy CLI can be used to:

* **Paste from a file:**

    ```bash
    pastefy-cli --file <file_path>
    ```

* **Paste from standard input:**

    ```bash
    # From string
    echo "Hello, world!" | pastefy-cli --title "My Paste"
    # From file
    cat <file_path> | pastefy-cli --title "My Paste"
    pastefy-cli --title "My Paste" < file_path
    ```

* **Set a title for your paste:**

    ```bash
    pastefy-cli --file <file_path> --title "My Paste"
    ```

* **Set your API key and base URL:**

    ```bash
    pastefy-cli --key <api_key> --base-url <base_url>
    ```

* **Set a folder for your paste:**

    ```bash
    pastefy-cli --file <file_path> --folder "My Folder"
    ```

* **Delete a paste:**

    ```bash
    pastefy-cli --delete <paste_id>
    ```

## Development

To build the `pastefy-cli` executable, run the following command:

```bash
make build
```

To run the tests, run the following command:

```bash
make test
```

To install the script in `~/.local/bin`, run:

```bash
make install
```

To clean up the build artifacts, run the following command:

```bash
make clean
```
