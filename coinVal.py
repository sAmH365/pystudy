import requests
import json

data = requests.get(
    'https://api-gateway.coinone.co.kr/exchange/chart/v1/KRW/ETH?lastDt=1710575100000&interval=15m&1711114451118')
# print(data.content)

dict = json.loads(data.content)
# print(dict['candles'][0])

print(dict['body']['candles'][0]['close'])
print(dict['body']['candles'][1]['close'])
print(dict['body']['candles'][2]['close'])
