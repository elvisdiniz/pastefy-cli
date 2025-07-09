import json
import os
import pathlib


class Config:
    config = {}

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
