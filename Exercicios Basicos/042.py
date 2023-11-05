lista = []

while True:
    p = int(input('Digite um numero: '))
    lista.append(p)
    esc = str(input('Deseja continuar? [S]-[N] ')).upper()
    lista_len = len(lista)
    cinco = 5
    if cinco == lista:
        print('A lista possui numero 5.')

    if esc == 'N':
        break
print(f'Lista digitada : {lista}.')

print(f'Foram digitados {lista_len} numeros.')
lista.sort(reverse=True)
print(f'Os valores em ordem decrecente sao: {lista}')
if 5 in lista:
    print('Lista possui 5')
else:
    print('Lista nao possui 5')