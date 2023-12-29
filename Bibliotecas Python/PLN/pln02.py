from spacy import load

nlp = load('pt_core_news_sm')

doc = nlp('Mateus ama programar')

token = [token for token in doc]

for token in doc:
    print(f'{token.text} - {token.shape_} - {token.shape}')
