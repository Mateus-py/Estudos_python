print('''

Tensao - [T]
---------------------------
Corrente eletrica - [I]
---------------------------
Resistencia eletrica - [R]
---------------------------
Capacitancia eletrica - [C]
---------------------------
Indutancia eletrica - [L]
---------------------------
''')
esc = str(input('Opçao : ')).upper()

if esc == 'T':
    print('E a diferença de potencial entre dois pontos de um circuito, que geralmente e medida em volts(V).')
if esc == 'I':
    print('E o fluxo de eletrons atravez de um circuito eletrico, que e medido em ampere.')
if esc == 'R':
    print('E a medida da oposiçao que um material apresenta ao fluxo de uma corrente eletrica,vque e medida geralmente em ohms.')
if esc == 'C':
    print('E a medida da capacidade de um determinado material de armazenar energia, que e medida em farad')
if esc == 'L':
    print('E a medida da capacidade de um determinado material de armazenar energia em um campo eletrico, que e medido em henrys')