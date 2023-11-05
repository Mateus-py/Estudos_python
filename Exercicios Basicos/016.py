class Personagem:
    vivo = ''
    def __init__(self,nome,nivel,força,hp,vivo):
        self.nome = nome
        self.nivel = nivel
        self.força = força
        self.hp = hp
        self.vivo = vivo
    
    def mostrar(self):
        print('.......................')
        print('Nome: ',self.nome)
        print('Nivel: ',self.nivel)
        print('Força: ',self.força)
        print('HP: ',self.hp)
        print('Vivo: ',self.vivo)
        vivo = 'Vivo' if self.vivo else 'Morto'
        print('.......................')
    def morrer(self):
        self.vivo == False
    def viver(self):
        self.vivo == True
    def andar(self):
        if(self.vivo):
            print('Estou morto')
        else:
            print('Estou vivo')

Rick = Personagem('Rick Grimes','1','10','10',False)
Rochelle = Personagem('rochelle bouvuer','1','10','10',False)
Negan = Personagem('Negan','1','10','10',False)



Rick.mostrar()
Negan.viver()

