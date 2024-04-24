import os
import shutil  # 파이썬이용한 파일 복사

files = os.listdir('osTest')

# for i in os.listdir('osTest'):
#     os.rename(f'osTest/{i}', f'osTest/re-{i}')

# shutil.copy('osTest', 'shUtilTest')

for i in os.listdir('osTest'):
    shutil.copy(f'osTest/{i}', 'shUtilTest')

# os.path.join('경로', '경로2') 경로합치기 함수
# os.getcwd() 파일의 절대경로 얻기 (current working directory)
