import time
import datetime

t = time.time()

t = time.ctime(t)

t = time.localtime()
print('현재시간은 :' + str(t.tm_hour) + '시' + str(t.tm_min) + '분')

formatTime = time.strftime('%Y년 %m월 %d일 %H시 %M분 %S초', t)
print(formatTime)

name = 'Kim'
print('hi %s' % name)
print(f'안녕하세요 {name}')

a = datetime.datetime(2024, 3, 24, 10, 23, 00)
print(a)
