from flet import *

import flet as ft

def main(page: Page):

    eje = Container(        # --- Contenedor para las pestañas --
        expand=True,
        #height=150,
        width=2000,
        bgcolor="yellow",
        padding=10,
        content= Container(
            #alignment=MainAxisAlignment.CENTER,
            bgcolor="red",
            width=150,
            content=
                Tabs(
                    selected_index=0,
                    #tab_alignment=alignment.center,
                    animation_duration=300,
                    width=100,
                    #expand=False,
                    #alignment=MainAxisAlignment.SPACE_BETWEEN,
                    tabs=[ 
                        Tab(
                            text="Tab 1",
                            content=Container(
                                content=Text("This is Tab 1"), alignment=alignment.center
                            ),
                        ),
                        Tab(
                            tab_content=Icon(icons.SEARCH),
                            content=Text("This is Tab 2"),
                        ),
                        Tab(
                            text="Tab 3",
                            icon=icons.SETTINGS,
                            content=Text("This is Tab 3"),
                        ),
                    ],
                    expand=True,
                )
        )                      
    )
    
    page.add(eje)

app(target=main)

'''
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

def main(page: Page):
    page.theme_mode = ThemeMode.DARK
    page.add(ejemplo2(page))

# Main
app(main)'''