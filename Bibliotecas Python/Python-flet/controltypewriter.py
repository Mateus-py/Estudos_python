import flet as ft
from time import sleep

class TypeWriterControl(ft.UserControl):
    def __init__(self,value='',font_family='SpaceGrotesk',color='#ffffff',transparency=True):
        super().__init__()
        self.text_to_print = value
        self.font_family = font_family
        self.color = color
        self.transparency = transparency
        
        
        
    def did_mount(self):
        self.effect()
        
    def update(self):
        super().update()
        self.effect()
        
        
    def effect(self):
        self.Type_writer.value = ''
        for letter in range(len(self.text_to_print)):
            self.Type_writer.value += self.Type_writer[letter] + '_'
            self.Type_writer.font_family = self.font_family
            self.Type_writer.color = self.color
            self.Type_writer.opacity = 1 if self.transparency == True else 0
            self.Type_writer.update()
            self.Type_writer.value = self.Type_writer.value[:-1]
            sleep(0.02)
        self.Type_writer.update()
            
            

    def build(self):
        self.Type_writer = ft.Text('',no_wrap=False)
        return self.Type_writer