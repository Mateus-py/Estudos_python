aluno = {}
dados = []

aluno['Nome'] = str(input('Seu nome: '))
aluno['Media'] = int(input('Sua media: '))

if aluno['Media'] >= 7:
    print(f'O aluno {aluno["Nome"]} esta aprovado.')
else:
    print(f'O aluno {aluno["Nome"]} esta reprovado.')