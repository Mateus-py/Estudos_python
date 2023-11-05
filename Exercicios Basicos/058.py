from random import randint
from time import sleep
from operator import itemgetter

jogadores = {'Jogador1' : randint(1,6),'Jogador2' : randint(1,6),'Jogador3' : randint(1,6),'Jogador4' : randint(1,6)}

ranking = {}

for k ,v in jogadores.items():
    print(f'{k} pegou {v} no dado.')
    sleep(1)

ranking = sorted(jogadores.items(), key=itemgetter(1))