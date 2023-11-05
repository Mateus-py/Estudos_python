import flet as ft
import openai


openai.api_key = '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'

class StandardPT():
    def __init__(self,Text_to_convert):
        self.Text_to_convert = Text_to_convert
        
    def convertStandartportugues(self):
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt= f"Corrija Essa Gramatica para norma padrao:\n\n{self.Text_to_convert}",
            temperature=0,
            max_tokens=60,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0
    )
        
        result = {
        'id' : response.id,
        'created' : response.created,
        'model' : response.model,
        'completion_tokens' : response.usage.completion_tokens,
        'prompt_tokens' : response.usage.prompt_tokens,
        'total_tokens' : response.usage.total_tokens,
        'output' : response.choices[0].text,
        'status' : response.choices[0].finish_reason,
    }
        return result['output']

def main(page: ft.Page):
    page.title = 'Gramaticando'
    page.horizontal_alignment = 'center'
    page.theme_mode = 'dark'
    
    logo = ft.Image(src=f'imgs/img1.png',width=300,border_radius=20)
    user_input = ft.TextField(hint_text='Escreva Qualquer coisa...',border_radius=30)
    outputText = ft.Text('A resposta aparecera aqui...')
    
    
    def print_result(e):
        answer = StandardPT(str(user_input.value)).convertStandartportugues()
        outputText.value = answer[2:]
        page.update()
    
    output_cont = ft.Container(
        content=outputText,
        margin=20,
        padding=20,
        bgcolor=ft.colors.AMBER_500,
        border_radius=20,
    )
    
    
    page.add(
        logo,
        user_input,
        ft.ElevatedButton('Procurar',on_click=print_result),
        output_cont,
    )

ft.app(target=main,assets_dir='assets')