import flet as ft
from controltypewriter import TypeWriterControl

def main(page: ft.Page):
    page.title = 'Typewriter Effect'
    page.window_width = 400
    page.window_height = 500
    page.bgcolor = '#333333'
    page.theme_mode = 'dark'
    page.window_center()
    page.scroll = 'always'
    page.update()
    
    
    texto_random = '''
    chatgpt is a chatbot linguage model created by openia an launched in novenber 2022 '''
    
    
    page.add(
        TypeWriterControl(texto_random)
    )


ft.app(target=main)