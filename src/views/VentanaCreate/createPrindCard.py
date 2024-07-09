from flet import *

class createPrind(UserControl):
    def __init__(self,page):
        super().__init__(expand=True)      # Clase de herencia que toma las caracteristicas del Frame

        self.color_teal = "teal"

        # Header
        self.cntHeader = Container(
            expand=True,
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
                    Container(        # --- Contenedor para las pestañas --
                        #expand=True,
                        height=150,
                        width=800,
                        bgcolor="yellow",
                        padding=10,
                        content= Container(
                            #alignment=MainAxisAlignment.CENTER,
                            bgcolor="red",
                            width=250,
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
                                    expand=0,
                                )
                        )                      
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
                    Container(      # --- Contenedor Ficha ---
                        expand=True,
                        bgcolor="green", 
                        margin=0,
                        padding=5,
                        content= Column(
                            controls=[
                                Container(    # Tamaño Ficha Tecnica
                                    Text("FICHA TECNICA",color="white"),
                                    alignment=alignment.center,
                                    bgcolor="blue",
                                ),
                                Container(
                                    alignment=alignment.center,
                                    content=Column(
                                        controls=[
                                            Text("Codigo del Producto"),
                                            TextField(
                                                label="Ingresar el PrindCard",
                                                border= InputBorder.OUTLINE,
                                                border_color="Black",
                                                label_style=TextStyle(color="Black",italic=True),
                                            ),
                                            Text("Cliente"),
                                            TextField(
                                                label="Ingresar el Cliente",
                                                border= InputBorder.OUTLINE,
                                                border_color="Black",
                                                label_style=TextStyle(color="Black",italic=True),
                                            ),
                                            Text("Fecha de Elavoración"),
                                            TextField(
                                                label="dd/MM/YYYY",
                                                border= InputBorder.OUTLINE,
                                                border_color="Black",
                                                label_style=TextStyle(color="Black",italic=True),
                                            ),
                                            Text("Fecha de Revición"),
                                            TextField(
                                                label="dd/MM/YYYY",
                                                border= InputBorder.OUTLINE,
                                                border_color="Black",
                                                label_style=TextStyle(color="Black",italic=True),
                                            ),
                                            Text("Nombre del Producto"),
                                            TextField(
                                                label="Ingrese el Nombre",
                                                border= InputBorder.OUTLINE,
                                                border_color="Black",
                                                label_style=TextStyle(color="Black",italic=True),
                                            ),
                                        ]
                                    ),
                                    
                                )
                            ],
                        )
                    ),
                    Container(      # --- Contenedor Ventas ---            
                        expand=True,
                        bgcolor="green",
                        margin=0,
                        padding=5,
                        content=Column(
                            controls=[
                                Container(    # Tamaño Ficha Tecnica
                                    Text("VENTAS",color="white"),
                                    alignment=alignment.center,
                                    bgcolor="blue",
                                ),
                                Container(
                                    content=Column(
                                            controls=[
                                                Text("Asesor Comercial de la Cuenta"),
                                                TextField(
                                                    label="Ingresar el Asesor",
                                                    border= InputBorder.OUTLINE,
                                                    border_color="Black",
                                                    label_style=TextStyle(color="Black",italic=True),
                                                ),
                                                Text("Tipo de Empaque"),
                                                TextField(
                                                    label="Ingresar el Tipo de Empaque",
                                                    border= InputBorder.OUTLINE,
                                                    border_color="Black",
                                                    label_style=TextStyle(color="Black",italic=True),
                                                ),
                                                Text("Producto Laminado"),
                                                Dropdown(
                                                    label="Laminado",
                                                    hint_text="Producto Laminado",
                                                    options=[
                                                        dropdown.Option("N/A"),
                                                        dropdown.Option("APLICA"),
                                                    ],
                                                    autofocus=True,
                                                    on_change= lambda e: print(e.control.value)  # Imprimir el resultado
                                                ),
                                                Text("Estructura del Producto"),
                                                TextField(
                                                    label="Ingresar la Estructura",
                                                    border= InputBorder.OUTLINE,
                                                    border_color="Black",
                                                    label_style=TextStyle(color="Black",italic=True),
                                                ),
                                                Text("Producto que se empaca"),
                                                TextField(
                                                    label="Ingrese el Empaque",
                                                    border= InputBorder.OUTLINE,
                                                    border_color="Black",
                                                    label_style=TextStyle(color="Black",italic=True),
                                            ),
                                        ]
                                    ),
                                )
                            ]
                        )
                    )
                ]
            )
        )  
        # Frame Main
        self.frameMain = Container(
            bgcolor="#737373",
            padding=2,
            content=Column(
                controls=[
                    self.cntHeader,
                    self.cntForm
                ]
            )
        )

    def jer(self,e):
        return e.contol.value

    def build(self):
        return self.frameMain

def main(page: Page):
    page.theme_mode = ThemeMode.DARK
    page.add(createPrind(page))
    #margin=margin.only(top=-5)

app(main)