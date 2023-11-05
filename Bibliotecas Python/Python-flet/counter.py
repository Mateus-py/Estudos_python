import flet as ft


'''
Theory:
1) UserControl precisa chamar self.update() para mostrar as mudanças na pagina

2) super().__init__() precisa ser chamado no construtor as vezes
'''

class Counter(ft.UserControl):
    def __init__(self,Cont_ini):
        super().__init__()
        self.Cont_init = Cont_ini
        
        
    def add_click(self,e):
        self.Cont_init += 1
        self.text.value = str(self.Cont_init)
        self.update()
        
    def build(self):
        self.text = ft.Text(str(self.Cont_init))
        self.add_button = ft.ElevatedButton("+",on_click=self.add_click)
        return ft.Row([
            self.text,
            self.add_button
        ])

def main(page: ft.Page):
    page.add(
        Counter(100)
    )
ft.app(target=main)