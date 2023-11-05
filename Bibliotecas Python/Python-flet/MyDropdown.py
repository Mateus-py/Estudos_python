import flet as ft


def main(page: ft.Page):
    page.title = 'Color Dropdown app'
    page.horizontal_alignment = 'center'
    page.vertical_alignment = 'center'
    
    
    def click(e):
        print_submit.value = f'Vc selecionou a cor {color_drop.value}'
        page.update()
    
    color_drop = ft.Dropdown(
        width=300,
        options=[
            ft.dropdown.Option('Red'),
            ft.dropdown.Option('Green'),
            ft.dropdown.Option('Blue')
        ]
    )
    
    
    
    submit_btn = ft.ElevatedButton(text='submit',on_click=click)
    print_submit = ft.Text()
    
    page.add(
        color_drop,
        submit_btn,
        print_submit
    )



ft.app(target=main)