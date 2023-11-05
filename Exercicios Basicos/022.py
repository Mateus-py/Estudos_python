def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        print(f'Vc tem {idade} anos Voto negado')
    elif 16 <= idade < 18 or idade > 65:
        print(f'Vc tem {idade} anos Voto opcional')
    else:
        print(f'Vc tem {idade} anos VOTO OBRIGATORIO')

nasc = int(input('Em que ano vc nasceu? '))
print(voto(nasc))