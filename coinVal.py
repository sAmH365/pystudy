import requests
import json
import time

data = requests.get(
    'https://api-gateway.coinone.co.kr/exchange/chart/v1/KRW/ETH?lastDt=1710575100000&interval=15m&1711114451118')
# print(data.content)

dict = json.loads(data.content)

print(dict['body']['candles'][0])
# print(dict['body']['candles'][0]['close'])
# print(dict['body']['candles'][1]['close'])
# print(dict['body']['candles'][2]['close'])

dataList = dict['body']['candles']

for i, v in enumerate(dataList):
    print('========' + str(i) + '========')
    formatTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(v['dt'] / 1000))
    print('dt: ' + formatTime)
    print('close: ' + v['close'])

len(dict['body']['candles'])
