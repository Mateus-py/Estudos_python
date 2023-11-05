def ler_int(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('ERRO!!! Digite um numero inteiro valido.')
        if ok:
            break
    return valor

#Programa Principal

n = ler_int('Digite um numero: ')
print(f'Vc digitou o numero {n}')
