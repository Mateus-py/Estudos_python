import flet as ft



def main(page: ft.Page):
    page.title = 'Mudando de paginas'
    
    def mud_rota(route):
        page.views.clear()
        page.views.append(
            ft.View(
            '/',
            [ft.AppBar(title=ft.Text('Meu APP'),bgcolor=ft.colors.AMBER),
             ft.ElevatedButton(text='Ir para pagina Principal',on_click=lambda _: page.go('/store'))]
        ))
        
        if page.route == '/store':
            page.views.append(ft.View(
                '/store',
                [ft.AppBar(title=ft.Text('Meu APP'),bgcolor=ft.colors.AMBER),
                ft.ElevatedButton(text='Voltar para pagina Principal',on_click=lambda _: page.go('/'))]
            ))
            
        page.update()
        
    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)
        
    page.on_route_change = mud_rota
    page.on_view_pop = view_pop
    page.go(page.route)     
    
    
    
ft.app(target=main)