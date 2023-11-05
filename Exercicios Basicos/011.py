class Ser_humano:
    def __init__(self,idade,sexo,nome):
        self.idade = idade
        self.sexo = sexo
        self.nome = nome
    def conversar(self):
        print('Estou Conversando...')
eu = Ser_humano(idade='20',sexo='Masculino',nome='Mateus')

eu.conversar()