from spacy import blank

nlp = blank('pt')

doc = nlp('Mateus ama programar. Ele esta estudando PLN')

# Token e so uma parte do modelo
token = doc[0]
# span e um grupo do modelo
span = doc[0:3]

print(span)