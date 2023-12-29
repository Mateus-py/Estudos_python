from spacy import load,displacy

nlp = load('pt_core_news_sm')

doc = nlp('Mateus ama programar mateusxavier1659@gmail.com')

token = [token for token in doc]

for token in doc:
    if token.like_email == True:
        print(f'Achei um email: ')
    
    
