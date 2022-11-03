import json


class Settings:
    def __init__(self, name: str):
        self.name = f'{name}.jsonc'

    def make_settings(self, data: dict):
        with open(self.name, 'w') as f:
            json.dump(data, f, indent=4)
    
    def load_settings(self) -> dict:
        try:
            with open(self.name, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return {}
    def save_settings(self, data: dict):
        with open(self.name, 'w') as f:
            json.dump(data, f, indent=4)
    def update_settings(self, data: dict):
        try:
            old_data = self.load_settings()
            old_data.update(data)
            with open(self.name, 'w') as f:
                json.dump(old_data, f, indent=4)
        except FileNotFoundError:
            self.make_settings(data)

