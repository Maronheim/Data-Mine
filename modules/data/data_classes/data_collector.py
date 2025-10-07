import pandas as panda

class data_collector:
    def __init__(self, data_sources: dict):
        self.data_sources = data_sources
        self.raw_data = {}

    def fetch_data(self):
        """Loads datasets from given sources."""
        for name, path in self.data_sources.items():
            print(f"Loading {name} data from {path}...")
            self.raw_data[name] = panda.read_csv(path)
        print("Data loaded successfully.")
        return self.raw_data