# - dar aumento de 20% se salario for 280$
# - dar aumento de 15% se salario for de 280$ a 700
# - dar aumento de 10% se salario for de 700$ a 1500
# - dar aumnento de 5% se for maior que 1500$
# - informar o salario antes do reajuste,percentual de aumento aplicado,valor do aumento e o novo salario.


sal = int(input('Por favor,digite seu salario: R$'))
alm1 = (20 / 100) * sal
alm2 = (15 / 100) * sal
alm3 = (10 / 100) * sal
alm4 = (5 / 100) * sal

if sal == 280:
    print('=='*30)
    print(f'Salario de ${sal}')
    print('=='*30)
    print(f'Recebera aumento de 20% que sera de R${alm1}')
    print('=='*30)
    print(f'Novo salario igual ha: R$ {sal + alm1}')
    print('=='*30)
if sal > 280 < 700:
    print('=='*30)
    print(f'Salario de ${sal}')
    print('=='*30)
    print(f'Recebera aumento de 15% que sera de R${alm2}')
    print('=='*30)
    print(f'Novo salario igual ha: R$ {sal + alm2}')
    print('=='*30)
if sal > 700 < 1500:
    print('=='*30)
    print(f'Salario de ${sal}')
    print('=='*30)
    print(f'Recebera aumento de 10% que sera de R${alm3}')
    print('=='*30)
    print(f'Novo salario igual ha: R$ {sal + alm3}')
    print('=='*30)
if sal > 1500:
    print('=='*30)
    print(f'Salario de ${sal}')
    print('=='*30)
    print(f'Recebera aumento de 5% que sera de R${alm4}')
    print('=='*30)
    print(f'Novo salario igual ha: R$ {sal + alm4}')
    print('=='*30)