# nunu = {'q': 'eat', 'w': 'snowball'}
# garen = {'q': 'strike', 'w': 'courage'}

class Hero:
    def __init__(self, qSkill, wSkill):
        self.q = qSkill
        self.w = wSkill

    def hello(self):
        print('안녕하세요')


nunu = Hero('eat', 'snowball')
garen = Hero('strike', 'courage')

print(nunu.q, nunu.w)
print(garen.q, garen.w)
nunu.hello()
