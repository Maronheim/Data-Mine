import pandas as panda
import os 

class data_collector:
    def __init__(self, data_files: dict):
        self.data_files = data_files
        self.raw_data = {}

    def fetch_data(self):
        """Loads datasets from given sources."""
        for name, path in self.data_files.items():
            current_dir = os.getcwd()
            print(f"Loading {name} data from {path}...")
            self.raw_data[name] = panda.read_csv(path)
        return self.raw_data