import json


class Exporter:

    def __init__(self, filename):
        self.filename = filename

    def save_tasks(self, tasks):
        with open(self.filename, 'w') as file:
            json.dump(tasks, file, indent=2)
