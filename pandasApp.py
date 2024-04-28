import pandas as pd

print('1. =====================')
df = pd.read_csv('credit.csv')
groupedData = df.groupby("성별")['나이'].mean()
print(groupedData)

# print(df['나이'].mean())  # 평균값
# print(df['나이'].mode())  # 최빈값
# print(df['나이'].max())  # 최대값
# print(df['나이'].min())  # 최소값
# print(df['나이'].describe())  # 빠른통계

# 판다스에서 다루는 dataframe 자료형 -> 2차원 데이터
# series -> 1차원 한줄 데이터
print('2. =====================')

# correlation 값 구하기 -> 관계도
# 1이랑 가까울수록 연관관계 높음
correlation = df[['나이', '사용금액']].corr()
print(correlation)

print('3. =====================')
data = df[df['나이'] > 50]  # 원하는 데이터만 필터주기
print(data)

print('4. =====================')
# 나이 컬럼 50이상, 성별 M, 기혼컬럼은 Married
# df.query() :: 여러가지 데이터 조건식을 한번에 주고 싶을때 query() 사용
result = df.query(" 나이 > 50 and 기혼 == 'Married' and 성별 == 'M' ")
print(result)

print('5. =====================')
# 기존 list 데이터를 dataframe으로 변환가능
shirts = [15, 20, 25]
pants = [150, 160, 170]

dic = {
    '셔츠': shirts,
    '바지': pants,
}
df2 = pd.DataFrame(dic)
print(df2)

print('6. example-1 =================')
# 검증하기: 결혼한 남자는 결혼 안한 남자에 비해 사용금액이 평균적으로 높은가?
marriedManAvg = df.query(" 기혼 == 'Married' and 성별 == 'M' ")['사용금액'].mean()
singleManAvg = df.query(" 기혼 == 'Single' and 성별 == 'M' ")['사용금액'].mean()

if marriedManAvg > singleManAvg:
    print('결혼한 남자는 결혼안한 남자에 비해 사용금액이 평균적으로 높다')
else:
    print('결혼한 남자는 결혼안한 남자에 비해 사용금액이 평균적으로 낮다')

print('7. example-2 =================')
# 검증하기: 소득이 높을 수록 사용금액이 평균적으로 높은가?
result = df.groupby('소득')['사용금액'].mean()  # 소득이 높을 수록 사용금액이 항상 많아지는건 아니다.

prev = 100000000
current = -999999999
flag = False

for data in result:
    current = data
    if current > prev:
        flag = True
        break
    else:
        prev = current
if flag:
    print('소득이 높을 수록 사용금액이 평균적으로 높지는 않다.')
else:
    print('소득이 높을 수록 사용금액이 평균적으로 높다.')
