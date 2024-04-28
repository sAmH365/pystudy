import pandas as pd

df = pd.read_csv('credit.csv')
groupedData = df.groupby("성별")['나이'].mean()
print(groupedData)

# print(df['나이'].mean())  # 평균값
# print(df['나이'].mode())  # 최빈값
# print(df['나이'].max())  # 최대값
# print(df['나이'].min())  # 최소값
# print(df['나이'].describe())  # 빠른통계

# 판다스에서 다루는 dataframe 자료형 -> 2차원 데이
# series -> 1차원 한줄 데이터
