import pandas as pd

# Ler o arquivo
tabela = pd.read_csv('brasil.csv')

#Lendo Dicionarios com o pandas
df = pd.DataFrame({
    'Nome' : ['Marcelo','Rian','Mateus'],
    'Idade' : [19, 18, 20],
    'Sexo' : ['Masc','Masc','Masc'],
    'Profissao' : ['Gamer','Youtuber','Programador']
})
df = df.describe()

#Definindo a column que quero usar
print(df)