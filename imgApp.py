from PIL import Image
import os

files = os.listdir('img')
print(files)

img = Image.open('img/photo1.jpg')
# img = img.resize((300, 500))
img.thumbnail((300, 500)) # 비율 맞춰서 줄여줌
img.save('img/new_photo1.jpg', quality=10) # jpg 파일은 quality옵션 사용, 기본 75 낮을수로 저화질
img = img.crop((50,50, 150, 150)) # 이미지 자르기 순서대로 왼쪽위부분, 오른쪽아래부분

img2 = Image.open('img/photo1.jpg').convert('L')  # L 옵션 주면 흑백 사진으로
img2.save('img/new_photo2.png')
img2.quantize(colors=256, method=None, kmeans=0, palette=None, dither=1) # png파일은 quantize 옵션사용


for i in files:
    img = Image.open(f'img/{i}')
    img.thumbnail((500, 2500))
    img.save(f'img/new_{i}')
