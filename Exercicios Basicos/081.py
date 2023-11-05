l1 = int(input('Digite um primeiro lado do triangulo: '))
l2 = int(input('Digite um segundo lado do triangulo: '))
l3 = int(input('Digite um terceiro lado do triangulo: '))

if l1 + l2 > l3:
    print('E um triangulo.')
elif l2 + l1 > l3:
    print('E um triangulo.')
elif l2 + l3 > l1:
    print('E um triangulo.')
elif l3 + l2 > l1:
    print('E um triangulo.')
elif l1 + l3 > l2:
    print('E um triangulo.')
elif l3 + l1 > l2:
    print('E um triangulo.')

# - Equilatero
if l1 == l2 == l3:
    print('E um triangulo equilatero !!!')
# - Escaleno
if l1 != l2 != l3:
    print('E um triangulo Escaleno !!!')

# - Isosceles
if l1 == l2:
    print('E um Triangulo isosceles !!!')
elif l1 == l3:
    print('E um Triangulo isosceles !!!')
elif l2 == l1:
    print('E um Triangulo isosceles !!!')
elif l2 == l3:
    print('E um Triangulo isosceles !!!')
elif l3 == l1:
    print('E um Triangulo isosceles !!!')
elif l3 == l2:
    print('E um Triangulo isosceles !!!')