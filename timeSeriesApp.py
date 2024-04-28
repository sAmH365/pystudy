import pandas as pd
from pandas_datareader import data
import yfinance as yfin
import matplotlib.pyplot as plt

yfin.pdr_override()
# 주어진 기간 동안의 Apple 주식 데이터 가져오기
df = data.get_data_yahoo('AAPL', start='2019-01-01', end='2020-01-01')

# 종가 데이터 시각화
# df['Close'].plot()

df2 = data.get_data_yahoo('005930.KS', start='2019-01-01', end='2020-01-01')
df2['Close'] = df2['Close'].astype(float)
df2['Close'].plot()

# 플롯 보여주기
# plt.show()

print('=======================')
# 이동 평균선 그리기
df2['rolling5'] = df2['Close'].rolling(5).mean()
df2['rolling20'] = df2['Close'].rolling(20).mean()

df2['rolling5'].plot()
df2['rolling20'].plot()
plt.show()
