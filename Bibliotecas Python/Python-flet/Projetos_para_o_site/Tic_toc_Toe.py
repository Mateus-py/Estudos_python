import flet as ft



def main(page: ft.Page):
  page.title = 'Tic Toc Toe'
  page.horizontal_alignment = 'center'
  page.vertical_alignment = 'center'
  page.bgcolor = ft.colors.BLUE_GREY
  
  text_cont1 = ft.Text(' ',text_align='center',size=30,visible=False)
  text_cont2 = ft.Text(' ',text_align='center',size=30,visible=False)
  text_cont3 = ft.Text(' ',text_align='center',size=30,visible=False)
  text_cont4 = ft.Text(' ',text_align='center',size=30,visible=False)
  text_cont5 = ft.Text(' ',text_align='center',size=30,visible=False)
  text_cont6 = ft.Text(' ',text_align='center',size=30,visible=False)
  text_cont7 = ft.Text(' ',text_align='center',size=30,visible=False)
  text_cont8 = ft.Text(' ',text_align='center',size=30,visible=False)
  text_cont9 = ft.Text(' ',text_align='center',size=30,visible=False)
  
  def reset(e):
    text_cont1.value = ' '
    text_cont2.value = ' '
    text_cont3.value = ' '
    text_cont4.value = ' '
    text_cont5.value = ' '
    text_cont6.value = ' '
    text_cont7.value = ' '
    text_cont8.value = ' '
    text_cont9.value = ' '
    page.update()
  
  def start(e):
    cont1.visible = True
    cont2.visible = True
    cont3.visible = True
    cont4.visible = True
    cont5.visible = True
    cont6.visible = True
    cont7.visible = True
    cont8.visible = True
    cont9.visible = True
    page.update()
    
    
  text_cont1 = ft.Text(' ',text_align='center',size=30,visible=False)
  text_cont2 = ft.Text(' ',text_align='center',size=30,visible=False)
  text_cont3 = ft.Text(' ',text_align='center',size=30,visible=False)
  text_cont4 = ft.Text(' ',text_align='center',size=30,visible=False)
  text_cont5 = ft.Text(' ',text_align='center',size=30,visible=False)
  text_cont6 = ft.Text(' ',text_align='center',size=30,visible=False)
  text_cont7 = ft.Text(' ',text_align='center',size=30,visible=False)
  text_cont8 = ft.Text(' ',text_align='center',size=30,visible=False)
  text_cont9 = ft.Text(' ',text_align='center',size=30,visible=False)

        
  def change1(e):
    text_cont1.visible = True
    text_cont1.value = 'X'
    cont1.content = text_cont1
    page.update()
  
  def change2(e):
    text_cont2.visible = True
    text_cont2.value = 'X'
    cont2.content = text_cont2
    page.update()

  def change3(e):
    text_cont3.visible = True
    text_cont3.value = 'X'
    cont3.content = text_cont3
    page.update()
    
  def change4(e):
    text_cont4.visible = True
    text_cont4.value = 'X'
    cont4.content = text_cont4
    page.update()
    
  def change5(e):
    text_cont5.visible = True
    text_cont5.value = 'X'
    cont5.content = text_cont5
    page.update()
    
  def change6(e):
    text_cont6.visible = True
    text_cont6.value = 'X'
    cont6.content = text_cont6
    page.update()
    
  def change7(e):
    text_cont7.visible = True
    text_cont7.value = 'X'
    cont7.content = text_cont7
    page.update()
    
  def change8(e):
    text_cont8.visible = True
    text_cont8.value = 'X'
    cont8.content = text_cont8
    page.update()
    
  def change9(e):
    text_cont9.visible = True
    text_cont9.value = 'X'
    cont9.content = text_cont9
    page.update()
    
    
    
  def changeO1(e):
    text_cont1.visible = True
    text_cont1.value = 'O'
    cont1.content = text_cont1
    page.update()
  
  def changeO2(e):
    text_cont2.visible = True
    text_cont2.value = 'O'
    cont2.content = text_cont2
    page.update()

  def changeO3(e):
    text_cont3.visible = True
    text_cont3.value = 'O'
    cont3.content = text_cont3
    page.update()
    
  def changeO4(e):
    text_cont4.visible = True
    text_cont4.value = 'O'
    cont4.content = text_cont4
    page.update()
    
  def changeO5(e):
    text_cont5.visible = True
    text_cont5.value = 'O'
    cont5.content = text_cont5
    page.update()
    
  def changeO6(e):
    text_cont6.visible = True
    text_cont6.value = 'O'
    cont6.content = text_cont6
    page.update()
    
  def changeO7(e):
    text_cont7.visible = True
    text_cont7.value = 'O'
    cont7.content = text_cont7
    page.update()
    
  def changeO8(e):
    text_cont8.visible = True
    text_cont8.value = 'O'
    cont8.content = text_cont8
    page.update()
    
  def changeO9(e):
    text_cont9.visible = True
    text_cont9.value = 'O'
    cont9.content = text_cont9
    page.update() 
    
    page.update()
    
  cont_header = ft.Container(
    content=ft.Text('Tic Toc Toe',text_align='center',size=30),
    padding=60
  )
  
  row_nav = ft.Row(
    [
      ft.ElevatedButton('Iniciar jogo',on_click=start),
      ft.ElevatedButton('Resetar Jogo',on_click=reset)
    ],
    alignment='center',
  )
  
  cont_nav = ft.Container(
    content=row_nav,
    padding=30,
  )
  
  text_cont1 = ft.Text(' ',text_align='center',size=30,visible=False)
  cont1 = ft.Container(
    content=text_cont1,
    width=50,
    height=50,
    bgcolor='red',
    border_radius=50,
    on_click=change1,
    on_long_press=changeO1,
    visible=False
  )
  
  text_cont2 = ft.Text(' ',text_align='center',size=30,visible=False)
  cont2 = ft.Container(
    content=text_cont2,
    width=50,
    height=50,
    bgcolor='red',
    border_radius=50,
    on_click=change2,
    on_long_press=changeO2,
    visible=False
  )
  
  text_cont3 = ft.Text(' ',text_align='center',size=30,visible=False)
  cont3 = ft.Container(
    content=text_cont3,
    width=50,
    height=50,
    bgcolor='red',
    border_radius=50,
    on_click=change3,
    on_long_press=changeO3,
    visible=False
  )
  
  text_cont4 = ft.Text(' ',text_align='center',size=30,visible=False)
  cont4 = ft.Container(
    content=text_cont4,
    width=50,
    height=50,
    bgcolor='red',
    border_radius=50,
    on_click=change4,
    on_long_press=changeO4,
    visible=False
  )
  
  text_cont5 = ft.Text(' ',text_align='center',size=30,visible=False)
  cont5 = ft.Container(
    content=text_cont5,
    width=50,
    height=50,
    bgcolor='red',
    border_radius=50,
    on_click=change5,
    on_long_press=changeO5,
    visible=False
  )
  
  text_cont6 = ft.Text(' ',text_align='center',size=30,visible=False)
  cont6 = ft.Container(
    content=text_cont6,
    width=50,
    height=50,
    bgcolor='red',
    border_radius=50,
    on_click=change6,
    on_long_press=changeO6,
    visible=False
  )
  
  text_cont7 = ft.Text(' ',text_align='center',size=30,visible=False)
  cont7 = ft.Container(
    content=text_cont7,
    width=50,
    height=50,
    bgcolor='red',
    border_radius=50,
    on_click=change7,
    on_long_press=changeO7,
    visible=False
  )
  
  text_cont8 = ft.Text(' ',text_align='center',size=30,visible=False)
  cont8 = ft.Container(
    content=text_cont8,
    width=50,
    height=50,
    bgcolor='red',
    border_radius=50,
    on_click=change8,
    on_long_press=changeO8,
    visible=False
  )
  
  text_cont9 = ft.Text(' ',text_align='center',size=30,visible=False)  
  cont9 = ft.Container(
    content=text_cont9,
    width=50,
    height=50,
    bgcolor='red',
    border_radius=50,
    on_click=change9,
    on_long_press=changeO9,
    visible=False
  )
  
  row1 = ft.Row(
    [
      cont1,
      cont2,
      cont3,
    ],
    alignment='center'
  )
  
  row2 = ft.Row(
    [
      cont4,
      cont5,
      cont6,
    ],
    alignment='center'
  )
  
  row3 = ft.Row(
    [
      cont7,
      cont8,
      cont9,
    ],
    alignment='center'
  )
  
  
  Tabuleiro = ft.Column(
    [
      row1,
      row2,
      row3,
    ]
  )
  
  page.add(
    cont_header,
    ft.Divider(),
    cont_nav,
    ft.Divider(),
    Tabuleiro,
      ft.Text('@mateusxavier6')
    )
    

ft.app(target=main)