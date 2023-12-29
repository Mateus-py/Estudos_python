from spacy import load

nlp = load('pt_core_news_sm')

doc = nlp('Mateus ama programar')

token = [token for token in doc]

# Existem dois tipos de analises de textos:
# Morfologica - Estudo das palavras e suas clsses gramaticais
# Sintatica - Funçao em que as palavras desempenham em oraçoes

# Atributos Lexicos:
# Taquemento POS(Part of speech)
# Classe gramatical: Mateus > subtantivo foi > verbo
# Lematizaçao
# Dependencias 
# Stopwords

for token in doc:
    print(f"{token.text} | {token.pos_} | {token.lemma_} | {token.dep_} | {token.is_stop}")