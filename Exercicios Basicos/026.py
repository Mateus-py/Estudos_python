num_ext = ('zero','um','dois','tres','quatro','cinco','seis','sete','oito','nove','dez')
while True:
    n = int(input('Digite um numero de 1 a 10: '))
    print(f'Vc Digitou o numero {num_ext[n]}')
    if n > 10:
        break
print('Numero invalido !!!')