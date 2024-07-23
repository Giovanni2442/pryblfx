from flet import * 
from src.views.VentanaCreate.Verificaciones import verificaciones
from src.app.filExcel.filtroExcel import filter

class Inpts_Lam():
    def __init__(self,page):
        super().__init__()
    
    ### INPUTS DE LAS TABLAS DE LAMINADO ###

    ### GENERAL / MATERIAL IMPRESO ###
        self.estrcPrdct = TextField(
            label="Estructura del Producto",
            border= InputBorder.OUTLINE,
            border_color="Black",
            label_style=TextStyle(color="Black",italic=True),
        )

        self.medMngTransf = PopupMenuButton(
            Text("Medida de la Manga para Transferencia"),
            bgcolor="white",
            menu_position=PopupMenuPosition.OVER,
            items=[ 
                PopupMenuItem(
                    content= Column(width=200,controls=[
                        Text("Manga"),
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

        self.anchCore_Tol = PopupMenuButton(
            Text("Ancho de Core y Tolerancia"),
            bgcolor="white",
            menu_position=PopupMenuPosition.OVER,
            items=[ 
                PopupMenuItem(
                    content= Column(width=200,controls=[
                        Text("Ancho"),
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

        self.dmtrGrsrCore = PopupMenuButton(
            Text("Diametro y Grosor de Core"),
            bgcolor="white",
            menu_position=PopupMenuPosition.OVER,
            items=[ 
                PopupMenuItem(
                    content= Column(width=200,controls=[
                        Text("Diametro"),
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
                        Text("Grosor de Core"),
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

        self.dmtrBob_Tol = PopupMenuButton(
            Text("Diametro de Bobina y Tolerancia"),
            bgcolor="white",
            menu_position=PopupMenuPosition.OVER,
            items=[ 
                PopupMenuItem(
                    content= Column(width=200,controls=[
                        Text("Diametro Bobina"),
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

        self.mxmEmplBob = TextField(
            label="Maximo de Empalmes por Bobina",
            border= InputBorder.OUTLINE,
            border_color="Black",
            label_style=TextStyle(color="Black",italic=True),
        )

        self.orntBobRck = TextField(
            label="Orientación de Bobina en Rack",
            border= InputBorder.OUTLINE,
            border_color="Black",
            label_style=TextStyle(color="Black",italic=True),
        )

        self.tipEmpqBob = TextField(
            label="Tipo de Empaque para Bobina",
            border= InputBorder.OUTLINE,
            border_color="Black",
            label_style=TextStyle(color="Black",italic=True),
        )

        self.etiquetado = Dropdown(
            label="Etiquetado",
            hint_text="etiquetado",
            options=[
                dropdown.Option("N/A"),
                dropdown.Option("ROLLO INDIVIDUAL"),
                dropdown.Option("TARIMA"),
                dropdown.Option("AMBAS"),
            ],
            autofocus=True,
            on_change= lambda e: print(e.control.value)  # Imprimir el resultado
        )

        self.psrPrdct = Dropdown(
            label="Pesar producto por : ",
            hint_text="pesar por ..",
            options=[
                dropdown.Option("N/A"),
                dropdown.Option("TARIMA"),
                dropdown.Option("BOBINA"),
                dropdown.Option("AMBAS"),
            ],
            autofocus=True,
            on_change= lambda e: print(e.control.value)  # Imprimir el resultado
        )
    
        self.psNtPromBob = TextField(
            label="Peso Neto Promedio de Bobina",
            border= InputBorder.OUTLINE,
            border_color="Black",
            label_style=TextStyle(color="Black",italic=True),
        )
    ##########################################################

        ### LAMINAR ####

    ### LAMINACIÓN N.1 ###

        self.LN1clbPel_Tol = PopupMenuButton(
            Text("Calibre de Pelicula y Tolerancia"),
            bgcolor="white",
            menu_position=PopupMenuPosition.OVER,
            items=[ 
                PopupMenuItem(
                    content= Column(width=200,controls=[
                        Text("Calibre"),
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

        self.LN1anchBob_Tol = PopupMenuButton(
            Text("Ancho de Bobina y Tolerancia"),
            bgcolor="white",
            menu_position=PopupMenuPosition.OVER,
            items=[ 
                PopupMenuItem(
                    content= Column(width=200,controls=[
                        Text("Ancho Bobina"),
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

        self.LN1tipTratado = Dropdown(
            label="Tipo de Tratado",
            hint_text="etiquetado",
            options=[
                dropdown.Option("N/A"),
                dropdown.Option("UNA CARA"),
                dropdown.Option("AMBAS CARAS"),
                dropdown.Option("SIN TRATADO"),
            ],
            autofocus=True,
            on_change= lambda e: print(e.control.value)  # Imprimir el resultado
        )

        self.LN1orntBobTam = Dropdown(
            label="Orientación de Bobina en Tarima",
            hint_text="Orientación",
            options=[
                dropdown.Option("N/A"),
                dropdown.Option("HORIZONTAL"),
                dropdown.Option("VERTICAL"),
            ],
            autofocus=True,
            on_change= lambda e: print(e.control.value)  # Imprimir el resultado
        )

    ###############################

    ### LAMINACIÓN N.2 ###

        self.LN2clbPel_Tol = PopupMenuButton(
            Text("Calibre de Pelicula y Tolerancia"),
            bgcolor="white",
            menu_position=PopupMenuPosition.OVER,
            items=[ 
                PopupMenuItem(
                    content= Column(width=200,controls=[
                        Text("Calibre"),
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

        self.LN2anchBob_Tol = PopupMenuButton(
            Text("Ancho de Bobina y Tolerancia"),
            bgcolor="white",
            menu_position=PopupMenuPosition.OVER,
            items=[ 
                PopupMenuItem(
                    content= Column(width=200,controls=[
                        Text("Ancho Bobina"),
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

        self.LN2tipTratado = Dropdown(
            label="Tipo de Tratado",
            hint_text="etiquetado",
            options=[
                dropdown.Option("N/A"),
                dropdown.Option("UNA CARA"),
                dropdown.Option("AMBAS CARAS"),
                dropdown.Option("SIN TRATADO"),
            ],
            autofocus=True,
            on_change= lambda e: print(e.control.value)  # Imprimir el resultado
        )

        self.LN2orntBobTam = Dropdown(
            label="Orientación de Bobina en Tarima",
            hint_text="Orientación",
            options=[
                dropdown.Option("N/A"),
                dropdown.Option("HORIZONTAL"),
                dropdown.Option("VERTICAL"),
            ],
            autofocus=True,
            on_change= lambda e: print(e.control.value)  # Imprimir el resultado
        )

    ### LAMINACIÓN N.3 ###

        self.LN3clbPel_Tol = PopupMenuButton(
            Text("Calibre de Pelicula y Tolerancia"),
            bgcolor="white",
            menu_position=PopupMenuPosition.OVER,
            items=[ 
                PopupMenuItem(
                    content= Column(width=200,controls=[
                        Text("Calibre"),
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

        self.LN3anchBob_Tol = PopupMenuButton(
            Text("Ancho de Bobina y Tolerancia"),
            bgcolor="white",
            menu_position=PopupMenuPosition.OVER,
            items=[ 
                PopupMenuItem(
                    content= Column(width=200,controls=[
                        Text("Ancho Bobina"),
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

        self.LN3tipTratado = Dropdown(
            label="Tipo de Tratado",
            hint_text="etiquetado",
            options=[
                dropdown.Option("N/A"),
                dropdown.Option("UNA CARA"),
                dropdown.Option("AMBAS CARAS"),
                dropdown.Option("SIN TRATADO"),
            ],
            autofocus=True,
            on_change= lambda e: print(e.control.value)  # Imprimir el resultado
        )

        self.LN3orntBobTam = Dropdown(
            label="Orientación de Bobina en Tarima",
            hint_text="Orientación",
            options=[
                dropdown.Option("N/A"),
                dropdown.Option("HORIZONTAL"),
                dropdown.Option("VERTICAL"),
            ],
            autofocus=True,
            on_change= lambda e: print(e.control.value)  # Imprimir el resultado
        )

    ### LAMINACIÓN N.4 ###

        self.LN4clbPel_Tol = PopupMenuButton(
            Text("Calibre de Pelicula y Tolerancia"),
            bgcolor="white",
            menu_position=PopupMenuPosition.OVER,
            items=[ 
                PopupMenuItem(
                    content= Column(width=200,controls=[
                        Text("Calibre"),
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

        self.LN4anchBob_Tol = PopupMenuButton(
            Text("Ancho de Bobina y Tolerancia"),
            bgcolor="white",
            menu_position=PopupMenuPosition.OVER,
            items=[ 
                PopupMenuItem(
                    content= Column(width=200,controls=[
                        Text("Ancho Bobina"),
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

        self.LN4tipTratado = Dropdown(
            label="Tipo de Tratado",
            hint_text="etiquetado",
            options=[
                dropdown.Option("N/A"),
                dropdown.Option("UNA CARA"),
                dropdown.Option("AMBAS CARAS"),
                dropdown.Option("SIN TRATADO"),
            ],
            autofocus=True,
            on_change= lambda e: print(e.control.value)  # Imprimir el resultado
        )

        self.LN4orntBobTam = Dropdown(
            label="Orientación de Bobina en Tarima",
            hint_text="Orientación",
            options=[
                dropdown.Option("N/A"),
                dropdown.Option("HORIZONTAL"),
                dropdown.Option("VERTICAL"),
            ],
            autofocus=True,
            on_change= lambda e: print(e.control.value)  # Imprimir el resultado
        )

        #### SUBMENU DE LAMINASIÓN ###
        self.subMenuLam = Container(   # Contenedor SUBMENU
            #expand=True,
            bgcolor="yellow",
            padding=3,
            content= 
                Row([           # --- SUBMENU PARA SECCIÓNAR LAS LAMINACIÓNES --- #
                    FilledButton(
                        expand=True,
                        height=20,
                        text = "Texto 1",
                        style = ButtonStyle(
                            #bgcolor="#616F67",
                            shape={
                            #ControlState.HOVERED: RoundedRectangleBorder(radius=15),
                            ControlState.DEFAULT: RoundedRectangleBorder(radius=2)
                            },
                        ),
                        on_click= self.subMnuLamFunc
                    ),
                    FilledButton(
                        expand=True,
                        #border_radius=0,
                        height=20,
                        text = "Texto 2",
                        style = ButtonStyle(
                            #bgcolor="#616F67",
                            shape={
                            #ControlState.HOVERED: RoundedRectangleBorder(radius=15),
                            ControlState.DEFAULT: RoundedRectangleBorder(radius=2)
                            },
                        ),
                        on_click= self.subMnuLamFunc
                    )        
                ])
        )

    def subMnuLamFunc(self,e):
        id = e.control.text
        dic = {
            "Texto 1" : a,
            "Texto 2" : b
        }
        print(dic[id])





