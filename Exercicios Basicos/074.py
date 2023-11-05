salary_per_hour = float(input('Digite quanto vc ganha por hora: R$'))

hour_worked_per_day = int(input('Digite quantas horas trabalha por dia: '))

hour_worked_per_week = hour_worked_per_day * 7

hour_worked_per_m = hour_worked_per_week * 4

salary_per_week = salary_per_hour * hour_worked_per_week

salary_per_m = salary_per_hour * hour_worked_per_m

print(f'Vc recebe R${salary_per_m} por mes.')