from modules.data.data_classes.data_collector import data_collector
from modules.data.data_classes.data_processor import preprocessor

class pipeline:
    def __init__(self, config: dict):
        self.config = config

    def run(self):
        collector = data_collector(self.config['data_files'])
        pre_data = collector.fetch_data()

        preprocess = preprocessor(pre_data)
        clean_data = preprocess.cleaner()
