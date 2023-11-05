# Formata a matriz
matriz = [[0,0,0],[0,0,0],[0,0,0]]
# Cria a matriz
for linha in range(0,3):
    for coluna in range(0,3):
        matriz[linha][coluna] = int(input(f'Digite o valor para ({linha},{coluna}) '))
# Desenha a matriz
for linha in range(0,3):
    for coluna in range(0,3):
        print(f'[{matriz[linha][coluna]:^5}]',end=" ")
    print( )