import requests
from bs4 import BeautifulSoup

# 크롤러 방지장치 우회 -> headers, Cookies

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'
}

cookie = {'name': '1234'}

r = requests.get(url='https://www.amazon.com/s?k=monitor&ref=nb_sb_noss_2', headers=headers, cookies=cookie)
# print(r.status_code)
# print(r.content)
soup = BeautifulSoup(r.content, 'html.parser')
# print(soup)
# titleSpanTag = soup.select('.a-size-medium')[0]
# print(titleSpanTag.text)
try:
    if r.status_code == 200:
        print(soup.select('.a-size-medium')[1000])
    else:
        print('error!!!')
except:
    print('index out of range')
