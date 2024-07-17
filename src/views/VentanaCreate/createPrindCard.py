from flet import *
from src.app.filExcel.filtroExcel import filter
from src.views.VentanaCreate.InptFich_Vents import InptsTable

#Notas : para el usuario se puede agregar cerrar su seción, ver su historial de modificaciónes etc..

# Librerias de Prueba con los inputs 
from src.views.VentanaCreate.InptsForm.Inpts_FichaTecVentas import Inpts_FichaTec_Ventas
from src.views.VentanaCreate.InptsForm.Inpts_Extrc import InptsExtrc


class createPrind(UserControl):
    def __init__(self,page):
        super().__init__(expand=True)      # Clase de herencia que toma las caracteristicas del Frame

        self.color_teal = "teal"
        self.page = page

        self.ele = InptsTable(page)
   
        # Inputs FichaTecnica
        self.Inpts = Inpts_FichaTec_Ventas(page)
        # Inputs Extrusión
        self.InptsExtrc = InptsExtrc(page)

        # btn Agregar
        self.btn = FilledButton(
                    text="ADD",
                    adaptive=True,
                    style=ButtonStyle(
                        bgcolor="#21A742",
                        color={
                            ControlState.HOVERED: colors.RED,
                            ControlState.HOVERED: colors.BLACK,
                        },
                        overlay_color=colors.TRANSPARENT,
                        elevation={"pressed": 0, "": 1},
                        animation_duration=200,
                        shape={
                            ControlState.HOVERED: RoundedRectangleBorder(radius=15),
                            ControlState.DEFAULT: RoundedRectangleBorder(radius=3),
                        },
                    ),
                    #on_click= lambda e: self.Inpts.clean_fields(e), 
                    on_click= self.upd
        )

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
                                    TextButton("INICIO",
                                               icon=icons.HOME,
                                               on_click=  lambda _: self.page.go('/')),
                                    #bgcolor="RED",
                                ), 
                                Container(
                                    IconButton(icon=icons.ACCOUNT_CIRCLE,
                                               icon_color="violet",
                                               on_click=  lambda _: self.page.go('/')), #Agregar el registro de usuarios
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
        self.vtnFicha_Ventas = Container(
            expand=True,
            margin=margin.only(top=-5),
            bgcolor=self.color_teal,
            padding=5,
            content=
            Column([
                Container(
                    bgcolor=self.color_teal,
                    content=
                        Row([       # --- ENCABEZADOS DE LAS TABLAS --- #
                            Container(    # Tamaño Ficha Tecnica
                                Text("FICHA TECNICA",color="white"),
                                expand=True,
                                alignment=alignment.center,
                                bgcolor="#858585",
                            ),
                            Container(    # Tamaño Ficha Tecnica
                                Text("VENTAS",color="white"),
                                expand=True,
                                alignment=alignment.center,
                                bgcolor="#858585",
                            ),
                        ])
                ),
                Row(                    # --- TABLAS FICHA / VENTAS ---
                    expand=True,
                    controls=[
                        Container(                  # -- Seccion 1 Ficha Tecnica--
                            expand=True,
                            bgcolor="#858585", 
                            margin=0,
                            padding=15,
                            alignment=alignment.center,
                            content= Column(
                                expand=True,
                                scroll="auto",
                                controls=[
                                    Container(      # FORMULARIO
                                        alignment=alignment.center,
                                        content=Column(
                                            controls=[
                                                Text("Codigo del Producto"),
                                                self.Inpts.id_product,

                                                Text("Cliente"),
                                                self.Inpts.cliente,

                                                Text("Fecha de Elavoración"),
                                                self.Inpts.fecha_Elav,

                                                Text("Fecha de Revición"),
                                                self.Inpts.fecha_Rev,

                                                Text("Nombre del Producto"),
                                                self.Inpts.producto,
                                            ]
                                        ),  
                                    )
                                ]
                            )
                        ),
                        Container(                  # -- Seccion 2 VENTAS --     
                            expand=True,
                            bgcolor="#858585", 
                            margin=0,
                            padding=15,
                            alignment=alignment.center,
                            content= Column(    # Formulario
                                expand=True,
                                scroll="auto",
                                controls=[
                                    Container(
                                        content=Column(
                                                scroll="auto",
                                                controls=[
                                                    Text("Asesor Comercial de la Cuenta"),
                                                    self.Inpts.AsesorCmrcl,

                                                    Text("Tipo de Empaque"),
                                                    self.Inpts.TipEmpq,

                                                    Text("Producto Laminado"),
                                                    self.Inpts.prdcLam,

                                                    Text("Estructura del Producto"),
                                                    self.Inpts.EstrcPrdct,

                                                    Text("Producto que se empaca"),
                                                    self.Inpts.PrdctEmpq
                                                ]
                                            ),
                                        )
                                    ]
                                )
                            )
                        ])
                    ])       
        )
    
        # EXTRUSIÓN
        self.vtnExtr = Container(
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
                    bgcolor="#858585",
                ),
                Row(                    # --- Contenedor EXTRUSIÓN ---
                    expand=True,
                    controls=[
                    Container(                  # -- Seccion 1 --
                        expand=True,
                        bgcolor="#858585", 
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
                                            self.InptsExtrc.tipMtrlExtr,

                                            Text("Dinaje Requerido"),
                                            self.InptsExtrc.dinajeReq,

                                            Text("Formula Extrusión"),
                                            self.InptsExtrc.frmlExtr,

                                            Text("Pigmento de Pelicula"),
                                            self.InptsExtrc.pigmPelc,
                                            
                                            Text("Tipo de Bobina"),
                                            self.InptsExtrc.tipBob,

                                            Text("Tipó de Tratado"),
                                            self.InptsExtrc.tipTratado,
                                        ]
                                    ),
                                    
                                )
                                
                            ]
                        )
                    ),
                    Container(                  # -- Seccion 2 --     
                        expand=True,
                        bgcolor="#858585", 
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
                                            #DropBox de Inputs
                                            Container(
                                                #Text("Ingresar !"),
                                                bgcolor="#B6DE3A",
                                                alignment=alignment.center,
                                                border_radius=5,
                                                padding=5,
                                                content= self.InptsExtrc.anchBob_Tol
                                            ),
                                            #DropBox de Inputs
                                            Container(
                                                #Text("Ingresar !"),
                                                bgcolor="#B6DE3A",
                                                alignment=alignment.center,
                                                border_radius=5,
                                                padding=5,
                                                content= self.InptsExtrc.anchCore_Tol
                                            ),

                                            Text("Maximo de Empalmes por Bobina"),
                                            self.InptsExtrc.maxEmplBob,

                                            Text("Orientación de Bobina en Tarima"),
                                            self.InptsExtrc.orntBobTam,

                                            Text("Tipó de Empaque para Bonina"),
                                            self.InptsExtrc.tipEmpqBob,

                                            Text("Pesar producto Por"),
                                            self.InptsExtrc.psrPrdct,

                                            #DropBox de Inputs
                                            Container(
                                                #Text("Ingresar !"),
                                                bgcolor="#B6DE3A",
                                                alignment=alignment.center,
                                                border_radius=5,
                                                padding=5,
                                                content= self.InptsExtrc.psPromBob
                                            ),
                                        ]
                                    ),
                                    
                                )
                                
                            ]
                        )
                    ),
                    Container(                  # -- Seccion 3 --   
                        expand=True,
                        bgcolor="#858585", 
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
                                            #DropBox de Inputs
                                            Container(
                                                #Text("Ingresar !"),
                                                bgcolor="#B6DE3A",
                                                alignment=alignment.center,
                                                border_radius=5,
                                                padding=5,
                                                content= self.InptsExtrc.DimBob_Tol
                                            ),

                                            Text("Etiquetado"),
                                            self.InptsExtrc.etiquetado,

                                            #DropBox de Inputs
                                            Container(
                                                bgcolor="#B6DE3A",
                                                alignment=alignment.center,
                                                border_radius=5,
                                                padding=5,
                                                content= self.InptsExtrc.numBobCma_CmaTrm
                                            ),

                                            Text("Numero de Bobinas en Tarima"),
                                            self.InptsExtrc.numBobTam,
                                            #DropBox de Inputs
                                            Container(
                                                #Text("Ingresar !"),
                                                bgcolor="#B6DE3A",
                                                alignment=alignment.center,
                                                border_radius=5,
                                                padding=5,
                                                content= self.InptsExtrc.psNtPromTam
                                            ),

                                            Text("La tarima llevara emplaye"),
                                            self.InptsExtrc.tamEmplaye,

                                            Text("La tarima sera refilada"),
                                            self.InptsExtrc.tamRefila,
                                        ]
                                    ),
                                    
                                )
                                
                            ]
                        )
                    )
                ])
            ])       
        )
    
        # IMPRECIÓN DIGITAL
        self.vtnImprDigtl = Container(
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
                    bgcolor="#858585",
                ),
                Row(                    # --- Contenedor EXTRUSIÓN ---
                    expand=True,
                    controls=[
                    Container(                  # -- Seccion 1 --
                        expand=True,
                        bgcolor="#858585", 
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
                                                bgcolor="#B6DE3A",
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
                                        ]
                                    ),
                                    
                                )
                                
                            ]
                        )
                    ),
                    Container(                  # -- Seccion 2 --     
                        expand=True,
                        bgcolor="#858585", 
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
                                            #DropBox de Inputs
                                            Container(
                                                #Text("Ingresar !"),
                                                bgcolor="#B6DE3A",
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
                                                bgcolor="#B6DE3A",
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
                                            Text("Maximo de Empalmes por Bobina"),
                                            TextField(
                                                label="N/A",
                                                border= InputBorder.OUTLINE,
                                                border_color="Black",
                                                label_style=TextStyle(color="Black",italic=True),
                                            ),
                                            Text("Orientación de Bobina en Tarima"),
                                            Dropdown(
                                                label="Orientación",
                                                hint_text="Orientación de Bobina",
                                                options=[
                                                    dropdown.Option("N/A"),
                                                    dropdown.Option("Horizontal"),
                                                    dropdown.Option("Vertical"),
                                                ],
                                                autofocus=True,
                                                on_change= lambda e: print(e.control.value)  # Imprimir el resultado
                                            ),
                                            Text("Tipó de Empaque para Bonina"),
                                            Dropdown(
                                                label="Empaque",
                                                hint_text="Tipo de Empaque",
                                                options=[
                                                    dropdown.Option("N/A"),
                                                    dropdown.Option("Emplaye"),
                                                    dropdown.Option("Bolsa"),
                                                    
                                                ],
                                                autofocus=True,
                                                on_change= lambda e: print(e.control.value)  # Imprimir el resultado
                                            ),
                                            Text("Pesar producto Por"),
                                            Dropdown(
                                                label="Pesar por..",
                                                hint_text="Pesar producto",
                                                options=[
                                                    dropdown.Option("N/A"),
                                                    dropdown.Option("Tarima"),
                                                    dropdown.Option("Bobina"),
                                                    dropdown.Option("Ambos")
                                                ],
                                                autofocus=True,
                                                on_change= lambda e: print(e.control.value)  # Imprimir el resultado
                                            ),
                                            #DropBox de Inputs
                                            Container(
                                                #Text("Ingresar !"),
                                                bgcolor="#B6DE3A",
                                                alignment=alignment.center,
                                                border_radius=5,
                                                padding=5,
                                                content= PopupMenuButton(
                                                    Text("Peso neto Promedio de Bobina"),
                                                    bgcolor="white",
                                                    menu_position=PopupMenuPosition.OVER,
                                                    items=[ 
                                                        PopupMenuItem(
                                                            content= Column(width=200,controls=[
                                                                Text("Peso Neto"),
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
                                        ]
                                    ),
                                    
                                )
                                
                            ]
                        )
                    ),
                    Container(                  # -- Seccion 3 --   
                        expand=True,
                        bgcolor="#858585", 
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
                                            #DropBox de Inputs
                                            Container(
                                                #Text("Ingresar !"),
                                                bgcolor="#B6DE3A",
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
                                            ),
                                            Text("Etiquetado"),
                                            Dropdown(
                                                label="Pesar por..",
                                                hint_text="Pesar producto",
                                                options=[
                                                    dropdown.Option("N/A"),
                                                    dropdown.Option("Rollo Individual"),
                                                    dropdown.Option("Tarima"),
                                                    dropdown.Option("Ambos")
                                                ],
                                                autofocus=True,
                                                on_change= lambda e: print(e.control.value)  # Imprimir el resultado
                                            ),
                                            #DropBox de Inputs
                                            Container(
                                                bgcolor="#B6DE3A",
                                                alignment=alignment.center,
                                                border_radius=5,
                                                padding=5,
                                                content= PopupMenuButton(
                                                    Text("Numero de Bobinas por Cama y Camas por Tarima"),
                                                    bgcolor="white",
                                                    menu_position=PopupMenuPosition.OVER,
                                                    items=[ 
                                                        PopupMenuItem(
                                                            content= Column(width=200,controls=[
                                                                Text("Bobinas por Cama"),
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
                                                                Text("Camas por Bobina"),
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
                                            Text("Numero de Bobinas en Tarima"),
                                            TextField(
                                                label="Ingresar Numero de Bobinas",
                                                border= InputBorder.OUTLINE,
                                                border_color="Black",
                                                label_style=TextStyle(color="Black",italic=True),
                                            ),
                                            #DropBox de Inputs
                                            Container(
                                                #Text("Ingresar !"),
                                                bgcolor="#B6DE3A",
                                                alignment=alignment.center,
                                                border_radius=5,
                                                padding=5,
                                                content= PopupMenuButton(
                                                    Text("Peso neto Promedio por Tarima"),
                                                    bgcolor="white",
                                                    menu_position=PopupMenuPosition.OVER,
                                                    items=[ 
                                                        PopupMenuItem(
                                                            content= Column(width=200,controls=[
                                                                Text("Peso"),
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
                                            Text("La tarima llevara emplaye"),
                                            Dropdown(
                                                label="Ingresar opción",
                                                hint_text="Emplaye",
                                                options=[
                                                    dropdown.Option("N/A"),
                                                    dropdown.Option("Aplica"),
                                                ],
                                                autofocus=True,
                                                on_change= lambda e: print(e.control.value)  # Imprimir el resultado
                                            ),
                                            Text("La tarima sera refilada"),
                                            Dropdown(
                                                label="Ingresar opción",
                                                hint_text="Refilado",
                                                options=[
                                                    dropdown.Option("N/A"),
                                                    dropdown.Option("Aplica"),
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

        # Contenedor de Boton Agregar a la BD
        self.cntBtn = Container(
            #expand=True,
            bgcolor=self.color_teal,
            padding=5,
            border_radius=5,
            content= Row(
                alignment=MainAxisAlignment.END,
                controls=[
                    self.btn
                ]
            )
        )

########################################################################

        # Frame Main
        self.frameMain = Container(
            bgcolor="#737373",
            padding=2,
            content=Column(
                controls=[
                    self.cntHeader,
                    self.vtnFicha_Ventas,       # Contenedor de FICHA / VENTAS como Inicio
                    self.cntBtn,
                ]
            )
        )

#################### PRUEBAS #######################
    
    def ji(self,id):
        print(id)
        self.txt = Container(
            bgcolor="red",
            width=50,
            height=50
        )
        self.frameMain.content.controls = [self.cntHeader]
        self.frameMain.content.controls.append(self.txt)
        #self.frameMain.content.controls.append(self.cntBtn)
        self.update()
        
        #self.id_product.update(
        
    def navTabs(self,e):
        id = e.control.selected_index
        #print(id)
        dic = [
            self.vtnFicha_Ventas,
            self.vtnExtr,
            self.vtnImprDigtl,
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
        self.frameMain.content.controls.append(self.cntBtn)

        self.update()

          # Limpiar Labels
    def clean_fields(self,e):
        self.Inpts.id_product.value = ""
        self.Inpts.cliente.value = ""
        self.Inpts.producto.value = ""
        self.Inpts.fecha_Elav.value = ""
        self.Inpts.fecha_Rev.value = ""
        self.update()

    def add_fields(self):
        self.Inpts.id_product.value = "Value"
        self.Inpts.cliente.value = "Value"
        self.Inpts.producto.value = "Value"
        self.Inpts.fecha_Elav.value = "Value"
        self.Inpts.fecha_Rev.value = "Value"
        self.update()
    
    def upd(self,e):
        #self.Inpts.pruData()
        self.Inpts.prCero()
        self.update()
  
    def build(self):
        return self.frameMain

def main(page: Page):
    page.theme_mode = ThemeMode.DARK
    page.add(createPrind(page))
    #margin=margin.only(top=-5)

#app(main)