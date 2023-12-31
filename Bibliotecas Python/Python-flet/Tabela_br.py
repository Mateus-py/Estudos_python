import flet as ft
import requests


key_test = 'test_aa5063def6ce2aadc5f17a73d11fd5'

key = 'live_4cbc8dad8caa1b39d255d72a024aff'

link = "https://api.api-futebol.com.br/v1/campeonatos/10/tabela"

req = requests.get(link,headers={'Authorization' : f'Bearer {key}'})

req_json = req.json()

POS = [req_json[0]['posicao'],
       req_json[1]['posicao'],
       req_json[2]['posicao'],
       req_json[3]['posicao'],
       req_json[4]['posicao'],
       req_json[5]['posicao'],
       req_json[6]['posicao'],
       req_json[7]['posicao'],
       req_json[8]['posicao'],
       req_json[9]['posicao'],
       req_json[10]['posicao'],
       req_json[11]['posicao'],
       req_json[12]['posicao'],
       req_json[13]['posicao'],
       req_json[14]['posicao'],
       req_json[15]['posicao'],
       req_json[16]['posicao'],
       req_json[17]['posicao'],
       req_json[18]['posicao'],
       req_json[19]['posicao']]

PO = [req_json[0]['pontos'],
       req_json[1]['pontos'],
       req_json[2]['pontos'],
       req_json[3]['pontos'],
       req_json[4]['pontos'],
       req_json[5]['pontos'],
       req_json[6]['pontos'],
       req_json[7]['pontos'],
       req_json[8]['pontos'],
       req_json[9]['pontos'],
       req_json[10]['pontos'],
       req_json[11]['pontos'],
       req_json[12]['pontos'],
       req_json[13]['pontos'],
       req_json[14]['pontos'],
       req_json[15]['pontos'],
       req_json[16]['pontos'],
       req_json[17]['pontos'],
       req_json[18]['pontos'],
       req_json[19]['pontos']]
TIME = [req_json[0]['time']['nome_popular'],
       req_json[1]['time']['nome_popular'],
       req_json[2]['time']['nome_popular'],
       req_json[3]['time']['nome_popular'],
       req_json[4]['time']['nome_popular'],
       req_json[5]['time']['nome_popular'],
       req_json[6]['time']['nome_popular'],
       req_json[7]['time']['nome_popular'],
       req_json[8]['time']['nome_popular'],
       req_json[9]['time']['nome_popular'],
       req_json[10]['time']['nome_popular'],
       req_json[11]['time']['nome_popular'],
       req_json[12]['time']['nome_popular'],
       req_json[13]['time']['nome_popular'],
       req_json[14]['time']['nome_popular'],
       req_json[15]['time']['nome_popular'],
       req_json[16]['time']['nome_popular'],
       req_json[17]['time']['nome_popular'],
       req_json[18]['time']['nome_popular'],
       req_json[19]['time']['nome_popular']]
J = [req_json[0]['jogos'],
       req_json[1]['jogos'],
       req_json[2]['jogos'],
       req_json[3]['jogos'],
       req_json[4]['jogos'],
       req_json[5]['jogos'],
       req_json[6]['jogos'],
       req_json[7]['jogos'],
       req_json[8]['jogos'],
       req_json[9]['jogos'],
       req_json[10]['jogos'],
       req_json[11]['jogos'],
       req_json[12]['jogos'],
       req_json[13]['jogos'],
       req_json[14]['jogos'],
       req_json[15]['jogos'],
       req_json[16]['jogos'],
       req_json[17]['jogos'],
       req_json[18]['jogos'],
       req_json[19]['jogos']]
V = [req_json[0]['vitorias'],
       req_json[1]['vitorias'],
       req_json[2]['vitorias'],
       req_json[3]['vitorias'],
       req_json[4]['vitorias'],
       req_json[5]['vitorias'],
       req_json[6]['vitorias'],
       req_json[7]['vitorias'],
       req_json[8]['vitorias'],
       req_json[9]['vitorias'],
       req_json[10]['vitorias'],
       req_json[11]['vitorias'],
       req_json[12]['vitorias'],
       req_json[13]['vitorias'],
       req_json[14]['vitorias'],
       req_json[15]['vitorias'],
       req_json[16]['vitorias'],
       req_json[17]['vitorias'],
       req_json[18]['vitorias'],
       req_json[19]['vitorias']]
