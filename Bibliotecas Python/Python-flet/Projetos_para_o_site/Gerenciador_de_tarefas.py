import flet as ft


def main(page: ft.Page):
    # - Configuraçao da pagina
    page.title = 'Gerenciador de Tarefas'
    page.horizontal_alignment = 'center'
    page.theme_mode = 'dark'
    
    def c_theme(e):
        if page.theme_mode == 'dark':
            page.theme_mode = 'light'
            page.update()
        elif page.theme_mode == 'light':
            page.theme_mode = 'dark'
            page.update()
        else:
            page.theme_mode = 'dark'
            page.update()
    
    def remtar(e):
        for item in act_tar:
            act_tar.remove(item)
            page.update()
    
    def appeartf(e):
        add_button.visible = False
        Text_f.visible = True
        btn_adc.visible = True
        div1.visible = True
        div2.visible = True
        page.update()
        
    def get_tar(e):
        div1.visible = False
        div2.visible = False
        add_button.visible = True
        Text_f.visible = False
        btn_adc.visible = False
        rem_tar.visible = True
        page.update()
        def add_to_done(e):
            if checkb.value == True:
                act_done.append(ft.Text(f'{checkb.label} Concluido'))
                page.update()
            elif checkb.value == False:
                for item in act_done:
                    act_done.remove(item)
                    page.update()
        checkb = ft.Checkbox(label=Text_f.value,on_change=add_to_done)
        act_tar.append(checkb)
        Text_f.value = ''
        page.update()
    
    
    # - Widgets
    header_txt = ft.Text('Gerenciador de Tarefas',size=20)
    header = ft.Container(
        content=ft.Row(
            [
            header_txt,
        ],
            alignment='center'
        )
    )
    
    btn_c_theme = ft.ElevatedButton('Mudar Tema',on_click=c_theme)
    add_button = ft.IconButton(icon=ft.icons.ADD,on_click=appeartf)
    cont_btn = ft.Row(
        [add_button],
        alignment='center'
    )
    
    Text_f = ft.TextField(label='Adicione a tarefa aqui',visible=False)
    btn_adc = ft.ElevatedButton('Adicionar',on_click=get_tar,visible=False)
    
    
    row_tf = ft.Row(
        [Text_f,
         btn_adc,
         cont_btn],
        alignment='center',
        wrap=True,
    )
    
    act_tar = []
    
    act_done = []
    
    cont_tar = ft.Container(
        content=ft.Row(
            act_tar,
            vertical_alignment='center',
        )
    )
    cont_to_done = ft.Container(
        content=ft.Column(
            act_done,
        )
    )
    
    div1 = ft.Divider(visible=False)
    div2 = ft.Divider(visible=False)
    
    
    rem_tar = ft.ElevatedButton('Remover ultima Tarefa salva',visible=False,on_click=remtar)
    cont_rem_tar = ft.Row(
        [rem_tar],
        alignment='center'
    )
    
    page.add(
        ft.Column(
            [
        header,
        btn_c_theme,
        div1,
        row_tf,
        cont_tar,
        div2,
        cont_rem_tar,
        ft.Divider(),
        cont_to_done,
            ]
        ),
    )
    
    
ft.app(target=main)