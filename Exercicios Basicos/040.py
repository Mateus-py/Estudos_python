# digitar varios valores numericos cadastrar em uma lista
# se o numero se repetir ele nao sera adicionado
# no final exibir todos os valores em ordem crescente
list_num = []

while True:

    p = int(input('Digite um numero: '))
    if p not in list_num:
        list_num.append(p)
    r = str(input('Deseja continuar? [S] - [N]'))

    if r in 'Nn':
        break
print(list_num)