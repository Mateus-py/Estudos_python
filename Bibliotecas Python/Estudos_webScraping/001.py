from bs4 import BeautifulSoup
import requests


url = 'https://www.mercadolivre.com.br/nintendo-switch-oled-64gb-standard-cor-branco-e-preto/p/MLB18537259?pdp_filters=deal:MLB779362-1&hide_psmb=true#promotion_type=DEAL_OF_THE_DAY&searchVariation=MLB18537259&deal_print_id=e1c9ac23-2e36-4b4c-83d6-6c397e9019da&position=5&search_layout=grid&type=product&tracking_id=90344be4-a3ab-4293-9e5e-9cb732366843&deal_print_id=cbd35de4-e2cb-4770-a7fb-cedab43bc362&promotion_type=DEAL_OF_THE_DAY'

result = requests.get(url)


site = BeautifulSoup(result.text,'html.parser')

price = site.find('span',attrs={'class':'andes-money-amount__fraction'})



print(price)

#with open('main.html','r')as f:
#    doc = BeautifulSoup(f,'html.parser')
    
# prettify() - Melhora a identaçao do arquivo html    
#print(doc.prettify())

# encontrando coisa pela Tag .title - mostra a tag titulo .string - mostra a string da tag
#tag = doc.title

#print(tag.string)

# outra maneira de encontrar e usando o comando find() e findall()

#tag = doc.find('p')

#print(tag)