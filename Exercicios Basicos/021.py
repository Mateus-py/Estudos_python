from random import randint
from time import sleep



def sorteia(list):
    numeros = list()
    for cont in range(0,5):
        numeros.append(randint(1,10))
    sleep(0.3)
    print(f' sorteando 5 numeros aleatorios.... {numeros}')

def somarpar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'Somndo os valores pares de {lista}, temos {soma}')

numero = list()
sorteia(list)
somarpar(list)