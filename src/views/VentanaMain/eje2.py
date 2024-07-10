from flet import *

import flet as ft
from flet import UserControl, Tabs, Tab, Container, BoxShadow, LinearGradient, alignment, Column, Row, IconButton, Text, margin, MainAxisAlignment, Page, ThemeMode

class Menu(UserControl):
    def __init__(self, page):
        super().__init__()
        self.page = page


        # TABS
        self.mytab = Tabs(
            selected_index=0,
            label_color="white",
            indicator_color="Red",
            indicator_border_radius=30,
            divider_color="#fc4795",
            scrollable=True,
            on_change=self.changeSelect,
            tabs=[
                Tab(
                    text="Home",
                    icon="home"
                ),
                Tab(
                    text="Face",
                    icon="face"
                ),
                Tab(
                    text="Person",
                    icon="person"
                ),
                Tab(
                    text="Notifications",
                    icon="notifications"
                ),
            ]
        )

        self.mybar = Container(
            border_radius=ft.border_radius.vertical(
                bottom=30
            ),
            shadow=BoxShadow(
                spread_radius=1,
                blur_radius=10,
                color="#fc4795",
                ),
                gradient=LinearGradient(
                    begin=alignment.top_left,
                    end=alignment.bottom_right,
                    colors=["#fc4795", "#7c59f0"]
                ),
                width=self.page.window_width,
                height=150,
                padding=20,  # Cambio el padding para que se ajuste mejor
                content=Column(
                    controls=[
                        Row(
                            alignment=MainAxisAlignment.SPACE_BETWEEN,
                            controls=[
                                IconButton(icon="menu", icon_color="white"),
                                Text("panch0", color="white"),
                                Row(
                                    controls=[
                                        IconButton(icon="menu", icon_color="white"),
                                        IconButton(icon="notifications", icon_color="white"),
                                        IconButton(icon="search", icon_color="white"),
                                    ]
                                )
                            ],
                        ),
                        Container(
                            bgcolor="red",
                            #alignment=MainAxisAlignment.SPACE_BETWEEN,
                            content=
                                Row(
                                alignment=MainAxisAlignment.SPACE_AROUND,
                                controls=[
                                    self.mytab
                                ]
                        )
                        ),
                        
                    ]
                ),
        )

        self.cnt1 = Column(
            controls=[
                Container(
                    margin=margin.only(top=self.page.window_height/2),
                    alignment=alignment.center,
                    content=Column(
                        controls=[
                            Text("Sample", size=30)
                        ]
                    )
                )
            ]
        )

        self.frameMain = Column(
            controls=[
                self.mybar,
                self.cnt1,
            ]
        )
    
    def changeSelect(self,e):
        id = e.control.selected_index
        nameScreen = e.control.tabs[id].text
        #print(id,nameScreen)
        #print(e.control.tabs)
        for x in range(0,len(e.control.tabs)):
            if id == x:
                self.page.controls[0].controls[0].content.controls[0].value = nameScreen
        self.page.update()

    def sal(self,e):
        print(e.control.value)

    def build(self):
        return self.frameMain

def main(page: Page):
    page.theme_mode = ThemeMode.DARK
    page.add(Menu(page))

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