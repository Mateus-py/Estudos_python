while True:
    num = int(input('Digite a quantidade de metros que deseja converter p/ centimetros: [0] - para parar  '))
    numincent = num * 100
    if num == 0:
        break
    print(f'{num} M/s convertido em centimetro e igual a {numincent} C/s.')