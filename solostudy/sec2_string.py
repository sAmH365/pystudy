# format 함수
a = 52
b = 273
str = "{} + {} = {}".format(a, b, a + b)
print(str)
print('-' * 20)

# f-문자열 (파이썬 v3.7 이상)
str2 = f"{a} + {b} = {a+b}"
str3 =f"""\
{a} + {b} = {a+b}
{a} - {b} = {a-b}
{a} * {b} = {a*b} 
{a} / {b} = {a/b}\
"""
print(str2)
print(str3)
# split 함수
list1 = "10 20 30 40".split(" ")
list2 = "10-20-30-40".split("-")
print('-' * 20)

print(list1)
print(list2)