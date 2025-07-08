#!/usr/bin/python3

import argparse
from pastefy_cli import PastefyAPI, Config, CLI

def main():
    config = Config()
    api = PastefyAPI(config)
    cli = CLI(api, config)

    arg_parser = argparse.ArgumentParser(description="Pastefy CLI")
    arg_parser.add_argument("--file", "-f", type=str, help="Paste from file")
    arg_parser.add_argument("--title", "-t", type=str, help="Set Paste title")
    arg_parser.add_argument("--contents", "-c", type=str, help="Set Paste contents")
    arg_parser.add_argument("--key", type=str, help="Set your api-key")
    arg_parser.add_argument("--base-url", type=str, help="Set your base url address")
    arg_parser.add_argument("--folder", type=str, help="Set folder")
    arg_parser.add_argument("--delete", type=str, help="Deletes a paste")

    parsed_args = arg_parser.parse_args()
    cli.run(parsed_args)

if __name__ == '__main__':
    main()