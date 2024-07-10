from flet import *

class createPrind(UserControl):
    def __init__(self,page):
        super().__init__(expand=True)      # Clase de herencia que toma las caracteristicas del Frame

        self.je = Container(
            #expand=True,
            bgcolor="red",
            #width=500,
            #height=500,
            content= Row(
                alignment=MainAxisAlignment.CENTER,
                controls=[
                Tabs(
                    on_change=self.track,
                    tabs=[
                        Tab(icon=icons.HOME),
                        Tab(icon=icons.HOME),
                        Tab(icon=icons.HOME)
                    ]
                )
                ]
            )
        )

        self.cntAdd = Container(
             bgcolor="red",
             expand=True,
             #width=500,
             #height=500,
        )
        self.cntAdd2 = Container(
            #Text("Ingresar !"),
             bgcolor="blue",
             border_radius=5,
             padding=5,
             content= PopupMenuButton(
                #Text("Ingresar!",icon=icons.DOWNLOAD_DONE),
                bgcolor="white",
                menu_position=PopupMenuPosition.OVER,
                items=[ 
                     PopupMenuItem(
                         content= Column(width=200,controls=[
                            Text("Ingresar!"),
                            TextField(
                                label="Ingresar la Estructura",
                                border= InputBorder.OUTLINE,
                                #width=100,
                                border_color="black",
                                label_style=TextStyle(color="black",italic=True),
                            )
                         ])
                     ),
                     PopupMenuItem(
                         content= Column([
                            Text("Ingresar!"),
                            TextField(
                                label="Ingresar la Estructura",
                                border= InputBorder.OUTLINE,
                                border_color="Black",
                                label_style=TextStyle(color="Black",italic=True),
                            )
                         ])
                     ),
                 ]
             )
             #width=500,
             #height=500,
        )
        self.cntAdd3 = Container(
             bgcolor="green",
             expand=True,
             #width=500,
             #height=500,
        )

        # Frame Main
        self.frameMain = Container(
            expand=True,
            bgcolor="#737373",
            padding=2,
            content=Column(
                controls=[
                    self.je
                ]
            )
        )
    

    def track(self,e):
        id = e.control.selected_index 
        print(id)
        dir = [
            self.cntAdd,
            self.cntAdd2,
            self.cntAdd3
        ]
        self.frameMain.content.controls = [self.je]
        self.frameMain.content.controls.append(dir[id])
        self.update()

    def build(self):
        return self.frameMain

def main(page: Page):
    page.theme_mode = ThemeMode.DARK
    page.add(createPrind(page))
    #margin=margin.only(top=-5)

app(main)