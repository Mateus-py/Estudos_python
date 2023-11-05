import flet as ft


def main(page: ft.Page):
    page.title = 'Basic To-do App'
    
    def checkbox_change(e):
        page.update()
        if swi_checkbox.value == True:
            otp_text.value = 'Swimming selecionado'
            page.update()
        if swi_checkbox.value == False:
            otp_text.value = 'Swimming Nao selecionado'
            page.update()
    
    swi_checkbox = ft.Checkbox(label='Swimming',value=False,on_change=checkbox_change)
    otp_text = ft.Text(value='Swimming Nao selecionado')
    
    page.add(
        swi_checkbox,
        otp_text
    )

ft.app(target=main)