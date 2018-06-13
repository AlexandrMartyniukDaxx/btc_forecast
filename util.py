import numpy as np
import pandas as pd
from matplotlib import pyplot as plt


def mergeGoogleTrends (frames):
    currentCoef = 1
    current = frames[0]
    last = current.iloc[-1].values[1]
    rest = frames[1:]
    for ds in rest:
        first = ds.iloc[0].values[1]
        currentCoef = currentCoef * last / first
        last = ds.iloc[-1],
        ds[['trendIndex']] = ds[['trendIndex']].multiply(currentCoef);
        current = pd.concat([current, ds[1:]])
    
    return current.reset_index(drop=True)


def foldMarketData (df, n):
    result = df[:-n]
    features = ['O', 'H', 'L', 'C', 'Volume','Market Cap', 'trendIndex']
    for i in range(1, n+1):
        newFeatures = []
        for f in features:
            newFeatures.append(f + ' -' + str(i))

        next_fold = df[i:-(n-i+1)]
        # print(next_fold)
        result[newFeatures] = result[features] - next_fold[features].reset_index(drop=True)

    return result


def norm_arr_std(arr):
    mean = arr.mean()
    std = arr.std()

    normalized = (arr - mean) / std
    return normalized


def norm_minmax(df):
    return (df - df.min())/(df.max() - df.min())


def norm_df(df, skip=[]):
    result = df.copy()

    for feature in df.columns:
        if feature not in skip:
            result[feature] = norm_arr_std(result[feature])

    return result


def split(df, perc):
    msk = np.random.rand(df.shape[0]) < perc
    return df[msk], df[~msk]


def printMeanStd(dframe):
    for feature in dframe.columns:
        print(dframe[feature].mean(), dframe[feature].std())

