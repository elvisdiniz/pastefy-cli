#!/usr/bin/python3

import requests
import argparse
import json
import os, os.path
import pathlib

configTemplate = {
    "key": "--"
}

config = configTemplate
pathlib.Path(os.path.expanduser("~")+"/.config").mkdir(parents=True, exist_ok=True)
configPath = os.path.expanduser("~")+"/.config/pastefycli.json"

def paste(title, content, folder=""):
    global config
    response = requests.post("https://pastefy.ga/api/v2/paste", json={
        "content": content,
        "title": title,
        "folder": folder
    }, headers={
        "x-auth-key": config["key"]
    })

    parsedResponse = response.json()

    if parsedResponse["success"]:
        return parsedResponse["paste"]["id"]
    else:
        return False

def writeConfig(content):
    global config, configPath
    with open(configPath, "w") as configFile:
        config = {**configTemplate, **config, **content}
        json.dump(config, configFile)



if (not os.path.isfile(configPath)):
    writeConfig(config)
else:
    with open(configPath, "r") as configFile:
        config = json.load(configFile)

if __name__ == '__main__':
    argParser = argparse.ArgumentParser(description="Pastefy CLI")
    argParser.add_argument("--file", "-f", type=str, help="Paste from file")
    argParser.add_argument("--title", "-t", type=str, help="Set Paste title")
    argParser.add_argument("--contents", "-c", type=str, help="Set Paste contents")
    argParser.add_argument("--key", type=str, help="Set your api-key")
    argParser.add_argument("--folder", type=str, help="Set folder")
    argParser.add_argument("--delete", type=str, help="Deletes a paste")

    parsed = argParser.parse_args()

    pasteInformation = {
        "create": False,
        "title": "",
        "folder": "",
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

    if parsed.folder is not None:
        pasteInformation["folder"] = parsed.folder

    if pasteInformation["create"]:
        if pasteInformation["content"].strip() == "":
            print("Can't paste. Content is empty")
        else:
            result = paste(pasteInformation["title"], pasteInformation["content"], pasteInformation["folder"])

            if isinstance(result, bool) and result is False:
                print("Error during pasting")
            else:
                print("https://pastefy.ga/"+result)
    
    if parsed.key is not None:
        writeConfig({"key": parsed.key})
        
        response = requests.get("https://pastefy.ga/api/v2/user", headers={
            "x-auth-key": config["key"]
        })

        parsedResponse = response.json()
        if (parsedResponse["logged_in"]):
            print("Welcome "+parsedResponse["name"]+"!")
        else:
            print("Couldn't log in")


    if parsed.delete is not None:
        response = requests.delete("https://pastefy.ga/api/v2/paste/"+parsed.delete, headers={
            "x-auth-key": config["key"]
        })

        if (response.json()["success"]):
            print("Deleted")
        else:
            print("Couldn't delete")
    