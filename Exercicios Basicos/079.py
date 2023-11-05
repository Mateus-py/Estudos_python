hour_p_day = int(input('Quantas horas vc trabalha por dia? '))

hour_worked_mes = (hour_p_day * 7) * 4

sal_hour = int(input('Qual e o valor da sua hora de trabalho? $'))

sal_mes = sal_hour * hour_worked_mes
ir = (5 / 100) * sal_mes
inss = (10 / 100) * sal_mes
FGTS = (11 / 100) * sal_mes
val_formated = sal_mes - (ir + inss)

print('=='*30)
print(f'Salario Bruto de ${sal_mes}')
print('=='*30)
print(f'| Valores descontados - IR = ${ir}')
print(f'| Valores descontados - INSS = ${inss}')
print(f'| Valores descontados - FGTS = ${FGTS}')
print('=='*30)
print(f'Descontos totais: ${ir + inss}')
print(f'Valor liquido: ${val_formated}')
print('Obs: FGTS pago pela empresa.')
