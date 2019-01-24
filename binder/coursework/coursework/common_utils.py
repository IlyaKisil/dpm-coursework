import os
import pandas as pd


def read_data(file=1):
    DATA_HOME = os.path.join(os.path.dirname(__file__), "data", "file_{}.csv".format(file))
    df = pd.read_csv(DATA_HOME)
    return df
