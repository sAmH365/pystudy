for i in range(10):
    print('for loop')

# 리스트에서 데이터 뽑기
list = ['bmw', 'k5', 'spark']
for i in list:
    print('하이')
    print(i +'!!!!')

print('=============')

# for i in range(0, 3):
#     print(i)


# for i in range(1, 10):
#     for j in range(2, 9):
#         print(i * j)

# x = "My crypto portfolio amount in dallars is"
# y = 50000

# print(x + str(y))
# print("%s%s" % (x, y))
# print("{} {}".format(x, y))


for i in range(2, 10):
    for j in range(1, 10):
        print(str(i) + " x " + str(j) + " = " + str(i*j))
    print("=========")