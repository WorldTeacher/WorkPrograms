import os
import json

class Settings:
    def __init__(self):
        self.name="gui-settings.json"
        self.origin="settings.json"
    def load_settings(self)->dict:
        if os.path.isfile(self.name):
            with open(self.name, 'r') as f:
                return json.load(f)
        else:
            if os.path.isfile(self.origin):
                with open(self.origin, 'r') as f:
                    return json.load(f)
            else:
                self.make_settings()
    def save_settings(self, data:dict):
        with open(self.name, 'w') as f:
            json.dump(data, f, indent=4)
    def make_settings(self):
        data={
            "Bibliotheks-ID": "",
            "Sigel": ""
        }
        self.save_settings(data)
