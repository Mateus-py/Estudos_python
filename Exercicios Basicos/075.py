# - sistem de validaçao de usuario , sendo obrigatorio ter,+3 caracteres,idade entre 0 e 100,salario maior que 0,sexo f ou m,estado civil = s c v d
c = True
while c == True:
    nome = str(input('Digite um usuario: [3 ou mais caracteres] '))
    if len(nome) <= 3:
        print('Numero de caracteres invalido !!')
        continue
    else:
     c = False

c = True    

while c == True:
    idade = int(input('Digite uma idade: [De 0-100] '))
    if idade > 100:
        print('Idade invalida !!')
        continue
    else:
        c = False

c = True

while c == True:
   salario = int(input('Digite se salario mensal: R$'))
   if salario <= 0:
    print('Numero invalido !!')
    continue
   else:
    c = False

c = True

while c == True:
   estadocv = str(input('Digite seu estado civil de acordo com as seguintes letras : [S] - solteiro [C] - casado [V] - viuvo(a) [D] - divorciado: ')).upper()
   letras = ('SOLTEIRO','SOLTEIRA','CASADO','CASADA','VIUVO','VIUVA','DIVORCIADO','DIVORCIADA')

   if estadocv not in letras:
      print('Estado civil invalido !!')
      continue
   else:
      c = False

print(f'''
Nome: {nome}
Idade: {idade}
Salario: {salario}
Estado civil: {estadocv}''')