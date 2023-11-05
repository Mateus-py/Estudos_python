import flet as ft
import time,threading

'''
Theory - User Control Provendo Life-cycle hook methods

1) did_mount() : Chamado apos o UserControl adicionar a pagina
2) will_unmount() : Chamado apos o UserControl e removido da pagina
'''

'''
Theory - Daemon

1) Em multask em computador OS, um daemon e um programa de computador que roda como processo de background

'''

class Timer(ft.UserControl):
    def __init__(self,seconds):
        super().__init__()
        self.seconds = seconds
    
    def did_mount(self):
        self.running = True
        self.Mythread = threading.Thread(target=self.update_timer,args=(),daemon=True)
        self.Mythread.start()
        
    def will_unmount(self):
        self.running = False   
        
    def update_timer(self):
        while self.seconds and self.running:
            mins,secs = divmod(self.seconds,60)
            self.conter.value = '{:02d}:{:02d}'.format(mins,secs)
            self.update()
            time.sleep(1)
            self.seconds -= 1
            
    def build(self):
        self.conter = ft.Text()
        return self.conter

def main(page: ft.Page):
    page.title = 'My timer App'
    page.window_height = 200
    page.window_width = 100
    page.add(
        Timer(100),
        Timer(69)
    )
ft.app(target=main)