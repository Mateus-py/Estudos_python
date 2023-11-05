dados = [[],[]]
valor = 0

for num in range(1,8):
    valor = int(input(f'Digite o {num}° numero. '))
    if valor % 2 == 0:
        dados[0].append(valor) 
    else:
        dados[1].append(valor)

dados[0].sort()
dados[1].sort()
print(f'Valores pares {dados[0]}.')
print(f'Valores impares {dados[1]}')