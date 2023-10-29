import json


class Importer:

    def __init__(self, filename):
        self.filename = filename

    def read_tasks(self):
        try:
            with open(self.filename, 'r') as file:
                data = json.load(file)
                return data
        except FileNotFoundError:
            return []


    def get_tasks(self):
        decoded_data = self.read_tasks()
        return decoded_data if decoded_data else []