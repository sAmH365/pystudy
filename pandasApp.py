import pandas as pd
import re

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

print('=========8. 엑셀 파일 오픈 + apply()=====================')
# pandas 엑셀파일 오픈
raw = pd.read_excel('product.xlsx', engine="openpyxl")  # openpyxl은 설치 해야함

# df에서 새 컬럼 만들고 싶으면
# raw['부가세포함'] = raw['판매가'] * 1.1

print('=========9. 부가세포함 컬럼 추가=====================')


# 컬럼 데이터를 쉽게 조작해주는 apply(함수)
# 특정 컬럼에 있는 모든 데이터를 함수에 넣었다 빼줌
def fun1(a):
    return a * 1.1


raw['부가세포함'] = raw['판매가'].apply(fun1)
print(raw);

print('=========10. 카테고리 값 추가=====================')


def fun2(data: str) -> str:
    data = str(data)

    if (data.__contains__('Chair')):
        return '의자'
    elif (data.__contains__('Table')):
        return '테이블'
    elif (data.__contains__('Mirror')):
        return '거울'
    elif (data.__contains__('Sofa')):
        return '소파'
    else:
        return '기타'


raw['카테고리'] = raw['상품목록'].apply(fun2)
print(raw)

print('=========11. 정규식으로 카테고리 값 추가=====================')


# a = re.search('^abc', 'ffabcdef')  # abc로 시작?
def fun2(data):
    if re.search('Chair', str(data)):
        return '의자'
    elif re.search('Table', str(data)):
        return '테이블'
    elif re.search('Mirror', str(data)):
        return '거울'
    elif re.search('Sofa', str(data)):
        return '소파'
    else:
        return '기타'


raw['카테고리'] = raw['상품목록'].apply(fun2)
print(raw)
