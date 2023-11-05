import flet as ft
import speedtest
from time import sleep

def main(page: ft.page):
    # configurando a page
    page.title = 'Internet Speedtest'
    page.theme_mode = "dark"
    page.vertical_alignment = 'center'
    page.horizontal_alignment = 'center'
    page.window_bgcolor = 'blue'
    page.padding = 30
    page.bgcolor = '#000000'
    
    # - Possibilitar o scrolling
    page.auto_scroll = True
    
    # - Fonts page
    page.fonts = {
        'Fraunces' : 'fonts/Fraunces-Italic-VariableFont_SOFT,WONK,opsz,wght.ttf',
        'SpaceGrotesk' : 'fonts/SpaceGrotesk-VariableFont_wght.ttf'
    }
    # - Speedtest
    st = speedtest.Speedtest()
    
    # - Head
    apptitle = ft.Row(
        controls=[
            ft.Text('INTERNET',font_family='SpaceGrotesk',style="displayLarge",color='#ff3300'),
            ft.Text('SPEED',font_family='SpaceGrotesk',style="displayLarge",color='#ffff00')
        ],
        alignment='center'
    )
    
    # - Linhas do Container
    
    line1 = ft.Text(value='> Pressione Start Para Iniciar o Test...',font_family='SpaceGrotesk',color='#ffffff')
    line2 = ft.Text(value='',font_family='SpaceGrotesk',color='#1aff1a')
    line3 = ft.Text(value='',font_family='SpaceGrotesk',color='#1aff1a')
    progressbar1 = ft.ProgressBar(width=400, color='#0080ff',bgcolor='#eeeeee',opacity=0)
    progresstext1 = ft.Text(' ',opacity=0)
    progressroll1 = ft.Row([
        progressbar1,
        progresstext1
    ])
    line4 = ft.Text(value='',font_family='SpaceGrotesk',color='#0080ff')
    line5 = ft.Text(value='',font_family='SpaceGrotesk',color='#1aff1a')
    line6 = ft.Text(value='',font_family='SpaceGrotesk',color='#ffff00')
    progressbar2 = ft.ProgressBar(width=400, color='#0080ff',bgcolor='#eeeeee',opacity=0)
    progresstext2 = ft.Text(' ',opacity=0)
    progressroll2 = ft.Row([
        progressbar2,
        progresstext2
    ])
    line7 = ft.Text(value='',font_family='SpaceGrotesk',color='#0080ff')
    line8 = ft.Text(value='',font_family='SpaceGrotesk',color='#1aff1a')
    con_text = ft.Column(
        controls=[
            line1,
            line2,
            line3,
            progressroll1,
            line4,
            line5,
            line6,
            progressroll2,
            line7,
            line8,
        ])
    
    # - Container
    cont_speed = ft.Container(
        content=con_text,
        width=200,
        height=100,
        bgcolor='#4d4d4d',
        border_radius=30,
        padding=20,
        animate=ft.animation.Animation(1000,'BounceOut')
    )
    
    # - Animaçao do container
    def animate_cont(e):
        progressroll1.opacity = 0
        progressbar1.opacity = 0
        progressbar1.value = None
        progressroll2.opacity = 0
        progressbar2.opacity = 0
        progressbar2.value = None
        line1.value = ''
        line2.value = ''
        line3.value = ''
        line4.value = ''
        line5.value = ''
        line6.value = ''
        line7.value = ''
        line8.value = ''
        cont_speed.update()
        
        cont_speed.width = 700
        cont_speed.height = 400
        line1.value = '> Calculando aguarde um momento por favor'
        cont_speed.update()
        sleep(2)
        
        ideal_server = st.get_best_server()
        city = ideal_server['name']
        country = ideal_server['country']
        cc = ideal_server['cc']
        line2.value = f'> Encontrando o melhor servidor em {city},{country},[{cc}]'
        cont_speed.update()
        sleep(2)
        
        line3.value = '> Iniciando o teste de download'
        progressroll1.opacity = 1
        progressbar1.opacity = 1
        cont_speed.update()
        downloadspeed = st.download() / 1024 / 1024
        progressbar1.value = 1
        line4.value = f'> Velocidade de download de {str(round(downloadspeed,2))} Mbps'
        cont_speed.update()
        
        line5.value = '> Calculando a velocidade de Upload'
        cont_speed.update()
        sleep(1)
        
        line6.value = '> Iniciando o teste de Upload'
        progressroll2.opacity = 1
        progressbar2.opacity = 1
        cont_speed.update()
        upspeed = st.upload() / 1024 / 1024
        progressbar2.value = 1
        line7.value = f'> Velocidade de Upload de {str(round(upspeed,2))} Mbps'
        cont_speed.update()
        sleep(1)
        line8.value = '> Teste Finalizado \n\n >> App desenvolvido por Mateus Xavier Pereira'
        cont_speed.update()
        
    # - Adicionando os widgets
    page.add(
        apptitle,
        cont_speed,
        ft.IconButton(icon=ft.icons.PLAY_CIRCLE_FILL_OUTLINED,on_click=animate_cont,icon_color='#1aff1a',icon_size=70)
    )


ft.app(target=main, assets_dir="assets")
