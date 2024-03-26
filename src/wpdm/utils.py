import pandas as pd
import numpy as np


def foo(x, y):
    """

    :param x:
    :param y:
    :return:
    """
    return x - y


def printuj(f):
    print(f)


def fillMissingData(df):
    df.set_index('id')
    df.replace('?', np.nan, inplace=True)
    df
