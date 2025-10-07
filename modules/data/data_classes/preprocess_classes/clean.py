import pandas as panda

class clean: 
    def __init__(self, raw_data):
        self.raw_data = raw_data
        self.cleaned_data = {}

    def drop_duplicates(self):
        print("Checking for Duplicates")

    def drop_na(self):
        print("Checking for N/A's")

    def normalize(self):
        print("Normalizing Data & Column Names")
