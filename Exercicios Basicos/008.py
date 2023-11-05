import random

abc = ['a','b','c','d','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
num = ['0','1','2','3','4','5','6','7','8','9']

quant_alg = int(input('Com quantos algoritmos deseja criar senha? '))

for num_let in range(quant_alg):
    res = random.sample(abc , quant_alg)
    print(res)
