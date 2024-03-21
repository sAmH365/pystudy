import requests
from bs4 import BeautifulSoup

data = requests.get('https://search.naver.com/search.naver?ssc=tab.blog.all&sm=tab_jum&query=%EC%82%AC%EA%B3%BC')
soup = BeautifulSoup(data.text.replace('\\', ''), 'html.parser')

list = soup.select('a.api_text_lines')

# print(list[0].text)
# print(list[1].text)
# print(list[2].text)

# 쿼리스트링에 start부분 기준으로 무한스크롤시 응답값 바뀜 (네이버 블로그)
# data2 = requests.get(
#     'https://s.search.naver.com/p/review/47/search.naver?ssc=tab.blog.all&api_type=4&query=%EC%82%AC%EA%B3%BC&start'
#     '=31&nx_search_query=&nx_and_query=&nx_sub_query=&ac=0&aq=0&spq=0&sm=tab_jum&nso=&prank=31&ngn_country=KR'
#     '&lgl_rcode=09590107&fgn_region=&fgn_city=&lgl_lat=37.483064&lgl_long=126.978668&enlu_query'
#     '=IggCAGmCULiNAAAAuGDqbIuW1YP0vEg6kPSZvKThDfucDIms%2FudRHfdG8G6lrY51DY46PeYIbwkbS8xiuQe%2FoIEqRtzwRIiG3wqui'
#     '%2Ftz058dTtOPvONNyyOXU7E%3D&abt=&_callback=getBlogContents&_callback=getBlogContents&_=1711029739912')
