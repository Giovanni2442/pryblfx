from flet import * 
## AVERIGUAR COMO HACER EL MENU MODULAR ##


class cnpntHeader(UserControl):
    def __init__(self):
        super().__init__(expand=True) 

        self.color_teal = "teal"

        # Pestañas
        self.Pestañas = Tabs(
            label_color="red",
            indicator_color="Red",
            indicator_border_radius=60,
            divider_color="#fc4795",
            on_change=self.navTabs,
            tabs=[
                Tab(
                    text="FICHA / VENTAS"
                    #icon="home"
                ),
                Tab(
                    text="EXTRUSIÓN",
                    #icon="face"
                ),
                Tab(
                    text="IMPRESIÓN DIGITAL",
                    #icon="person"
                ),
                Tab(
                    text="LAMINADO",
                    #icon="person"
                ),
                Tab(
                    text="REFILADO",
                    #icon="person"
                ),
                Tab(
                    text="CONVERSION",
                    #icon="person"
                )
            ]
        )

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
                        #height=100,
                        bgcolor="green",
                        alignment=alignment.center,
                        content= Row(
                            alignment=MainAxisAlignment.SPACE_BETWEEN,
                            controls=[
                                Container(
                                    TextButton("INICIO",icon=icons.HOME),
                                    #bgcolor="RED",
                                ), 
                                Container(
                                    IconButton(icon=icons.ACCOUNT_CIRCLE,icon_color="violet"),
                                    #bgcolor="RED",
                                ),             
                            ]
                        )
                    ),
                    Container(      # Contenedor para las Pestañas
                        #height=100,
                        bgcolor="green",
                        content= Row(
                            alignment=MainAxisAlignment.CENTER,
                            controls=[
                                self.Pestañas # Añadir las pestañas
                            ]
                        )
                    )
                ]
            )
        )

######## FUNCIONES ##########

    def navTabs(self,e):
        id = e.control.selected_index
        #print(id)
        dic = [
            vtn1,
            vtn2,
            Container(
                bgcolor="red",
                width=100,
                height=100
            ),
            Container(
                bgcolor="blue",
                width=100,
                height=100
            ),
            Container(
                bgcolor="green",
                width=100,
                height=100
            ),
        ]

        return dic[id]