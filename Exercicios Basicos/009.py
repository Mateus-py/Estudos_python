import random

cond = True
num = ['0','1','2','3','4','5','6','7','8','9']
req = 0,1
qnt_num = int(input('Quantos numeros deseja usar? '))

while cond:
    aleat = random.sample(num,qnt_num)
    print(aleat)

    if aleat == req:
        break