from flet import *

class windowPru(UserControl):
    def __init__(self,page):
        super().__init__(expand=True) 

        self.main = Container(
            bgcolor="green",
            width=500,
            height=500,
            content= Text("Ejemplo")
        )

    def build(self):
        return self.main
    
def main(page: Page):
    page.theme_mode = ThemeMode.LIGHT
    page.padding = 0
    page.add(windowPru(page))
    
#app(main)