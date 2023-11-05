matriz = []
matriz_formated = []

for item in range(1,10):
    matriz.append(int(input(f'Digite o {item}° valor da matriz : ')))
    matriz_formated.append(matriz[:])
    matriz.clear()
print(f'''
[{matriz_formated[0]}] - [{matriz_formated[1]}] - [{matriz_formated[2]}]

[{matriz_formated[3]}] - [{matriz_formated[4]}] - [{matriz_formated[5]}]

[{matriz_formated[6]}] - [{matriz_formated[7]}] - [{matriz_formated[8]}]''')