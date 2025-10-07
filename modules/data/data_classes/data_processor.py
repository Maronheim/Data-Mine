import numpy as n
from modules.data.data_classes.preprocess_classes.clean import clean

class preprocessor:
    def __init__(self, data: dict):
        self.data = data
        self.cleaned_data = {}

    def cleaner(self):
        for name, cln in self.data.items():
            print("ITEM: \n", cln)

            cln = clean.drop_duplicates(cln)
            print("Duplicates Dropped")
            cln = clean.drop_na(cln)
            print("N/A's Dropped")
            cln = clean.normalize(cln)
            print("Data Normalized")

            self.cleaned_data[name] = cln
            print("Data Cleaned.")


        return self.cleaned_data
    