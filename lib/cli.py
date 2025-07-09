import os
import select
import sys

from lib.config import Config
from lib.pastefy_api import PastefyAPI


class CLI:
    def __init__(self, api: PastefyAPI, config: Config):
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
