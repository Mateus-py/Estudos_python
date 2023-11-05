matriz = []
matriz_formated = []
num_par = []
for item in range(1,10):
    matriz.append(int(input(f'Digite o {item}º valor da matriz: ')))
    matriz_formated.append(matriz[:])
    matriz.clear()
print(f'''
 ( {matriz_formated[0]} ) - ( {matriz_formated[1]} ) - ( {matriz_formated[2]} )
 ( {matriz_formated[3]} ) - ( {matriz_formated[4]} ) - ( {matriz_formated[5]} )
 ( {matriz_formated[6]} ) - ( {matriz_formated[7]} ) - ( {matriz_formated[8]} )''')

for item in matriz_formated:
    # define o numero par
    if item[0] % 2 == 0:
        num_par.append(item[0])


soma = matriz_formated[2] + matriz_formated[5] + matriz_formated[8]
print('=-'*30)
print(num_par)
print(soma)

