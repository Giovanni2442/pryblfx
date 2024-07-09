from flet import *

import flet as ft

def main(page: ft.Page):
    t = ft.Tabs(
        selected_index=1,
        animation_duration=300,
        tabs=[
            ft.Tab(
                text="Tab 1",
                content=ft.Container(
                    content=ft.Text("This is Tab 1"), alignment=ft.alignment.center
                ),
            ),
            ft.Tab(
                tab_content=ft.Icon(ft.icons.SEARCH),
                content=ft.Text("This is Tab 2"),
            ),
            ft.Tab(
                text="Tab 3",
                icon=ft.icons.SETTINGS,
                content=ft.Text("This is Tab 3"),
            ),
        ],
        expand=1,
    )

    # Crear un Row para centrar los tabs
    centered_tabs = ft.Row(
        controls=[t],
        alignment=ft.MainAxisAlignment.CENTER,  # Centrar los tabs
    )

    page.add(centered_tabs)

ft.app(target=main)


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