dados = {}
gols = []
soma = 0
# - gpp == gols em cd jogo

dados['Jogador'] = str(input('Nome do Jogador: '))

dados['num_part'] = int(input('Numero de partidas: '))

for part in range(0,dados['num_part']):
    gols.append(int(input(f'Quantos gols ele fez na {part + 1}º partida ? : ')))
dados['gpp'] = gols
for item in gols:
    soma = item + soma
dados['soma_gols'] = soma

print('=='*30)
print(f'Jogador: {dados["Jogador"]}')
print('=='*30)
print('=='*30)
print(f'Partidas jogadas: {dados["num_part"]}')
print('=='*30)
print('=='*30)
print('Em cada partida ele fez: ')
for item in gols:
    print(f'{item} GOLS.')
print('=='*30)
print(f'Soma dos gols: {dados["soma_gols"]}')
print('=='*30)