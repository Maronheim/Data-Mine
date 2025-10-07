import numpy as n
from modules.data.data_classes.preprocess_classes.clean import clean

class preprocessor:
    def __init__(self, data: dict):
        self.data = data
        self.cleaned_data = {}

    def cleaner(self):
        for name, cln in self.data.items():
            cln = clean.drop_duplicates(cln)
            cln = clean.drop_na(cln)
            cln = clean.normalize(cln)

            self.cleaned_data[name] = cln

        return self.cleaned_data
    