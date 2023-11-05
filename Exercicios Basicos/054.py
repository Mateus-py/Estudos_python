clientes = []
Idprob = []

while True:
    print('''ID  ''')
    clientes.append(str(input('Nome Completo: ')))
    Idprob.append(int(input('ID do Problema: ')))
    p = str(input('Deseja continuar? [S/N] '))
    if p in 'Nn':
        break

print(f'Clientes Cadastrados... {clientes}')