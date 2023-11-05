from time import sleep

def ml():
    print('~'*30)
def contador(inicio,fim,contador):
    print(f'Contagem de {inicio} a {fim} de {contador} em {contador}')
    for item in range(inicio,fim,contador):
        sleep(0.5)
        print(f'{item}',end=' ', flush=True)

contador(10,-10,-2)