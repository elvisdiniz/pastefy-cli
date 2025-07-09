import requests

from lib.config import Config


class PastefyAPI:
    def __init__(self, config: Config):
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
