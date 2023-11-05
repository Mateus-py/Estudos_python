import flet as ft
from random import randint
p1 = str(input('Digite o player 1: '))
p2 = str(input('Digite o player 2: '))

def main(page: ft.Page):
    global p1,p2
    page.title = 'Guess me'
    page.padding = 30
    
    # - Logica do sistema
    answer = randint(1,100)
    print('>',answer)
    
    # configurando as fontes
    
    page.fonts = {
        # - Key -> Value
        "Fraunces" : "fonts/Fraunces-Italic-VariableFont_SOFT,WONK,opsz,wght.ttf",
        "Space Grotesk" : "fonts/SpaceGrotesk-VariableFont_wght.ttf"      
    }
    
    player_1 = ft.TextField(label=p1,border_radius=20)
    player_2 = ft.TextField(label=p2,border_radius=20)
    
    result = ft.Text(font_family="Space Grotesk",color='blue',size=45)
    
    # - funçoes 
    
    def check_guess_1(e):
        if int(player_1.value) < answer:
            result.value = "Mais..."
            page.update()
        elif int(player_1.value) > answer:
            result.value = "Menos..."
            page.update()
        elif int(player_1.value) == answer:
            result.value = f"{p1} GANHOU !!!"
            page.update()
        if int(player_1.value) >= 101:
            result.value = "Algo errado nao esta certo...."
            page.update()  
    
    def check_guess_2(e):
        if int(player_2.value) < answer:
            result.value = "Mais..."
            page.update()
        elif int(player_2.value) > answer:
            result.value = "Menos..."
            page.update()
        elif int(player_2.value) == answer:
            result.value = f"{p2} GANHOU !!!"
            page.update()
        if int(player_2.value) >= 101:
            result.value = "Algo errado nao esta certo...."
            page.update()
            
    check_p1 = ft.ElevatedButton('Clique aqui para checar',on_click=check_guess_1)
    check_p2 = ft.ElevatedButton('Clique aqui para checar',on_click=check_guess_2)
    page.add(
        ft.Card(
        ft.Container(
            content=ft.Row(
            controls=[ft.Text(value='GUESS ME',font_family="Fraunces",size=26)],alignment = 'center'),padding=20),),
        ft.Column(
            controls=[
                ft.Text(value='Pense em um numero de 1-100',font_family="Space Grotesk"),
                ft.Row([player_1,check_p1]),
                ft.Row([player_2,check_p2]),
                result,
            ],
        )
        
    )


ft.app(target=main,assets_dir='assets')