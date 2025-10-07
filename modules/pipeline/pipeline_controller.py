from modules.data.data_classes.data_collector import data_collector
from modules.data.data_classes.data_processor import preprocessor
from modules.pipeline.explorer import explorer
from modules.pipeline.feature_engineer import feature_engineer


class pipeline:
    def __init__(self, config: dict):
        self.config = config

    def run(self):
        print("---COLLECTING DATA---")
        collector = data_collector(self.config['data_files'])
        pre_data = collector.fetch_data()
        if not pre_data:
            print("No Data Found. \n")
        else:
            print("Data Collected. \n")

        print("---PREPROCESSING DATA---")
        preprocess = preprocessor(pre_data)
        clean_data = preprocess.cleaner()
        print("Data Preprocessed. \n")

        print("---PERFORMING INITAIL DATA EXPLORATION---")
        # Accept User Input for attribute to focus on
        explore = explorer(clean_data)
        explored_data = explore.correl(self.config['selection'])
        # Show Correlation and other analysis findings
        print("Data Explored. \n")

        print("---STARTING FEATURE ENGINEERING---")
        engineer = feature_engineer(explored_data)
        engineered_data = engineer.engineer_features()
        print("Features Engineered. \n")
