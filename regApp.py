import re

# 정규식 : 문자를 검사하는 식

print('1. =====================')
a = re.findall('^a', 'abcdefg')  # a로시작하는지
g = re.findall('g$', 'abcdefg')  # g로 끝나는지
tmp = re.findall('\\$', 'abcdef$g')  # $ 찾기
tmp2 = re.findall('[abc]', 'abcdef$g')  # a 또는 b 또는 c를 포함하는지
tmp3 = re.findall('[a-zA-Z]', 'abcdef$g')
tmp4 = re.findall('[가-힣]', 'abcdef$g안녕하세요')
tmp5 = re.findall('[^0-9]', 'abcdef$g안녕하세요')  # 0부터 9가 아닌것
tmp6 = re.findall('[^가-힣]', 'abcdef$g안녕하세요')  # 한글이 아닌것
tmp7 = re.findall(r'\d', 'abcd321e2f$g안녕하세요')  # 모든 숫자를 나타낼때 (digit의 약자)
tmp8 = re.findall(r'\d\d', 'abcd321e2f$g안녕하세요')  # 숫자뒤에 숫자오는거 (두자리숫자)
tmp8 = re.findall(r'\d\d', 'abcd321e2f$g안녕하세요')  # 숫자뒤에 숫자오는거 (두자리숫자)
tmp9 = re.findall(r'\d{3}', 'abcd321e2f$g안녕하세요')  # 세자리 숫자찾기
tmp10 = re.findall(r'\D', 'abcd321e2f$g안녕하세요')  # \d가 아닌것 (숫자가 아닌 모든것)
tmp11 = re.findall(r'\s', 'abcd 321e2f $g안녕 하세요')  # 스페이스바 찾기
tmp12 = re.findall(r'\S', 'abcd 321e2f $g안녕 하세요')  # 스페이스바 아닌것 (= 모든문자)
tmp13 = re.findall('a+', 'aabcdaaaaaaaa321e2fㄱㄱㄱㄱㄱㄱ$g안녕 하세요')  # 반복해서 찾으라고 시킬때
tmp14 = re.findall('abc', 'aAbcAbdaaaaaaaa321e2fㄱㄱㄱㄱㄱㄱ$g안녕 하세요', re.IGNORECASE)  # 대소문자 구분안할 땐 re.IGNORECASE

print(a)
print(g)
print(tmp, '- tmp')
print(tmp2, '- tmp2')
print(tmp3, '- tmp3')
print(tmp4, '- tmp4')
print(tmp5, '- tmp5')
print(tmp6, '- tmp6')
print(tmp7, '- tmp7')
print(tmp8, '- tmp8')
print(tmp9, '- tmp9')
print(tmp10, '- tmp10')
print(tmp11, '- tmp11')
print(tmp12, '- tmp12')
print(tmp13, '- tmp13')
print(tmp14, '- tmp14')
print()

print('2. =====================')
date = '2022-1-1'
formatDate = re.sub(r'\-', '.', date)  # sub('이걸찾아서', '이걸로 바꿔주세요', '대상문자') 첫번째 파라미터는 정규식
print(formatDate)

str1 = 'Abcde$f^1243145'  # 문자열에서 숫자 다 제거하려면
str1Result = re.sub(r'\d', '', str1)
print(str1Result)

str2 = 'Abcde$f^1243145'  # 문자열에서 숫자만 남기고 싶으면
# str2Result = re.sub(r'[^\d]', '', str2)
str2Result = re.sub(r'\D', '', str2)
print(str2Result)

print('===================== 3. example1 - 이메일 형식이 맞는지 판단하는 정규식 =====================')
str1 = 'ksh@naver.com'
result = re.findall(r'\S+@\S+\.(?:com|co\.kr|go\.kr)', str1)  # ?: => 그룹에 포함된 문자열과 일치하지만 결과에 반환되지는 않음
print(result)

print(
    '===================== 4. example2 - 상품목록에 Mirror 또는 Sofa라는 영단어가 포함되어있으면 카테고리컬럼에 \'가구\'라고 기록하고 싶습니다 =====================')

print('===================== 5. example3 - 상품목록에 글자가 없고 숫자만 있으면 그 칸은 \'에러\'라는 단어로 바꾸고 싶습니다.  =====================')
