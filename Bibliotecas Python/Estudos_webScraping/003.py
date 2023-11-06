from bs4 import BeautifulSoup
import requests as r
import re


# Pegar informaçoes sobre ultima e proxima partida de um time

url = 'https://onefootball.com/pt-br/time/flamengo-1802'

req = r.get(url=url)

site = BeautifulSoup(req.text,'html.parser')

def Get_last_match():

    ultimos_resultados = site.find('div',attrs={'class':'SimpleMatchCard_simpleMatchCard__content__ZWt2p'})

    times = ultimos_resultados.findAll('div',attrs={'class':'SimpleMatchCard_simpleMatchCard__teamContent__hQHVO SimpleMatchCardTeam_simpleMatchCardTeam___GPYH'})

    tag_nome_man = times[0].find('span',attrs={'class':'SimpleMatchCardTeam_simpleMatchCardTeam__name__7Ud8D'})
    tag_placar_man = times[0].find('span',attrs={'class':'SimpleMatchCardTeam_simpleMatchCardTeam__score__UYMc_'})

    tag_nome_vis = times[1].find('span',attrs={'class':'SimpleMatchCardTeam_simpleMatchCardTeam__name__7Ud8D'})
    tag_placar_vis = times[1].find('span',attrs={'class':'SimpleMatchCardTeam_simpleMatchCardTeam__score__UYMc_'})

    return print(f'{tag_nome_man.text} [{tag_placar_man.text}] x [{tag_placar_vis.text}] {tag_nome_vis.text}')

def Get_Next_match():
    
    Prox_part = site.findAll('div',attrs={'class':'XpaLayout_xpaLayoutContainerGridItemComponents__MaerZ'})
    
    Dados_prox_partida = Prox_part[1].text
    
    info = f'Proxima partida sera entre {Dados_prox_partida[15:23]} e {Dados_prox_partida[23:32]} dia {Dados_prox_partida[32:40]} as {Dados_prox_partida[40:45]}'
    
    return print(info)


Get_Next_match()