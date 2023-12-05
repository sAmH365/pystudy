print('hello')

someWord = '이런 문자가 있을 경우'

print(someWord[0:4])  # 이런 문
print()

# 리스트, 딕셔너리 자료 구조
중고차 = ['K5', 'whit', 5000]
중고차[1] = 'black'

중고차2 = { #딕셔너리 자료형(중괄호 사용)
    'brand': 'BMW',
    'model': '520d'
}
print(중고차[0])
print(중고차2['brand'])

중고차2['brand'] = 'abc123'
print(중고차2['brand'])