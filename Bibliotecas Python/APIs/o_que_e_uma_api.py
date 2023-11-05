# - Aplication programing interface 
# - Existem APIs publicas e privadas

import requests
import json

cotaçoes = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL')
cotaçoes = cotaçoes.json()
cotaçoes_btc = cotaçoes['BTCBRL']

print(cotaçoes_btc)