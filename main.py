#!/usr/bin/python3

import requests
import argparse


def paste(title, content):
    response = requests.post("https://pastefy.ga/create:paste", json={
        "content": content,
        "title": title
    })

    parsedResponse = response.json()

    if parsedResponse["success"]:
        return parsedResponse["id"]
    else:
        return False


if __name__ == '__main__':
    argParser = argparse.ArgumentParser(description="Pastefy CLI")
    argParser.add_argument("--file", "-f", type=str, help="Paste from file")
    argParser.add_argument("--title", "-t", type=str, help="Set Paste title")
    argParser.add_argument("--contents", "-c", type=str, help="Set Paste contents")

    parsed = argParser.parse_args()

    pasteInformation = {
        "create": False,
        "title": "",
        "content": None
    }

    if parsed.file is not None:
        pasteInformation["create"]  = True
        pasteInformation["title"]   = parsed.file
        pasteInformation["content"] = open(parsed.file).read()

    if parsed.title is not None:
        pasteInformation["title"] = parsed.title

    if parsed.contents is not None:
        pasteInformation["create"]  = True
        pasteInformation["content"] = parsed.contents

    if pasteInformation["create"]:
        if pasteInformation["content"].strip() == "":
            print("Can't paste. Content is empty")
        else:
            result = paste(pasteInformation["title"], pasteInformation["content"])

            if isinstance(result, bool) and result is False:
                print("Error during pasting")
            else:
                print("https://pastefy.ga/"+result)
