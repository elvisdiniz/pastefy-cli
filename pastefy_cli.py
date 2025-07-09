import select
import requests
import json
import os
import pathlib
import sys


class PastefyAPI:
    def __init__(self, config):
        self.config = config

    def paste(self, title, content, folder=""):
        response = requests.post(
            f"{self.config.get('baseUrl')}/api/{self.config.get('apiVersion')}/paste",
            json={"content": content, "title": title, "folder": folder},
            headers={"x-auth-key": self.config.get("key")},
        )
        parsed_response = response.json()
        if parsed_response.get("success"):
            return parsed_response["paste"]["id"]
        return False

    def delete_paste(self, paste_id):
        response = requests.delete(
            f"{self.config.get('baseUrl')}/api/{self.config.get('apiVersion')}/paste/{paste_id}",
            headers={"x-auth-key": self.config.get("key")},
        )
        return response.json().get("success", False)

    def get_user(self):
        response = requests.get(
            f"{self.config.get('baseUrl')}/api/{self.config.get('apiVersion')}/user",
            headers={"x-auth-key": self.config.get("key")},
        )
        return response.json()


class Config:
    def __init__(self, config_path=None):
        self.config_template = {
            "key": "--",
            "baseUrl": "https://pastefy.ga",
            "apiVersion": "v2",
        }
        self.config_path = config_path or os.path.expanduser(
            "~/.config/pastefycli.json"
        )
        self.config = self.load_config()

    def load_config(self):
        if not os.path.isfile(self.config_path):
            self.write_config(self.config_template)
            return self.config_template
        with open(self.config_path, "r") as config_file:
            return {**self.config_template, **json.load(config_file)}

    def write_config(self, content):
        pathlib.Path(os.path.dirname(self.config_path)).mkdir(
            parents=True, exist_ok=True
        )
        with open(self.config_path, "w") as config_file:
            self.config = {**self.config, **content}
            json.dump(self.config, config_file)

    def get(self, key):
        return self.config.get(key)


class CLI:
    def __init__(self, api, config):
        self.api = api
        self.config = config

    def run(self, args):
        if args.file:
            self.handle_file_paste(args)
        elif args.contents:
            self.handle_contents_paste(args)
        elif args.key and args.base_url:
            self.handle_login(args)
        elif args.delete:
            self.handle_delete(args)
        elif not args.file and not args.contents:
            if select.select([sys.stdin], [], [], 0.0)[0]:
                self.handle_stdin_paste(args, sys.stdin.read().strip())
            else:
                print(
                    "No content provided. Use --file or --contents or pipe content to stdin.",
                    file=sys.stderr,
                )
                sys.exit(1)

    def handle_file_paste(self, args):
        try:
            with open(args.file) as f:
                content = f.read()
            title = args.title or os.path.basename(args.file)
            self.paste_and_print(title, content, args.folder)
        except FileNotFoundError:
            print("File not found.", file=sys.stderr)
            sys.exit(1)

    def handle_contents_paste(self, args):
        self.paste_and_print(args.title, args.contents, args.folder)

    def handle_stdin_paste(self, args, stdin_content):
        self.paste_and_print(args.title, stdin_content, args.folder)

    def paste_and_print(self, title, content, folder):
        if not content.strip():
            print("Can't paste. Content is empty", file=sys.stderr)
            sys.exit(1)
        result = self.api.paste(title, content, folder)
        if result:
            print(f"{self.config.get('baseUrl')}/{result}")
        else:
            print("Error during pasting", file=sys.stderr)
            sys.exit(1)

    def handle_login(self, args):
        self.config.write_config({"key": args.key, "baseUrl": args.base_url})
        user_data = self.api.get_user()
        if user_data.get("logged_in"):
            print(f"Welcome {user_data.get('name')}!")
        else:
            print("Couldn't log in", file=sys.stderr)
            sys.exit(1)

    def handle_delete(self, args):
        if not args.yes:
            confirmation = input("Are you sure you want to delete this paste? [y/N] ")
            if confirmation.lower() != "y":
                print("Deletion cancelled.")
                sys.exit(0)

        if self.api.delete_paste(args.delete):
            print("Deleted")
        else:
            print("Couldn't delete", file=sys.stderr)
            sys.exit(1)
