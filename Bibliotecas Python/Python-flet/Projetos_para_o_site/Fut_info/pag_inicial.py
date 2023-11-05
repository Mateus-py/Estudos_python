import flet as ft
import requests


api_key = 'live_4cbc8dad8caa1b39d255d72a024aff'

api_key_test = 'test_aa5063def6ce2aadc5f17a73d11fd5'





def get_partida_ao_vivo(time_id,key):
    """_Pega partida ao vivo por ID_

    Args:
        time_id (_INT_): _O ID DO TIME DADO POR API-FUTEBOL_
        key (_STR_): _API-KEY DO API_FUTEBOL_

    Returns:
        _DIC_: _[Time Mandante,Placar Mandante,Time Visitante,Placar Visitante,Hora de inicio jogo]_
    """
    link_p_ao_vivo = f'https://api.api-futebol.com.br/v1/times/{time_id}/partidas/ao-vivo'
    req_p_ao_vivo = requests.get(link_p_ao_vivo,headers={'Authorization' : f'Bearer {key}'})
    req_json = req_p_ao_vivo.json()
    time_mandante = req_json['copa-do-brasil'][0]['time_mandante']['nome_popular']
    placar_mandante = req_json['copa-do-brasil'][0]['placar_mandante']
    time_visitante = req_json['copa-do-brasil'][0]['time_visitante']['nome_popular']
    placar_visitante = req_json['copa-do-brasil'][0]['placar_visitante']
    inicio_jogo = req_json['copa-do-brasil'][0]['hora_realizacao']
    
    dados = [time_mandante,placar_mandante,time_visitante,placar_visitante,inicio_jogo]
    return dados

def get_info_rodada(r,key):
    """_Descriçao_

    Args:
        r (_Int_): _Indicar a rodada equivalente_\n
        key (_API_KEY_): Chave da api

    Returns:
        _Dict_: _Retorna [[Num_rodada_atual,status_rodada_atual],[Jogos da rodada atual(0-10)]]_
    """
    link_rd = f'https://api.api-futebol.com.br/v1/campeonatos/10/rodadas/{r}'
    rod = requests.get(link_rd,headers={'Authorization' : f'Bearer {key}'})
    rod_json = rod.json()
    
    # - Nome , status
    st_rod = [rod_json['rodada'],rod_json['status']]
    part_rod_ante = []
    for i in range(0,10):
        part_rod_ante.append(rod_json['partidas'][i]['placar'])
    
    
    info_needed = [st_rod,part_rod_ante]
    return info_needed

# - Trazendo informaçoes da rodada atual
info_r_a = get_info_rodada(15,api_key)
num_e_status_rod_atual = info_r_a[0]
partidas_rod_atual = info_r_a[1]
# - Trazendo informaçoes da proxima Rodada
info_p_r = get_info_rodada(16,api_key)
num_e_status_rod_adiante = info_p_r[0]
partidas_rod_adiante = info_p_r[1]



def name_to_id(time):
    """_Conversor ID_to_string(api_futebol)_

    Args:
        time (_STR_): _Atençao usar .upper apos o argumento senao nao funciona_

    Returns:
        _INT_: _retorna o id do time_
    """
    ID = None
    if time == 'FLAMENGO':
        ID = 18
    elif time == 'BOTAFOGO':
        ID = 22
    elif time == 'FORTALEZA':
        ID = 131
    elif time == 'PALMEIRAS':
        ID = 56
    elif time == 'INTERNACIONAL':
        ID = 44
    elif time == 'FLUMINENSE':
        ID = 26
    elif time == 'CRUZEIRO':
        ID = 37
    elif time == 'GREMIO':
        ID = 45
    elif time == 'SAO PAULO':
        ID = 57
    elif time == 'ATLETICO-MG':
        ID = 30
    elif time == 'SANTOS':
        ID = 63
    elif time == 'BAHIA':
        ID = 68
    elif time == 'GOIAS':
        ID = 115
    elif time == 'CORINTHIANS':
        ID = 65
    elif time == 'CUIABA':
        ID = 204
    elif time == 'VASCO':
        ID = 23
    elif time == 'BRAGANTINO':
        ID = 64
    elif time == 'ATHLETICO-PR':
        ID = 185
    elif time == 'CORITIBA':
        ID = 84

    return ID

