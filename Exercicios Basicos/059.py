from datetime import datetime
dados = {}

print('+-'*30)
dados['nome'] = str(input('Digite seu nome: '))
print('+-'*30)
dados['ano_de_nascimento'] = int(input('Ano de nascimento: '))
print('+-'*30)
dados['Carteira_trab'] = int(input('Numero do CTPS: [0] - nao possui: '))
print('+-'*30)
dados['idade'] = datetime.now().year - dados['ano_de_nascimento']
dados['ano_pos'] = dados['idade'] + 35
if dados['Carteira_trab'] == 0:
   print('=='*30)
   print(f'Nome: {dados["nome"]}')
   print('=='*30)
   print(f'Ano de nascimento: {dados["ano_de_nascimento"]}')
   print('=='*30)
   print(f'Idade: {dados["idade"]}')
   print('=='*30)
   print('Usuario nao possuim CTPS....')
   print('=='*30)
elif dados['Carteira_trab'] > 0:
    print('+-'*30)
    dados['ano_da_contrataçao'] = int(input('Ano da contrataçao: '))
    print('+-'*30)
    dados['salario'] = float(input('seu salario: '))
    print('=='*30)
    print('=='*30)
    print(f'Nome: {dados["nome"]}')
    print('=='*30)
    print(f'Ano de nascimento: {dados["ano_de_nascimento"]}')
    print('=='*30)
    print(f'Idade: {dados["idade"]}')
    print('=='*30)
    print(f'Ano da contrataçao: {dados["ano_da_contrataçao"]}')
    print('=='*30)
    print(f'Salario: R${dados["salario"]}')
    print('=='*30)
    print(f'Idade para a aposentadoria: {dados["ano_pos"]}')
    print('=='*30)