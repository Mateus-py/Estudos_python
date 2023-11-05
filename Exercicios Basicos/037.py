import random
lp = (['Flamengo','Fluminense','Gremio','Internacional','Vasco','Botafogo'])

random.shuffle(lp)

print(lp)

while True:
    user = str(input('Digite uma letra [A-Z] ')).lower


    if user == '0':
        break
