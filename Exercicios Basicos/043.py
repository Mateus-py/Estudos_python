lista = []
lista_pares = []
lista_impares = []

while True:
    p = int(input('Digite um numero inteiro: '))
    lista.append(p)
    esc = str(input('Deseja continuar? [S] - [N] '))

    if esc in 'Nn':
        break
for i , v in enumerate(lista):
    if v % 2 == 0:
        lista_pares.append(v)
    if v % 2 == 1:
        lista_impares.append(v)

lista.sort(reverse=True)
lista_pares.sort(reverse=True)
lista_impares.sort(reverse=True)
print(lista)
print(f' Os valores pares sao {lista_pares}')
print(f' Os valores impares sao {lista_impares}')
