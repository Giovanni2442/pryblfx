from flet import *

class ejemplo2(UserControl):
    def __init__(self,page):
        super().__init__()

        self.page = page

        self.frame1 = Container(
            bgcolor="red",
            width=150,
            height=150,
            padding=5,
            margin=0,
            alignment=alignment.center,
            content= Column(
                controls=[
                    Text("Este es el ejemplo 2"),
                    Text("Este es el ejemplo 2"),
                    Text("Este es el ejemplo 2"),
                ],
            )
        )

        self.frame2 = Container(
            bgcolor="blue",
            width=150,
            height=150,
            padding=10,
            margin=0,
            alignment=alignment.center,
            content= Column(
                controls=[
                    Text("Este es el ejemplo 2"),
                    Text("Este es el ejemplo 2"),
                    Text("Este es el ejemplo 2"),
                ],
            )
        )

        self.cntBtn = Container(
            bgcolor="green",
            #width=150,
            #height=150,
            padding=10,
            margin=0,
            alignment=alignment.center,
            content=Column(
                controls=[
                    #Text(),
                    TextButton("Press Here!",
                        icon=icons.PLAY_CIRCLE_FILL_OUTLINED,
                        on_click= lambda _: self.page.go('/'))
                ]
                    
            )
        )

    # Colocar los frames en forma de columna
        self.frameMain = Container(
            bgcolor="yellow",
            border_radius=10,
            padding=10,
            content=Column(
                    alignment=alignment.center,
                    expand=False,
                    controls=[
                        self.frame1,
                        self.frame2,
                        self.cntBtn 
                    ],
                ),
        )


   # Construye todos los frames tiene el frame Main
    def build(self):
        return self.frameMain

'''
def main(page: Page):
    page.theme_mode = ThemeMode.DARK
    page.add(ejemplo2(page))

# Main
app(main)'''