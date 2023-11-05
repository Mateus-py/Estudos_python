import pandas as pd

# Ler o arquivo
tabela = pd.read_csv('brasil.csv')

#Exibe apens 8 linhas e colunas
#tabela_head = tabela.head(8)
#Exibe a tabela em tipos de dados
#tabela_dtype = tabela.dtypes
#Exibe informaçoes sobre a tabela
tabela_info = tabela.info()

#print(tabela_head)
#print(tabela_dtype)
print(tabela_info)