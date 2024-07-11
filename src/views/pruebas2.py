from flet import *

class mqtrImprDig(UserControl):
    def __init__(self,page):
        super().__init__(expand=True)

        # Contenedor Header
        self.cntHeader = Container(
            #expand=True,
            padding=10,
            bgcolor="blue",
            content= Column(
                controls=[
                    # Encabezado 1
                    Container(
                        #expand=True,
                        bgcolor="yellow",
                        #width=100,
                        height=30,
                        content= Row(
                            alignment=MainAxisAlignment.SPACE_BETWEEN,
                            controls=[
                                Container( TextButton(icon=icons.HOME)),
                                Container( TextButton(icon=icons.ACCOUNT_CIRCLE)),
                                Container( TextButton(icon=icons.ACCOUNT_CIRCLE))
                            ]
                        )
                    ),
                    # Encabezado 2
                    Container(
                        #expand=True,
                        bgcolor="yellow",
                        #width=100,
                        #height=30,
                        content=
                            Row(
                               alignment=MainAxisAlignment.CENTER,
                                controls=[
                                    Tabs(
                                        tabs=[
                                            Tab(icon=icons.HOME),
                                            Tab(icon=icons.ACCESS_ALARM_OUTLINED),
                                            Tab(icon=icons.UPLOAD_SHARP)
                                
                                        ]
                                    ),
                                ]
                            ) 
                    )
                ]
            )
        )

        # Contenedor Formulario
        self.cntForm = Container(
            expand=True,
            bgcolor="red",
            padding=10,
            content=Column(
                controls=[
                    # Encabezado / Titulo
                    Container(
                        bgcolor="yellow",
                        height=30
                    ),
                    # Formulario
                    Container(
                        expand=True,
                        bgcolor="yellow",
                        #height=30
                    )
                ]
            )
        )

        # Contener Principal
        self.cuadro1 = Container(
            padding=10,
            expand=True,
            bgcolor="green",
            content= Column(
                controls=[
                    self.cntHeader,
                    self.cntForm
                ]
            )
            #width=200,
            #height=200
        )


    def build(self):
        return self.cuadro1

    
def main(page: Page):
    #page.theme_mode = ThemeMode.DARK
    page.add(mqtrImprDig(page))

app(main)