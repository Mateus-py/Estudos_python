time = []
dados = []
jogadores = {}

while True:
    jogadores['Jogador'] = str(input('Jogador: '))
    jogadores['Quantidade_partidas'] = int(input(f'Quantas partidas {jogadores["Jogador"]} jogou ? : '))
    for item in range(0,jogadores['Quantidade_']):
        jogadores['gpp'] = int(input(f'[ {item + 1}ª ] - PARTIDA: '))
    dados.append(jogadores.copy())
    p = str(input('Registrar mais? [S/N]')).upper()[0]
    if p in 'nN':
        break
for item in dados:
    print(f'Jogadores Registrados: {item}')