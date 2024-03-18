import requests
from bs4 import BeautifulSoup

data = requests.get('https://finance.naver.com/item/sise.nhn?code=005930')

# print(data.content)
# print(data.status_code)

soup = BeautifulSoup(data.content, 'html.parser')
print(soup.find_all('strong', id="_nowVal")[0].text)
print(soup.find_all('span', class_="tah")[5].text)
