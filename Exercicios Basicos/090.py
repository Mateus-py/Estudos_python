

def maiorval(*num):
    for valor in num:
        print(f'Valor analizado....: {valor}')
    print(f'O maior numero e {max(num)}')


maiorval(5,10,20,12,5)