import flet as ft


def main(page: ft.Page):
    page.title = 'Madlib'
    page.theme_mode = 'dark'
    page.horizontal_alignment = 'center'
    page.padding = 40
    page.scroll = 'always'
    
    ocupation = ft.TextField(label='Emprego:',border_radius=20)
    subs1 = ft.TextField(label='Substantivo',border_radius=20)
    adje1 = ft.TextField(label='Adjetivo',border_radius=20)
    subs2 = ft.TextField(label='Substantivo',border_radius=20)
    verb1 = ft.TextField(label='Verbo',border_radius=20)
    adje2 = ft.TextField(label='Adjetivo',border_radius=20)
    verb2 = ft.TextField(label='Verbo',border_radius=20)
    subs3 = ft.TextField(label='Substantivo',border_radius=20)
    adje3 = ft.TextField(label='Adjetivo',border_radius=20)
    subs4 = ft.TextField(label='Substantivo',border_radius=20)
    
    
    final_madlib = ft.Text(color='#ffff00')
    
    title = ft.Text('Enjoy madlibs',color='#FFFFFF')
    
    def generate_mad(e):
        final_madlib.value = f'Hoje um {ocupation.value} chamado {subs3} entrou na escola'
        page.update()
    
    
    page.add(
        title,
        ft.Container(padding=ft.padding.only(bottom=10)),
        ft.Row([ocupation,subs1],alignment='center'),
        ft.Row([adje1,subs2],alignment='center'),
        ft.Row([verb1,adje2],alignment='center'),
        ft.Row([subs3,verb2],alignment='center'),
        ft.Row([subs4,adje3],alignment='center'),
        ft.ElevatedButton('Gerar o madlib',on_click=generate_mad),
        final_madlib,
    )



ft.app(target=main,assets_dir="assets")