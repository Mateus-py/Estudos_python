class Casa:
    def __init__(self,Telhado,comodos,moveis):
        self.Telhado = Telhado
        self.Telhado = comodos
        self.moveis = moveis

    def ent_casa(self):
        print('Estou entrando na casa...')

casa1 = Casa(Telhado='Grande',comodos='8',moveis='muitos')

casa1.ent_casa()