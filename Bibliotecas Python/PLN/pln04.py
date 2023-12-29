from spacy import load,displacy

nlp = load('pt_core_news_sm')

doc = nlp('''Liev Tolstói é um famoso autor russo. Ele nasceu em 9 de setembro de 1828, na propriedade rural da família. Mais tarde, começou a estudar Direito na Universidade de Kazan, mas desistiu do curso. Também participou da Guerra da Crimeia (1853-1856). Além disso, fez grande sucesso como escritor.
O romancista, que faleceu em 20 de novembro de 1910, em Astapovo, é um dos principais autores do realismo russo. Seus romances apresentam análise psicológica, crítica social, fluxo de consciência, além da temática do adultério. Uma de suas narrativas mais conhecidas é o livro Guerra e paz.
Seus três primeiros livros obtiveram grande sucesso. Tolstói, então, deixou o exército em 1856 e decidiu morar em São Petersburgo. Em 1859, retornou a sua casa natal, onde abriu uma escola para atender aos filhos dos camponeses. No ano seguinte, partiu para a Europa Ocidental onde estudou Pedagogia. Em 1862, ele se casou com Sofia Andreevna (1844-1919).''')

# Aprendendo o Basico de Tokenizacao (Separacao de palavras)

token = [token for token in doc]


# Aprendendo o basico sobre Sentencas (Frases)

sents = doc.sents

for sent in sents:
    sent # As frases do texto
    # Lemmaticao e stemming

    frase01 = sent[0]

    print(f'{frase01.text} | {frase01}')