from flet import *

class createPrind(UserControl):
    def __init__(self,page):
        super().__init__(expand=True)      # Clase de herencia que toma las caracteristicas del Frame

        self.color_teal = "teal"

        # Header
        self.cntHeader = Container(
            #expand=True,
            bgcolor=self.color_teal,
            #height=80,
            padding=5,
            content= Column(
                controls=[
                    Container(      #-- Contenedor de Inicio y Usuario --
                        #expand=True,
                        height=20,
                        bgcolor="green", 
                        margin=0,
                    ),
                    Container(        # --- Contenedor para las pestañas --
                        #expand=True,
                        height=50,
                        bgcolor="green",
                        margin=0,
                    )
                ]
            )
        )   

       # Contenido de la tabla 
        self.cntForm = Container(
            expand=True,
             margin=margin.only(top=-5),
            bgcolor=self.color_teal,
            padding=5,
            content= Row(
                controls=[
                    Container(      #-- Contenedor Ficha
                        expand=True,
                        bgcolor="green", 
                        margin=0,
                        content= Column(
                            controls=[
                                Container(    
                                    Text("Ficha Tecnica",color="white"),
                                    alignment=alignment.center,
                                    bgcolor="blue",
                                ),
                            ],
                        )
                    ),
                    Container(      
                        expand=True,
                        bgcolor="green",
                        margin=0,
                    )
                ]
            )
        )  
        # Frame Main
        self.frameMain = Container(
            bgcolor="yellow",
            padding=2,
            content=Column(
                controls=[
                    self.cntHeader,
                    self.cntForm
                ]
            )
        )

    def build(self):
        return self.frameMain

def main(page: Page):
    page.theme_mode = ThemeMode.DARK
    page.add(createPrind(page))
    page.padding = 0

app(main)