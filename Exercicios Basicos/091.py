board = ['#','#','#','#','#','#','#','#','#']
playerum = 'X'
playerdois = 'O'
def vezplayerum(pos):
    board[pos] = playerum
    return print(f'''
    [{board[0]}] - [{board[1]}] - [{board[2]}]
    [{board[3]}] - [{board[4]}] - [{board[5]}]
    [{board[6]}] - [{board[7]}] - [{board[8]}] 
    ''')
    

def vezplayerdois(pos):
    board[pos] = playerdois
    return print(f'''
    [{board[0]}] - [{board[1]}] - [{board[2]}]
    [{board[3]}] - [{board[4]}] - [{board[5]}]
    [{board[6]}] - [{board[7]}] - [{board[8]}] 
    ''')


nome = 'Jogo_da_velha'

p = str(input('Deseja JOGAR ou ver as REGRAS do jogo? ')).upper()[0]

if p == 'J':
    while True:
        print('#'* len(nome))
        print(nome)
        print('#'* len(nome))
        print(f'''
    [{board[0]}] - [{board[1]}] - [{board[2]}]
    [{board[3]}] - [{board[4]}] - [{board[5]}]
    [{board[6]}] - [{board[7]}] - [{board[8]}] 
    ''')
        p = int(input('Vez do player um:[0-8] '))
        vezplayerum(p)
        p = int(input('Vez do player dois:[0-8] '))
        vezplayerdois(p)

elif p == 'R':
    print('EM Construçao....')