E = [req_json[0]['empates'],
       req_json[1]['empates'],
       req_json[2]['empates'],
       req_json[3]['empates'],
       req_json[4]['empates'],
       req_json[5]['empates'],
       req_json[6]['empates'],
       req_json[7]['empates'],
       req_json[8]['empates'],
       req_json[9]['empates'],
       req_json[10]['empates'],
       req_json[11]['empates'],
       req_json[12]['empates'],
       req_json[13]['empates'],
       req_json[14]['empates'],
       req_json[15]['empates'],
       req_json[16]['empates'],
       req_json[17]['empates'],
       req_json[18]['empates'],
       req_json[19]['empates']]
D = [req_json[0]['derrotas'],
       req_json[1]['derrotas'],
       req_json[2]['derrotas'],
       req_json[3]['derrotas'],
       req_json[4]['derrotas'],
       req_json[5]['derrotas'],
       req_json[6]['derrotas'],
       req_json[7]['derrotas'],
       req_json[8]['derrotas'],
       req_json[9]['derrotas'],
       req_json[10]['derrotas'],
       req_json[11]['derrotas'],
       req_json[12]['derrotas'],
       req_json[13]['derrotas'],
       req_json[14]['derrotas'],
       req_json[15]['derrotas'],
       req_json[16]['derrotas'],
       req_json[17]['derrotas'],
       req_json[18]['derrotas'],
       req_json[19]['derrotas']]
GP = [req_json[0]['gols_pro'],
       req_json[1]['gols_pro'],
       req_json[2]['gols_pro'],
       req_json[3]['gols_pro'],
       req_json[4]['gols_pro'],
       req_json[5]['gols_pro'],
       req_json[6]['gols_pro'],
       req_json[7]['gols_pro'],
       req_json[8]['gols_pro'],
       req_json[9]['gols_pro'],
       req_json[10]['gols_pro'],
       req_json[11]['gols_pro'],
       req_json[12]['gols_pro'],
       req_json[13]['gols_pro'],
       req_json[14]['gols_pro'],
       req_json[15]['gols_pro'],
       req_json[16]['gols_pro'],
       req_json[17]['gols_pro'],
       req_json[18]['gols_pro'],
       req_json[19]['gols_pro']]
GC = [req_json[0]['gols_contra'],
       req_json[1]['gols_contra'],
       req_json[2]['gols_contra'],
       req_json[3]['gols_contra'],
       req_json[4]['gols_contra'],
       req_json[5]['gols_contra'],
       req_json[6]['gols_contra'],
       req_json[7]['gols_contra'],
       req_json[8]['gols_contra'],
       req_json[9]['gols_contra'],
       req_json[10]['gols_contra'],
       req_json[11]['gols_contra'],
       req_json[12]['gols_contra'],
       req_json[13]['gols_contra'],
       req_json[14]['gols_contra'],
       req_json[15]['gols_contra'],
       req_json[16]['gols_contra'],
       req_json[17]['gols_contra'],
       req_json[18]['gols_contra'],
       req_json[19]['gols_contra']]
SG = [req_json[0]['saldo_gols'],
       req_json[1]['saldo_gols'],
       req_json[2]['saldo_gols'],
       req_json[3]['saldo_gols'],
       req_json[4]['saldo_gols'],
       req_json[5]['saldo_gols'],
       req_json[6]['saldo_gols'],
       req_json[7]['saldo_gols'],
       req_json[8]['saldo_gols'],
       req_json[9]['saldo_gols'],
       req_json[10]['saldo_gols'],
       req_json[11]['saldo_gols'],
       req_json[12]['saldo_gols'],
       req_json[13]['saldo_gols'],
       req_json[14]['saldo_gols'],
       req_json[15]['saldo_gols'],
       req_json[16]['saldo_gols'],
       req_json[17]['saldo_gols'],
       req_json[18]['saldo_gols'],
       req_json[19]['saldo_gols']]
APR = [req_json[0]['aproveitamento'],
       req_json[1]['aproveitamento'],
       req_json[2]['aproveitamento'],
       req_json[3]['aproveitamento'],
       req_json[4]['aproveitamento'],
       req_json[5]['aproveitamento'],
       req_json[6]['aproveitamento'],
       req_json[7]['aproveitamento'],
       req_json[8]['aproveitamento'],
       req_json[9]['aproveitamento'],
       req_json[10]['aproveitamento'],
       req_json[11]['aproveitamento'],
       req_json[12]['aproveitamento'],
       req_json[13]['aproveitamento'],
       req_json[14]['aproveitamento'],
       req_json[15]['aproveitamento'],
       req_json[16]['aproveitamento'],
       req_json[17]['aproveitamento'],
       req_json[18]['aproveitamento'],
       req_json[19]['aproveitamento']]

