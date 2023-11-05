dados = []
galera = []

while True:
    dados.append(str(input('Digite seu nome: ')))
    dados.append(str(input('Digite seu peso: ')))
    galera.append(dados[:])
    dados.clear()

    p = str(input('Deseja continuar? [S/N]: ')).upper()



    if p == 'N':
        break
qtp = len(galera[0])

for p in galera:
    p_leves = []
    p_leves.append(p[1][1])
print(p_leves)




print(f'Foram registradas {qtp} pessoas.')