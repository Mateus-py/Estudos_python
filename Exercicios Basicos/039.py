lista = []


for i in range(0,5):
    i = i + 1
    p = int(input(f'Digite o valor da Pos {i} '))
    p = lista.append(p)
    lista.sort(reverse=True)
print(lista)
print(f'O maior item da lista e {lista[0]} na posicao 1 ')
print(f'O menor item da lista e {lista[4]} na posicao 4')