UJGS = [req_json[0]['ultimos_jogos'],
       req_json[1]['ultimos_jogos'],
       req_json[2]['ultimos_jogos'],
       req_json[3]['ultimos_jogos'],
       req_json[4]['ultimos_jogos'],
       req_json[5]['ultimos_jogos'],
       req_json[6]['ultimos_jogos'],
       req_json[7]['ultimos_jogos'],
       req_json[8]['ultimos_jogos'],
       req_json[9]['ultimos_jogos'],
       req_json[10]['ultimos_jogos'],
       req_json[11]['ultimos_jogos'],
       req_json[12]['ultimos_jogos'],
       req_json[13]['ultimos_jogos'],
       req_json[14]['ultimos_jogos'],
       req_json[15]['ultimos_jogos'],
       req_json[16]['ultimos_jogos'],
       req_json[17]['ultimos_jogos'],
       req_json[18]['ultimos_jogos'],
       req_json[19]['ultimos_jogos']]


def main(page:ft.Page):
    page.horizontal_alignment = 'center'
    page.vertical_alignment = 'center'
    page.scroll = True
    
    main_cont = ft.Container(
        width='360',
        height='640',
        bgcolor=ft.colors.GREEN_400,
        content=ft.ResponsiveRow([
            ft.Container(content=ft.Text('TABELA BR 2023',text_align='center'),bgcolor=ft.colors.GREEN_ACCENT),
            ft.Container(content=ft.Text('POS | PO | TIME | J | V | E | D | GP | GC | SG | UJGS | APR ',bgcolor=ft.colors.GREEN_800,size=10)),
            ft.Container(content=ft.Text(f'{POS[0] } |{PO[0] } | {TIME[0] } | {J[0] } | {V[0] }|{E[0] } | {D[0] } | {GP[0] }|{GC[0] }|{SG[0] }|{UJGS[0] }|{APR[0]}',bgcolor=ft.colors.GREEN_600,size=10)),
            ft.Container(content=ft.Text(f'{POS[1]} | {PO[1] } | {TIME[1] } | {J[1] } | {V[1] }|{E[1] } | {D[1] } | {GP[1] }|{GC[1] }|{SG[1] }|{UJGS[1] }|{APR[1]}',bgcolor=ft.colors.GREEN_600,size=10)),
            ft.Container(content=ft.Text(f'{POS[2]} | {PO[2] } | {TIME[2] } | {J[2] } | {V[2] }|{E[2] } | {D[2] } | {GP[2] }|{GC[2] }|{SG[2] }|{UJGS[2] }|{APR[2]}',bgcolor=ft.colors.GREEN_600,size=10)),
            ft.Container(content=ft.Text(f'{POS[3]} | {PO[3] } | {TIME[3] } | {J[3] } | {V[3] }|{E[3] } | {D[3] } | {GP[3] }|{GC[3] }|{SG[3] }|{UJGS[3] }|{APR[3]}',bgcolor=ft.colors.GREEN_600,size=10)),
            ft.Container(content=ft.Text(f'{POS[4]} | {PO[4] } | {TIME[4] } | {J[4] } | {V[4] }|{E[4] } | {D[4] } | {GP[4] }|{GC[4] }|{SG[4] }|{UJGS[4] }|{APR[4]}',bgcolor=ft.colors.GREEN_600,size=10)),
            ft.Container(content=ft.Text(f'{POS[5]} | {PO[5] } | {TIME[5] } | {J[5] } | {V[5] }|{E[5] } | {D[5] } | {GP[5] }|{GC[5] }|{SG[5] }|{UJGS[5] }|{APR[5]}',bgcolor=ft.colors.GREEN_600,size=10)),
            ft.Container(content=ft.Text(f'{POS[6]} | {PO[6] } | {TIME[6] } | {J[6] } | {V[6] }|{E[6] } | {D[6] } | {GP[6] }|{GC[6] }|{SG[6] }|{UJGS[6] }|{APR[6]}',bgcolor=ft.colors.GREEN_600,size=10)),
            ft.Container(content=ft.Text(f'{POS[7]} | {PO[7] } | {TIME[7] } | {J[7] } | {V[7] }|{E[7] } | {D[7] } | {GP[7] }|{GC[7] }|{SG[7] }|{UJGS[7] }|{APR[7]}',bgcolor=ft.colors.GREEN_600,size=10)),
            ft.Container(content=ft.Text(f'{POS[8]} | {PO[8] } | {TIME[8] } | {J[8] } | {V[8] }|{E[8] } | {D[8] } | {GP[8] }|{GC[8] }|{SG[8] }|{UJGS[8] }|{APR[8]}',bgcolor=ft.colors.GREEN_600,size=10)),
            ft.Container(content=ft.Text(f'{POS[9]} | {PO[9] } | {TIME[9] } | {J[9] } | {V[9] }|{E[9] } | {D[9] } | {GP[9] }|{GC[9] }|{SG[9] }|{UJGS[9] }|{APR[9]}',bgcolor=ft.colors.GREEN_600,size=10)),
            ft.Container(content=ft.Text(f'{POS[10]} | {PO[10] } | {TIME[10] } | {J[10] } | {V[10] } | {E[10] } | {D[10] }|{GP[10] }|{GC[10] }|{SG[10] }|{UJGS[10] }|{APR[10]}',bgcolor=ft.colors.GREEN_600,size=10)),
            ft.Container(content=ft.Text(f'{POS[11]} | {PO[11] } | {TIME[11] } | {J[11] } | {V[11] } | {E[11] } | {D[11] }|{GP[11] }|{GC[11] }|{SG[11] }|{UJGS[11] }|{APR[11]}',bgcolor=ft.colors.GREEN_600,size=10)),
            ft.Container(content=ft.Text(f'{POS[12]} | {PO[12] } | {TIME[12] } | {J[12] } | {V[12] } | {E[12] } | {D[12] }|{GP[12] }|{GC[12] }|{SG[12] }|{UJGS[12] }|{APR[12]}',bgcolor=ft.colors.GREEN_600,size=10)),
            ft.Container(content=ft.Text(f'{POS[13]} | {PO[13] } | {TIME[13] } | {J[13] } | {V[13] } | {E[13] } | {D[13] }|{GP[13] }|{GC[13] }|{SG[13] }|{UJGS[13] }|{APR[13]}',bgcolor=ft.colors.GREEN_600,size=10)),
            ft.Container(content=ft.Text(f'{POS[14]} | {PO[14] } | {TIME[14] } | {J[14] } | {V[14] } | {E[14] } | {D[14] }|{GP[14] }|{GC[14] }|{SG[14] }|{UJGS[14] }|{APR[14]}',bgcolor=ft.colors.GREEN_600,size=10)),
            ft.Container(content=ft.Text(f'{POS[15]} | {PO[15] } | {TIME[15] } | {J[15] } | {V[15] } | {E[15] } | {D[15] }|{GP[15] }|{GC[15] }|{SG[15] }|{UJGS[15] }|{APR[15]}',bgcolor=ft.colors.GREEN_600,size=10)),
            ft.Container(content=ft.Text(f'{POS[16]} | {PO[16] } | {TIME[16] } | {J[16] } | {V[16] } | {E[16] } | {D[16] }|{GP[16] }|{GC[16] }|{SG[16] }|{UJGS[16] }|{APR[16]}',bgcolor=ft.colors.GREEN_600,size=10)),
            ft.Container(content=ft.Text(f'{POS[17]} | {PO[17] } | {TIME[17] } | {J[17] } | {V[17] } | {E[17] } | {D[17] }|{GP[17] }|{GC[17] }|{SG[17] }|{UJGS[17] }|{APR[17]}',bgcolor=ft.colors.GREEN_600,size=10)),
            ft.Container(content=ft.Text(f'{POS[18]} | {PO[18] } | {TIME[18] } | {J[18] } | {V[18] } | {E[18] } | {D[18] }|{GP[18] }|{GC[18] }|{SG[18] }|{UJGS[18] }|{APR[18]}',bgcolor=ft.colors.GREEN_600,size=10)),
            ft.Container(content=ft.Text(f'{POS[19]} | {PO[19] } | {TIME[19] } | {J[19] } | {V[19] } | {E[19] } | {D[19] }|{GP[19] }|{GC[19] }|{SG[19] }|{UJGS[19] }|{APR[19]}',bgcolor=ft.colors.GREEN_600,size=10)),
            
        ])
    )
    
    page.add(
        main_cont
    )

ft.app(target=main)