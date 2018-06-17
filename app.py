import pandas as pd
import util
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
import matplotlib.pyplot as plt
from sklearn import preprocessing
import indicators

print(pd.__version__)

print(indicators.OPEN)

trends = util.mergeGoogleTrends([pd.read_csv('./data/trends_1.csv'), pd.read_csv('./data/trends_2.csv')])
df = pd.read_csv('./data/btc_quotations.csv')
df['trendIndex'] = trends['trendIndex'].values
df = df.iloc[::-1]

# df_std = df.copy()
# df_minmax = df.copy()
# df_minmax[['O','H','L','C','Volume','Market Cap', 'trendIndex']] = preprocessing.MinMaxScaler().fit_transform(df_minmax[['O','H','L','C','Volume','Market Cap', 'trendIndex']])
# df_std[['O','H','L','C','Volume','Market Cap', 'trendIndex']] = preprocessing.StandardScaler().fit_transform(df_std[['O','H','L','C','Volume','Market Cap', 'trendIndex']])

# util.foldMarketData(df, 10)
with_macd = indicators.macd(df)
with_macd[['trendIndex', 'O', 'H', 'L', 'C', 'macd_val', 'macd_signal_line']].hist()
plt.show()
# folded = util.foldMarketData(df, 10)
# folded.plot()
# plt.show()


# print(df_std.head())
# print(df_minmax.head())
# df_minmax.hist()
# df_std.hist()
# plt.show()