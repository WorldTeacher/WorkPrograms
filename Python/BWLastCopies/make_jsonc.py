import json


class Settings:
    """
    This class will create a json file with the given name. In it, it will save the given data.
    """
    def __init__(self, name: str):
        self.name = f'{name}.json'

    def make_settings(self, data: dict):
        """
        This function will create a settings file with the given data.

        Args:
            data (dict): The data to be saved.
        """
        with open(self.name, 'w') as f:
            json.dump(data, f, indent=4)
    
    def load_settings(self) -> dict:
        """
        This function will load the settings file.

        Returns:
            dict: The data read from the settings file.
            IF Error: Returns an empty dict.
        """
        try:
            with open(self.name, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return {}
    def save_settings(self, data: dict):
        """
        This function will save the settings file with the given data.

        Args:
            data (dict): The data to be saved.
        """
        with open(self.name, 'w') as f:
            json.dump(data, f, indent=4)
    def update_settings(self, data: dict):
        """
        This function will update the settings file with the given data.

        Args:
            data (dict): The new, or updated data.
        """
        try:
            old_data = self.load_settings()
            old_data.update(data)
            with open(self.name, 'w') as f:
                json.dump(old_data, f, indent=4)
        except FileNotFoundError:
            self.make_settings(data)

