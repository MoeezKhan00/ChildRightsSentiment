# load_data.py
import pandas as pd

def load_csv(filepath):
    df = pd.read_csv(filepath, encoding='ISO-8859-1', names=["target", "ids", "date", "flag", "user", "text"])
    return df
