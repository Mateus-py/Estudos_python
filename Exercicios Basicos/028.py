from time import sleep

print('''
    [V] - Volts
    ------------------------------
    [I] - Ampere
    ------------------------------
    [R] - Ohms
    ------------------------------
    [C] - Farads
    ------------------------------
    [L] - henrys
    ------------------------------
    [P] - watts
    ------------------------------''')
while True:

    exp = str(input('Digite o que vc deseja descobrir ,[0] - para sair do loop: ')).upper()
    sleep(0.5)

    if exp == 'V':
        t = int(input('Qual a voltagem/Tensao da sua residencia ? '))
        print(f'------- Tensao da sua residencia e de {t}v -------')
    if exp == 'I':
        t = int(input('Tensao envolvida : '))
        r = int(input('Resistencia em ohms : '))
        i = t / r
        print(f'------- Amperagem e de {i}A -------')
    if exp == 'R':
        t = int(input('Tensao envolvida : '))
        i = int(input('Corrente eletrica em ampere : '))
        r = t / i
        print(f'------- Resistencia igual a {r}ohms -------')
    if exp == 'C':
        q = int(input('Carga eletrica : '))
        t = int(input('Tensao envolvida : '))
        c = q / t
        print(f'------- Capacitancia de {c}f -------')
    if exp == 'L':
        print('------- Em breve -------')
    if exp == 'P':
        i = int(input('Corrente eletrica em ampere : '))
        v = int(input('Tensao envolvida : '))
        p = i * v
        print(f'------- Potencia igual a {p}watts -------')
    elif exp == '0':
        break