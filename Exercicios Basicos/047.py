dados = []
galera = []
maior = menor = 0

while True:
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Idade: ')))
    if len(galera) == 0:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]
    galera.append(dados[:])
    dados.clear()
    p = str(input('Deseja continuar ? [S/N]'))

    if p in 'Nn':
        break

qtd = len(galera)
print(f'Foram cadastradas {qtd} pessoas')
print(f'A maior idade  foi de {maior} anos')
print(f'A menor idade foi de {menor} anos')