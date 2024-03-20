import requests
from bs4 import BeautifulSoup

data = requests.get('https://finance.naver.com/item/sise.nhn?code=005930')

# print(data.content)
# print(data.status_code)

soup = BeautifulSoup(data.content, 'html.parser')
print(soup.find_all('strong', id="_nowVal")[0].text)
print(soup.find_all('span', class_="tah")[5].text)

# css 셀렉터 입력해서 찾을수있음
soup.select('strong#_nowVal')
# result = soup.select('#tab_con1 .gray')  # class명이 f_down 이면서 그안에 있는 <em> 태그 찾기
result = soup.find('th', string='동일업종 등락률').find_next_sibling('td').find('em').text.strip()
print(result)

img = soup.select('#img_chart_area')[0]
print(img['src'])

soup = BeautifulSoup(requests.get('https://finance.naver.com/item/sise.nhn?code=066575').content, 'html.parser')
print(soup.find_all('strong', id="_nowVal")[0].text)
print(soup.find_all('span', class_="tah")[5].text)

#tab_con1 > div:nth-child(6) > table > tbody > tr:nth-child(2) > td > em