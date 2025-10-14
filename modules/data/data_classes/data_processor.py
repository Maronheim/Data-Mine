import numpy as n
import sqlite3 as s

from modules.data.data_classes.preprocess_classes.clean import clean

class preprocessor:
    def __init__(self, data: dict):
        self.data = data
        self.cleaned_data = {}
        
        con = s.connect("modules/data/data_files/sqlite3_test.db")
        print("CONNECTED TO SQLITE3")
        cur = con.cursor()

        res = cur.execute("SELECT * FROM sqlite_master")
        res.fetchone()

        print('RESULT: ', res.fetchone())

    def cleaner(self):
        for name, cln in self.data.items():
            cln = clean.drop_duplicates(cln)
            cln = clean.drop_na(cln)
            cln = clean.normalize(cln)

            self.cleaned_data[name] = cln

        return self.cleaned_data
    