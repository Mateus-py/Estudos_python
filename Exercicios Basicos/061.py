pessoas = {}
dados = []
qtd_Homens = 0
while True:
    pessoas.clear()
    pessoas['Nome'] = str(input('Digite seu nome: '))
    while True:
        pessoas['Sexo'] = str(input('Digite qual seu sexo: [M/F] ')).upper()[0]
        if pessoas['Sexo']  in 'MF':
            break
        print('ERRO !! Por Favor, digite apenas M ou F')
        
    pessoas['idade'] = int(input('Digite sua idade: '))
    dados.append(pessoas.copy())
    while True:
        resp = str(input('Deseja continuar? [S/N] ')).upper()[0]

        if resp in 'SN':
            break
        print('Erro! Digite SIM ou NAO.')

    if resp == 'N':
        break
print('=='*30)
print(f'Pessoas cadastradas.... {len(dados)}')
for p in dados:
    if p['Sexo'] in 'Mn':
        qtd_Homens = qtd_Homens + 1
print(f'Homens cadastrados: {qtd_Homens}')