def name_to_id_api_dt(time):
    """_Conversor ID_to_string(futebol.data.org)_

    Args:
        time (_STR_): _Atençao usar .upper apos o argumento senao nao funciona_

    Returns:
        _INT_: _retorna o id do time_
    """
    T_ID = None
    if time == 'FLAMENGO':
        T_ID = 1783
    elif time == 'BOTAFOGO':
        T_ID = 1770
    elif time == 'FORTALEZA':
        T_ID = 3984
    elif time == 'PALMEIRAS':
        T_ID = 1769
    elif time == 'INTERNACIONAL':
        T_ID = 6684
    elif time == 'FLUMINENSE':
        T_ID = 1765
    elif time == 'CRUZEIRO':
        T_ID = 1771
    elif time == 'GREMIO':
        T_ID = 1767
    elif time == 'SAO PAULO':
        T_ID = 1776
    elif time == 'ATLETICO-MG':
        T_ID = 1766
    elif time == 'SANTOS':
        T_ID = 6685
    elif time == 'BAHIA':
        T_ID = 1777
    elif time == 'GOIAS':
        T_ID = 4250
    elif time == 'CORINTHIANS':
        T_ID = 1779
    elif time == 'CUIABA':
        T_ID = 4289
    elif time == 'VASCO':
        T_ID = 1780
    elif time == 'BRAGANTINO':
        T_ID = 4286
    elif time == 'ATHLETICO-PR':
        T_ID = 1768
    elif time == 'CORITIBA':
        T_ID = 4241
    elif time == 'AMERICA_MG':
        T_ID = 1838

    return T_ID

def get_squad_info(t_id):
    """_Info do Time_

    Args:
        t_id (_INT_): _ID do Time_

    Returns:
        _DIC_: _Retorna um dicionario com as seguintes infos\n[Tecnico,Equipe[Jogador,Posiçao,Nacionalidade]]_
    """
    url = f'https://api.football-data.org/v4/teams/{t_id}'
    headers = { 'X-Auth-Token': '06ea9151e7ca405280cf1bd43a396a7a' }
    response = requests.get(url, headers=headers)
    req_json = response.json()
    tecnico = req_json['coach']['name']
    Equipe = []
    for item in req_json['squad']:
        Equipe.append([item['name'],item['position'],item['nationality']])
    
    Dados = [tecnico,Equipe]
    
    
    return Dados

