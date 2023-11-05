import pandas as pd

tabela = pd.read_csv('brasil.csv')

tabela = tabela.plot('ensino')



print(tabela)