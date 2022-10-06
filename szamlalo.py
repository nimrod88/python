import random

szamlalo = 0
'''
x=0
while 3*x+2!=59:
    x=x+1
    print(x)

dobas = random.choice["fej", "írás"]
print(dobas)


szorzandó = 1
while szorzandó <= 10:
    szorzó = 1
    while szorzó <= 10:
        print(szorzandó, '*', szorzó, '=', szorzandó*szorzó)
        szorzó +=1
    print('')
    szorzandó+=1
'''
dobas = random.randint(1,7)
for i in range(1, 1000000):
    if dobas == 6:
        szamlalo=szamlalo+1
        print(szamlalo)

