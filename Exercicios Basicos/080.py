nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
nota3 = float(input('Digite a terceira nota: '))
nota4 = float(input('Digite a quarta nota: '))

conceito = 0

media = (nota1 + nota2 + nota3 + nota4) / 4

if media >= 9 and media <= 10:
    conceito = 'A'
    print('=='*30)
    print(f'Media: [{media}]')
    print(f'Conceito: [{conceito}]')
    print('Aluno: Aprovado')
    print('=='*30)
elif media >= 7.5 and media <= 9.0:
    conceito = 'B'
    print('=='*30)
    print(f'Media: [{media}]')
    print(f'Conceito: [{conceito}]')
    print('Aluno: Aprovado')
    print('=='*30)
elif media >= 6.0 and media <= 7.5:
    conceito = 'C'
    print('=='*30)
    print(f'Media: [{media}]')
    print(f'Conceito: [{conceito}]')
    print('Aluno: Reprovado')
    print('=='*30)
elif media >= 4.0 and media <= 6.0:
    conceito = 'D'
    print('=='*30)
    print(f'Media: [{media}]')
    print(f'Conceito: [{conceito}]')
    print('Aluno: Reprovado')
    print('=='*30)
elif media <= 4.0 and media >= 0:
    conceito = 'E'
    print('=='*30)
    print(f'Media: [{media}]')
    print(f'Conceito: [{conceito}]')
    print('Aluno: Reprovado')
    print('=='*30)