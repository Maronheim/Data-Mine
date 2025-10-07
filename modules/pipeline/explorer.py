import pandas as p

class explorer:
    def __init__(self, features: p.DataFrame):
        self.features = features

    def correl(self, target_df: p.DataFrame):
        #combined = p.merge(self.features, target_df, on='company', how='inner')
        #corr = combined.corr(numeric_only=True) 
        corr = "TRUE"
        return corr