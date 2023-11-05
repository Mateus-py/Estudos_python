estado  = {}
brasil = []

for c in range(0,3):
    estado['Uf'] = str(input('Unidade Federativa: '))
    estado['Sigla'] = str(input('Sigla: '))
    brasil.append(estado.copy())
print(brasil)