import flet as ft

def main(page: ft.Page):
    page.title = 'Calculadora'
    page.horizontal_alignment = 'center'
    page.vertical_alignment = 'center'
    page.theme_mode = 'dark'
    page.bgcolor = 'blue'
    
    
    result = ft.Text(value='',size=40,text_align='center')
    cont_result = ft.Container(
            width=420,
            height=100,
            content=result,
            bgcolor=ft.colors.BLUE,
            border_radius=30,
            margin=10
        )
    
    
    def save7(e):
        result.value = str(result.value) + '7'
        page.update()
        
    def save8(e):
        result.value = str(result.value) + '8'
        page.update()
        
    def save9(e):
        result.value = str(result.value) + '9'
        page.update()
        
    def saveadd(e):
        result.value = str(result.value) + '+'
        page.update()
        
    def save6(e):
        result.value = str(result.value) + '6'
        page.update()
        
    def save5(e):
        result.value = str(result.value) + '5'
        page.update()
        
    def save4(e):
        result.value = str(result.value) + '4'
        page.update()
        
    def savenadd(e):
        result.value = str(result.value) + '-'
        page.update()
        
    def save3(e):
        result.value = str(result.value) + '3'
        page.update()
        
    def save2(e):
        result.value = str(result.value) + '2'
        page.update()
        
    def save1(e):
        result.value = str(result.value) + '1'
        page.update()
        
    def savemt(e):
        result.value = str(result.value) + '*'
        page.update()
        
        
    def save0(e):
        result.value = str(result.value) + '0'
        page.update()
        
    def saveeq(e):
        result.value = str(eval(result.value))
        page.update()
    
    def savedel(e):
        result.value = ''
        page.update()
        
        
    def savediv(e):
        result.value = str(result.value) + '/'
        page.update()
        
    row1 = ft.Row(
            [
                ft.ElevatedButton('7',expand=1,on_click=save7),
                ft.ElevatedButton('8',expand=1,on_click=save8),
                ft.ElevatedButton('9',expand=1,on_click=save9),
                ft.ElevatedButton('+',expand=1,on_click=saveadd),
            ]
        )

    row2 = ft.Row(
            [
                ft.ElevatedButton('6',expand=1,on_click=save6),
                ft.ElevatedButton('5',expand=1,on_click=save5),
                ft.ElevatedButton('4',expand=1,on_click=save4),
                ft.ElevatedButton('-',expand=1,on_click=savenadd),
            ]
        )
        
    row3 = ft.Row(
            [
                ft.ElevatedButton('3',expand=1,on_click=save3),
                ft.ElevatedButton('2',expand=1,on_click=save2),
                ft.ElevatedButton('1',expand=1,on_click=save1),
                ft.ElevatedButton('*',expand=1,on_click=savemt),
            ]
        )
        
    row4 = ft.Row(
            [
                ft.ElevatedButton('=',expand=1,on_click=saveeq,bgcolor=ft.colors.GREEN_400),
                ft.ElevatedButton('0',expand=1,on_click=save0),
                ft.ElevatedButton('Del',expand=1,on_click=savedel,bgcolor=ft.colors.RED_400),
                ft.ElevatedButton('/',expand=1,on_click=savediv)
            ]
        )

        
    return page.add(
        ft.Container(
            margin=10,
            padding=10,
            width=420,
            height=380,
            bgcolor='Black',
            border_radius=30,
            content=ft.Column(
            [
                cont_result,
                ft.Divider(),
                row1,
                row2,
                row3,
                row4,
                ]
            )
        ),
        ft.Text('@mateusxavier6, V_1.0',text_align='center')
    )
ft.app(target=main)


