matriz = []
num_par = []
soma = 0
for num in range(1,10):
    matriz.append(int(input(f'Digite o {num}º Valor: ')))


for numero in matriz:
    if numero % 2 == 0:
        num_par.append(numero)
for n in num_par:
        soma = soma + n
print(matriz)

print(f'Todos numeros pares somados e igual a {soma}')