def main(page: ft.Page):
    verde = '#2FAD2F'
    verde_cinza = '#4C7D5B'
    
    # - fonts
    
    page.fonts = {
        'Ysabeau' : '/fonts/Ysabeau/Ysabeau-VariableFont_wght.ttf',
        'Josefin_Sans' : '/fonts/Josefin_Sans/JosefinSans-Bold.ttf'
    }
    
    # - Configuraçoes da pagina
    page.title = 'Fut.info'
    page.horizontal_alignment = 'center'
    page.vertical_alignment = 'center'
    page.scroll = True
    page.bgcolor = verde_cinza
    page.padding = 20
    
    
    
    # exit function
    def Exit(e):
        btn_Exit.visible = False
        search.visible = False
        btn_search_mn.visible = False
        cont_search.visible = False
        rec_info.visible = False
        page.update()
    
    # data function
    def get_nome_mandante(e):
        n = 'equipe'.upper()
        g_nome_mandante = search.value
        # - Getter das infos dos times
        dados_time_mandante = get_squad_info(name_to_id_api_dt(g_nome_mandante.upper()))
        Equipe = dados_time_mandante[1]
        info_time_mandante.controls.append(ft.Text(f'{n}:\nTecnico: {dados_time_mandante[0]}',font_family='Ysabeau'))
        for jogador in range(len(Equipe)):
            info_time_mandante.controls.append(ft.Divider())
            info_time_mandante.controls.append(ft.Text(f'Jogador: {dados_time_mandante[1][jogador][0]}\nPos: {dados_time_mandante[1][jogador][1]}\nNac: {dados_time_mandante[1][jogador][2]}'))
        page.update()
        
        

    
    try:
        l_rodada_atual = ft.ListView(controls=[ft.Text(f'{num_e_status_rod_atual[0]}ª Rodada\n\nStatus: {num_e_status_rod_atual[1]}',
                                                       font_family='Josefin_Sans',color='#000000')
                                               ],padding=10
                                     ,spacing=30)
        for i in range(len(partidas_rod_atual)):
            l_rodada_atual.controls.append(ft.Text(f'{partidas_rod_atual[i]}',font_family='Josefin_Sans',color='#000000'))
            l_rodada_anterior = ft.ListView(controls=[ft.Text(f'{num_e_status_rod_adiante[0]}ª Rodada\n\nStatus: {num_e_status_rod_adiante[1]}',font_family='Josefin_Sans',color='#000000')],padding=10,spacing=30)
        for i in range(len(partidas_rod_adiante)):
            l_rodada_anterior.controls.append(ft.Text(f'{partidas_rod_adiante[i]}',font_family='Josefin_Sans',color='#000000'))
    except:
        print('ERRO SEM CONEXAO !!')
        
        
    info_rodada_atual = ft.Container(
        width=300,
        bgcolor=verde,
        content=ft.Row(
            [
                l_rodada_atual,
            ],
        )
    )

    info_rodada_anterior = ft.Container(
        width=300,
        bgcolor=verde,
        content=ft.Row(
            [
                l_rodada_anterior,
            ],
        )
    )
    
    page_info = ft.Container(
        width=300,
        bgcolor=verde,
        content=ft.Column(
            [
                ft.Divider(),
                info_rodada_atual,
                ft.Divider(),
                info_rodada_anterior,
                ft.Divider(),
                ],
            alignment='center',
        ),
        border=ft.border.all(1,'#000000')
    )
        
    info_time_mandante = ft.ListView()
    cont_info_m = ft.Container(
        content=info_time_mandante
    )
    
    # Data function
    def back(e):
        body_app.content = body
        btn_search.visible = False
        btn_Exit.visible = False
        page.update()
    
    # data function
    def open_search_bar(e):
        cont_search.visible = True
        search.visible = True
        btn_search_mn.visible = True
        btn_Exit.visible = True
        page.update()
    
    
    search = ft.TextField(tooltip='Pesquisar Informaçao do clube ',focused_border_color=verde_cinza,color='#000000',visible=False)
    btn_search_mn = ft.ElevatedButton('Pesquisar',bgcolor=verde,visible=False,on_click=get_nome_mandante)
    cont_search = ft.Container(
        padding=ft.padding.all(30),
        width=300,
        bgcolor=verde,
        content=ft.ResponsiveRow([search,btn_search_mn]),
        visible=False
    )
    
    tabela_br = ft.Container(
        width=300,
        bgcolor='Green',
    )
    
    rec_info = ft.Text('Pesquise o elenco do seu time clicando no botao de pesquisa')
    pag_jogos = ft.Container(
            width=300,
            bgcolor=verde,
            border_radius=10,
            content=ft.Column(
                [
                    rec_info,
                    cont_search,
                    ft.ResponsiveRow([cont_info_m,ft.Divider()]),
                    tabela_br,
                    ft.ResponsiveRow([ft.Text('@mateusxavier6',text_align='center')],
                        )
                ],
            ),
            border=ft.border.all(1,'#000000'),
        )
    
    
    # change bar
    def change1(e):
        body_app.content = pag_jogos
        btn_search.visible = True
        if btn_search == True:
            btn_Exit.visible = True
        page.update()
    
    # change bar 
    def change2(e):
        body_app.content = page_info
        page.update()
    
    btn_1 = ft.ElevatedButton(text='Acompanhe informaçoes sobre um time',bgcolor=verde_cinza,color='#000000',on_click=change1)
    btn_2 = ft.ElevatedButton(text='Info rodada e tabela',bgcolor=verde_cinza,color='#000000',on_click=change2)
    body = ft.Container(
        width=300,
        bgcolor=verde,
        border=ft.border.all(1,"#000000"),
        content=ft.Column(
            [
                ft.Image(src='/images/banner.png'),
                ft.Text(value='Informaçoes sobre o Brasileirao e Copa Do Brasil em tempo real.',size=20,font_family='Ysabeau'),
                ft.Divider(),
                ft.Row(
                    [
                        btn_1,
                    ],
                    alignment='center'
                ),
                ft.Divider(),
                ft.Row(
                    [
                        btn_2
                    ],
                    alignment='center',
                ),
                ft.Divider(),
                ft.Text('@mateusxavier6 v1.0(Atualizado dia 05/05/2023 as 11:32)',
                                    text_align='center',)
                ],
            alignment='center',
            )
        )
    

    
    body_app = ft.Container(
        content=body
    )
    
    btn_Exit = ft.IconButton(icon=ft.icons.ARROW_BACK,visible=False,tooltip='Fechar barra de pesquisa',on_click=Exit)
    btn_search = ft.IconButton(icon=ft.icons.SEARCH,visible=False,tooltip='Pesquisar Time mandante',on_click=open_search_bar)
    page.add(
        ft.AppBar(bgcolor=verde,color='#000000',leading=btn_Exit,title=ft.Text('Fut.Info',font_family='Ysabeau',text_align='center'),
                  leading_width=40,center_title=True,actions=[btn_search,ft.IconButton(icon=ft.icons.HOME,tooltip='Voltar para HOME',on_click=back)]),
        body_app,
    )
    

    
ft.app(target=main,assets_dir='assets')