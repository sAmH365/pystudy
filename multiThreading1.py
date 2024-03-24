import requests
import json
import time

# map 함수 사용법
# numList = [2, 3, 4, 5, 6]
# def add(x):
#     return x + 1
# result = map(add, numList)
# print(list(result))

urlList = [
    'https://tb.coinone.co.kr/api/v1/chart/olhc/?site=coinoneeth&type=1h&last_time=1609524000000',
    'https://tb.coinone.co.kr/api/v1/chart/olhc/?site=coinoneeth&type=1h&last_time=1608811200000',
    'https://tb.coinone.co.kr/api/v1/chart/olhc/?site=coinoneeth&type=1h&last_time=1608098400000',
    'https://tb.coinone.co.kr/api/v1/chart/olhc/?site=coinoneeth&type=1h&last_time=1606672800000',
    'https://tb.coinone.co.kr/api/v1/chart/olhc/?site=coinoneeth&type=1h&last_time=1605960000000',
    'https://tb.coinone.co.kr/api/v1/chart/olhc/?site=coinoneeth&type=1h&last_time=1605242700000',
    'https://tb.coinone.co.kr/api/v1/chart/olhc/?site=coinoneeth&type=1h&last_time=1604534400000',
    'https://tb.coinone.co.kr/api/v1/chart/olhc/?site=coinoneeth&type=1h&last_time=1603821600000',
    'https://tb.coinone.co.kr/api/v1/chart/olhc/?site=coinoneeth&type=1h&last_time=1603108800000',
    'https://tb.coinone.co.kr/api/v1/chart/olhc/?site=coinoneeth&type=1h&last_time=1602396000000',
]


def getCurrentVal(url):
    data = requests.get(url)
    dictionary = json.loads(data.content)
    return dictionary['data'][0]['Close']


# getCurrentVal(urlList[0])
# getCurrentVal(urlList[1])
# getCurrentVal(urlList[2])
# getCurrentVal(urlList[3])
# getCurrentVal(urlList[4])

# 멀티프로세싱 라이브러리
# .dummy를 붙이면 멀티쓰레딩 가능
from multiprocessing.dummy import Pool as ThreadPool

pool = ThreadPool(4)
result = pool.map(getCurrentVal, urlList)
print(result)

pool.close()
pool.join()
