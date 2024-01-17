# 파일 만들기
file = open('a.text', 'w') # writea모드로 오픈, 있으면 덮어쓰기,
# 'wb': binary모드로 오픈 => 이미지 파일같은경우

file.write('hello123\n') # 파일 내용 작성
file.close()

# 파일 내용 추가
file = open('a.text', 'a') # append모드
file.write('greeting\n')
file.close()


# 파일 읽기
file = open('a.text', 'r') # Read 모드로 오픈
print(file.read())
file.close()

# 엑셀 형식으로 파일 만들기
file = open('data.csv', 'w')
file.write('kim, lee, park')
file.close()

list = ['samsung', 'kakao', 'naver', 'daum']
str = ''
for el in list:
    str += '\n' + el
print(str)
file = open('result.txt', 'w')
file.write(str)
file.close()