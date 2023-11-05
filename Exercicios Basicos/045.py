dados = []
galera = []
nomes = []
idade = []

for pessoa in range(0,3):
    dados.append(str(input('Digite se nome: ')))
    dados.append(int(input('Digite sua idade: ')))
    galera.append(dados[:])
    dados.clear()

print(galera)
for pessoa in galera:
    if pessoa[1] >= 18:
        print(f'{pessoa[0]} e maior de idade')
