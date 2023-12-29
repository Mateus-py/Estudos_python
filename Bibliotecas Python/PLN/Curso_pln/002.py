from spacy import load,explain

nlp = load('pt_core_news_sm')

doc = nlp('A Apple esta querendo comprar o Brasil por $1 Bi de reais')

for token in doc:
    token
    
    
# O atributo .dep_ retorna o marcador de dependência (ou termo sintático) previsto.   
# O atributo .head retorna o índice do token principal. Você pode pensar nele como o "pai" ao qual a palavra está conectada.

# Entidades nomeadas são "objetos do mundo real" que possuem um nome. Por exemplo: uma pessoa, uma organização ou um país.
#A propriedade doc.ents permite o acesso às entidades nomedas identificadas (previstas) pelo modelo de reconhecimento de entidades nomeadas
#Ela retorna um iterável de objetos do tipo Span, possibilitando o acesso ao texto e ao marcador através do atributo .label_.

for ent in doc.ents:
    print(f'{ent.label_} | {ent.text} {explain("MISC")}')