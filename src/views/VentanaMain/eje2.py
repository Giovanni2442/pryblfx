
# NOTAS para MAÑANA: 
# * Acabar el Formulario de Extrución
# * Arreglar la parte de las Pestañas y redirecciónes
# * Hacer la conexión de los formularios a la base de datos (las 2 primeras tablas)
# * Agregar las validaciónes (Expreciones regulares a los inputs)



from flet import *
import flet as ft

class createPrind(UserControl):
    def __init__(self,page):
        super().__init__(expand=True)      # Clase de herencia que toma las caracteristicas del Frame

        self.color_teal = "teal"

        # Pestañas
        self.Pestañas = Tabs(
            label_color="red",
            indicator_color="Red",
            indicator_border_radius=60,
            divider_color="#fc4795",
            on_change=self.jiji,
            tabs=[
                Tab(
                    text="Tab 1",
                    icon="home"
                ),
                Tab(
                    text="Tab 2",
                    icon="face"
                ),
                Tab(
                    text="Tab 3",
                    icon="person"
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

#################### FORMULARIOS ########################################
       # FICHA / VENTAS
        self.cntForm = Container(
            expand=True,
            margin=margin.only(top=-5),
            bgcolor=self.color_teal,
            padding=5,
            content= Row(
                controls=[
                    Container(      # --- Contenedor Ficha ---
                        expand=True,
                        bgcolor="#5C516D", 
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
                        bgcolor="#5C516D",
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
                                                )
                                            ]
                                    ),
                                )
                            ]
                        )
                    )
                ]
            )
        )

        # EXTRUSIÓN
        self.cntForm2 = Container(
            expand=True,
            margin=margin.only(top=-5),
            bgcolor=self.color_teal,
            padding=5,
            content=
            Column([
                Container(    # Tamaño Ficha Tecnica
                    #expand=True,
                    Text("EXTRUSIÓN",color="white"),
                    alignment=alignment.center,
                    bgcolor="blue",
                ),
                Row(                    # --- Contenedor EXTRUSIÓN ---
                    expand=True,
                    controls=[
                    Container(                  # -- Seccion 1 --
                        expand=True,
                        bgcolor="blue", 
                        margin=0,
                        padding=15,
                        alignment=alignment.center,
                        content= Column(
                            expand=True,
                            scroll="auto",
                            controls=[
                                Container(
                                    alignment=alignment.center,
                                    content=Column(
                                        controls=[
                                            Text("Tipo de Material a Extruir"),
                                            TextField(
                                                label="Ingresar tipo de material",
                                                border= InputBorder.OUTLINE,
                                                border_color="Black",
                                                label_style=TextStyle(color="Black",italic=True),
                                            ),
                                            Text("Dinaje Requerido"),
                                            TextField(
                                                label="Ingresar el Dinaje",
                                                border= InputBorder.OUTLINE,
                                                border_color="Black",
                                                label_style=TextStyle(color="Black",italic=True),
                                            ),
                                            Text("Formula Extrusión"),
                                            TextField(
                                                label="Ingresar la Formula",
                                                border= InputBorder.OUTLINE,
                                                border_color="Black",
                                                label_style=TextStyle(color="Black",italic=True),
                                            ),
                                            Text("Pigmento de Pelicula"),
                                            TextField(
                                                 label="Ingresar el Pigmento",
                                                border= InputBorder.OUTLINE,
                                                border_color="Black",
                                                label_style=TextStyle(color="Black",italic=True),
                                            ),
                                            #DropBox de Inpits
                                            Container(
                                                #Text("Ingresar !"),
                                                bgcolor="green",
                                                border_radius=5,
                                                padding=5,
                                                content= PopupMenuButton(
                                                    Text("Ingresar!"),
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
                                            ),
                                            Text("Tipo de Bobina"),
                                            Dropdown(
                                                label="Laminado",
                                                hint_text="Producto Laminado",
                                                options=[
                                                    dropdown.Option("N/A"),
                                                    dropdown.Option("Lamina"),
                                                    dropdown.Option("Tabular Abierta"),
                                                ],
                                                autofocus=True,
                                                on_change= lambda e: print(e.control.value)  # Imprimir el resultado
                                            ),
                                        ]
                                    ),
                                    
                                )
                                
                            ]
                        )
                    ),
                    Container(                  # -- Seccion 2 --
                        expand=True,
                        bgcolor="blue", 
                        margin=0,
                        padding=15,
                        alignment=alignment.center,
                        content= Column(
                            expand=True,
                            scroll="auto",
                            controls=[
                                Container(         
                                    #alignment=alignment.center,
                                    content=Column(
                                        controls=[
                                            Text("Tipó de Tratado"),
                                            Dropdown(
                                                label="Laminado",
                                                hint_text="Producto Laminado",
                                                options=[
                                                    dropdown.Option("N/A"),
                                                    dropdown.Option("Seccionado"),
                                                    dropdown.Option("Una cara"),
                                                    dropdown.Option("Ambas caras"),
                                                    dropdown.Option("Sin tratado"),
                                                ],
                                                autofocus=True,
                                                on_change= lambda e: print(e.control.value)  # Imprimir el resultado
                                            ),
                                            #DropBox de Inputs
                                            Container(
                                                #Text("Ingresar !"),
                                                bgcolor="green",
                                                alignment=alignment.center,
                                                border_radius=5,
                                                padding=5,
                                                content= PopupMenuButton(
                                                    Text("Ancho de Bobina y Tolerancia!"),
                                                    bgcolor="white",
                                                    menu_position=PopupMenuPosition.OVER,
                                                    items=[ 
                                                        PopupMenuItem(
                                                            content= Column(width=200,controls=[
                                                                Text("Ancho de bobina"),
                                                                TextField(
                                                                    label="N/A",
                                                                    border= InputBorder.OUTLINE,
                                                                    #width=100,
                                                                    border_color="black",
                                                                    label_style=TextStyle(color="black",italic=True),
                                                                )
                                                            ])
                                                        ),
                                                        PopupMenuItem(
                                                            content= Column([
                                                                Text("Tolerancia"),
                                                                TextField(
                                                                    label="N/A",
                                                                    border= InputBorder.OUTLINE,
                                                                    border_color="Black",
                                                                    label_style=TextStyle(color="Black",italic=True),
                                                                )
                                                            ])
                                                        ),
                                                    ]
                                                )
                                            ),
                                            #DropBox de Inputs
                                            Container(
                                                #Text("Ingresar !"),
                                                bgcolor="green",
                                                alignment=alignment.center,
                                                border_radius=5,
                                                padding=5,
                                                content= PopupMenuButton(
                                                    Text("Ancho de Core y Tolerancia"),
                                                    bgcolor="white",
                                                    menu_position=PopupMenuPosition.OVER,
                                                    items=[ 
                                                        PopupMenuItem(
                                                            content= Column(width=200,controls=[
                                                                Text("Ancho de Core"),
                                                                TextField(
                                                                    label="N/A",
                                                                    border= InputBorder.OUTLINE,
                                                                    #width=100,
                                                                    border_color="black",
                                                                    label_style=TextStyle(color="black",italic=True),
                                                                )
                                                            ])
                                                        ),
                                                        PopupMenuItem(
                                                            content= Column([
                                                                Text("Tolerancia"),
                                                                TextField(
                                                                    label="N/A",
                                                                    border= InputBorder.OUTLINE,
                                                                    border_color="Black",
                                                                    label_style=TextStyle(color="Black",italic=True),
                                                                )
                                                            ])
                                                        ),
                                                    ]
                                                )
                                            ),
                                            #DropBox de Inputs
                                            Container(
                                                #Text("Ingresar !"),
                                                bgcolor="green",
                                                alignment=alignment.center,
                                                border_radius=5,
                                                padding=5,
                                                content= PopupMenuButton(
                                                    Text("Diametro de Bobina y Tolerancia"),
                                                    bgcolor="white",
                                                    menu_position=PopupMenuPosition.OVER,
                                                    items=[ 
                                                        PopupMenuItem(
                                                            content= Column(width=200,controls=[
                                                                Text("Diametro de Bobina"),
                                                                TextField(
                                                                    label="N/A",
                                                                    border= InputBorder.OUTLINE,
                                                                    #width=100,
                                                                    border_color="black",
                                                                    label_style=TextStyle(color="black",italic=True),
                                                                )
                                                            ])
                                                        ),
                                                        PopupMenuItem(
                                                            content= Column([
                                                                Text("Tolerancia"),
                                                                TextField(
                                                                    label="N/A",
                                                                    border= InputBorder.OUTLINE,
                                                                    border_color="Black",
                                                                    label_style=TextStyle(color="Black",italic=True),
                                                                )
                                                            ])
                                                        ),
                                                    ]
                                                )
                                            )
                                        ]
                                    ),
                                    
                                )
                                
                            ]
                        )
                    ),
                    Container(                  # -- Seccion 3 --     
                        expand=True,
                        bgcolor="blue", 
                        margin=0,
                        padding=15,
                        alignment=alignment.center,
                        content= Column(
                            expand=True,
                            scroll="auto",
                            controls=[
                                Container(
                                    alignment=alignment.center,
                                    content=Column(
                                        controls=[
                                            Text("Maximo de Empalmes por Bobina"),
                                            TextField(
                                                label="N/A",
                                                border= InputBorder.OUTLINE,
                                                border_color="Black",
                                                label_style=TextStyle(color="Black",italic=True),
                                            ),
                                            Text("Dinaje Requerido"),
                                            TextField(
                                                label="Ingresar el Dinaje",
                                                border= InputBorder.OUTLINE,
                                                border_color="Black",
                                                label_style=TextStyle(color="Black",italic=True),
                                            ),
                                            Text("Formula Extrusión"),
                                            TextField(
                                                label="Ingresar la Formula",
                                                border= InputBorder.OUTLINE,
                                                border_color="Black",
                                                label_style=TextStyle(color="Black",italic=True),
                                            ),
                                            Text("Pigmento de Pelicula"),
                                            TextField(
                                                 label="Ingresar el Pigmento",
                                                border= InputBorder.OUTLINE,
                                                border_color="Black",
                                                label_style=TextStyle(color="Black",italic=True),
                                            ),
                                            #DropBox de Inpits
                                            Container(
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
                                            ),
                                            Text("Tipo de Bobina"),
                                            Dropdown(
                                                label="Laminado",
                                                hint_text="Producto Laminado",
                                                options=[
                                                    dropdown.Option("N/A"),
                                                    dropdown.Option("Lamina"),
                                                    dropdown.Option("Tabular"),
                                                ],
                                                autofocus=True,
                                                on_change= lambda e: print(e.control.value)  # Imprimir el resultado
                                            ),
                                        ]
                                    ),
                                    
                                )
                                
                            ]
                        )
                    ),
                    Container(             # -- Seccion 3 --   
                        expand=True,
                        bgcolor="blue", 
                        margin=0,
                        padding=15,
                        alignment=alignment.center,
                        content= Column(
                            expand=True,
                            scroll="auto",
                            controls=[
                                Container(
                                    alignment=alignment.center,
                                    content=Column(
                                        controls=[
                                            Text("Tipo de Material a Extruir"),
                                            TextField(
                                                label="Ingresar tipo de material",
                                                border= InputBorder.OUTLINE,
                                                border_color="Black",
                                                label_style=TextStyle(color="Black",italic=True),
                                            ),
                                            Text("Dinaje Requerido"),
                                            TextField(
                                                label="Ingresar el Dinaje",
                                                border= InputBorder.OUTLINE,
                                                border_color="Black",
                                                label_style=TextStyle(color="Black",italic=True),
                                            ),
                                            Text("Formula Extrusión"),
                                            TextField(
                                                label="Ingresar la Formula",
                                                border= InputBorder.OUTLINE,
                                                border_color="Black",
                                                label_style=TextStyle(color="Black",italic=True),
                                            ),
                                            Text("Pigmento de Pelicula"),
                                            TextField(
                                                 label="Ingresar el Pigmento",
                                                border= InputBorder.OUTLINE,
                                                border_color="Black",
                                                label_style=TextStyle(color="Black",italic=True),
                                            ),
                                            #DropBox de Inpits
                                            Container(
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
                                            ),
                                            Text("Tipo de Bobina"),
                                            Dropdown(
                                                label="Laminado",
                                                hint_text="Producto Laminado",
                                                options=[
                                                    dropdown.Option("N/A"),
                                                    dropdown.Option("Lamina"),
                                                    dropdown.Option("Tabular"),
                                                ],
                                                autofocus=True,
                                                on_change= lambda e: print(e.control.value)  # Imprimir el resultado
                                            ),
                                        ]
                                    ),
                                    
                                )
                                
                            ]
                        )
                    )
                ])
            ])       
        )
        


########################################################################

        # Frame Main
        self.frameMain = Container(
            bgcolor="#737373",
            padding=2,
            content=Column(
                controls=[
                    self.cntHeader,
                    #self.cntForm       # Contenedor de FICHA / VENTAS como Inicio
                    self.cntForm2
                    #self.pru()
                ]
            )
        )


#################### PRUEBA #######################
    def jiji(self,e):
        id = e.control.selected_index
        #print(id)
        dic = [
            self.cntForm,
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

        self.frameMain.content.controls = [self.cntHeader]
        self.frameMain.content.controls.append(dic[id])
        self.update()


    def build(self):
        return self.frameMain

def main(page: Page):
    page.theme_mode = ThemeMode.DARK
    page.add(createPrind(page))
    #margin=margin.only(top=-5)

app(main)