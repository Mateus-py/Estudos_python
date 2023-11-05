import flet as ft

def main(page: ft.Page):
    page.title = 'Chapter 3'
    page.theme_mode = 'light'
    page.horizontal_alignment = 'center'
    page.padding = 100
    user_name = ft.TextField(
        label='Seu nome:',
        width=300,
    )
    print_name_column = ft.Column()
    
    def ola(e):
        if not user_name.value:
            user_name.error_text =  'Esqueceu de colocar seu nome!'
            page.update()
        else:
            page.clean()
            print_name_column.controls.append(ft.Text(f'Bem vindo {user_name.value}'))
            page.add(print_name_column)
            page.update()
    page.add(
        user_name,
        ft.ElevatedButton('Diga Ola',on_click=ola),
    )
ft.app(target=main)