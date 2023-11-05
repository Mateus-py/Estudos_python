import flet as ft


'''
Theory:
1) UserControls possibilita a construçao isolada de componentes reutilizaveis,
combinando os Controls flet existentes.

2) UserControls precisa implementar a funçao build que e chamada para construir a UI controls

3) Funçao build precisa retornar uma instancia ou uma lista de controls
'''

class GreetingsControl(ft.UserControl):
    def build(self):
        text = ft.Text('Hello world')
        return text

def main(page: ft.Page):
    page.add(
        GreetingsControl()
    )
ft.app(target=main)