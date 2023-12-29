# Curso de PLN em -> 'https://course.spacy.io/pt/'

from spacy import load , blank

nlp = blank('pt')

doc = nlp('Mateus ama programar')

# O objeto token faz parte do objeto doc , nele e armazenado as 'palavras'

for token in doc:
    token
    
# O objeto span faz parte do objeto doc , representa uma ou mais palavras
# Ela pode ser acessado como uma lista fazendo slice por exemplo
span = doc[0]

# Atributos Lexicos: Index e texto

#print("Index:   ", [token.i for token in doc])
#print("Text:    ", [token.text for token in doc])

#print("is_alpha:", [token.is_alpha for token in doc])
#print("is_punct:", [token.is_punct for token in doc])
#print("like_num:", [token.like_num for token in doc])