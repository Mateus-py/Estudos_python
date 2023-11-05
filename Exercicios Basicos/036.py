op = ['SIM','NAO']
nota = 0


p1 = str(input('Telefonou para a vitima? ')).upper()
if p1 == op[0]:
    nota = nota + 1
elif p1 == op[1]:
    nota = nota - 1
p2 = str(input('Esteve no local do crime? ')).upper()
if p2 == op[0]:
    nota = nota + 1
elif p2 == op[1]:
    nota = nota - 1
p3 = str(input('Mora perto da vitima? ')).upper()
if p3 == op[0]:
    nota = nota + 1
elif p3 == op[1]:
    nota = nota - 1
p4 = str(input('Devia para a vitima? ')).upper()
if p4 == op[0]:
    nota = nota + 1
elif p4 == op[1]:
    nota = nota - 1

if nota == 0:
    print('Inocente')
if nota == (1,2):
    print('Suspeito')
if nota == (3,4):
    print('Assasino')

print(f'Nota igual ha {nota}')
