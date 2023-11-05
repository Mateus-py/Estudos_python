import flet as ft

def main(page: ft.Page):
    page.title = 'Chapter 3'
    page.theme_mode = 'light'
    page.vertical_alignment = 'center'
    
    txt = ft.TextField(
        value='0',
        width=100,
        text_align='center'
    )
    
    def remove(e):
        txt.value = int(txt.value) - 1
        page.update()
    
    def add(e):
        txt.value = int(txt.value) + 1
        page.update()
    
    page.add(
        ft.Row(
            controls=[
                ft.IconButton(ft.icons.REMOVE,on_click=remove),
                txt,
                ft.IconButton(ft.icons.ADD,on_click=add),
            ],
            alignment='center'
        )
    )

ft.app(target=main)