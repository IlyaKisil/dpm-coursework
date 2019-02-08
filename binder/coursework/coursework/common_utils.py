import os
import pandas as pd
from .data import FILE_1, FILE_2


def read_data(file=1):
    if file == 1:
        df = pd.read_csv(FILE_1)
    else:
        df = pd.read_csv(FILE_2)
    return df
