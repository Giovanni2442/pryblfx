from flet import * 
from src.views.VentanaCreate.Verificaciones import verificaciones
from src.app.filExcel.filtroExcel import filter

class Inpts_Lam():
    def __init__(self,page):
        super().__init__()
    
    ### INPUTS DE LAS TABLAS DE LAMINADO ###

    ### GENERAL ###
        self.estrcPrdct = TextField(            # GENERAL
            label="Estructura del Producto",
            border= InputBorder.OUTLINE,
            border_color="Black",
            value="N/A",
            error_text = "",
            label_style=TextStyle(color="Black",italic=True),
        )

        self.medMngTransf = PopupMenuButton(    # GENERAL
            Text("Medida de la Manga para Transferencia"),
            bgcolor="white",
            menu_position=PopupMenuPosition.OVER,
            items=[ 
                PopupMenuItem(
                    content= Column(width=200,controls=[
                        Text("Manga"),
                        TextField(
                            label="Manga",
                            border= InputBorder.OUTLINE,
                            #width=100,
                            border_color="black",
                            value=0,
                            error_text = "",
                            label_style=TextStyle(color="black",italic=True),
                        )
                    ])
                ),
                PopupMenuItem(
                    content= Column([
                        Text("Tolerancia"),
                        TextField(
                            label="tolerancia",
                            border= InputBorder.OUTLINE,
                            border_color="Black",
                            value=0,
                            error_text = "",
                            label_style=TextStyle(color="Black",italic=True),
                        )
                    ])
                ),
            ]
        )

        self.anchCore_Tol = PopupMenuButton(    # GENERAL
            Text("Ancho de Core y Tolerancia"),
            bgcolor="white",
            menu_position=PopupMenuPosition.OVER,
            items=[ 
                PopupMenuItem(
                    content= Column(width=200,controls=[
                        Text("Ancho"),
                        TextField(
                            label="ancho",
                            border= InputBorder.OUTLINE,
                            #width=100,
                            border_color="black",
                            value=0,
                            error_text = "",
                            label_style=TextStyle(color="black",italic=True),
                        )
                    ])
                ),
                PopupMenuItem(
                    content= Column([
                        Text("Tolerancia"),
                        TextField(
                            label="tolerancia",
                            border= InputBorder.OUTLINE,
                            border_color="Black",
                            value=0,
                            error_text = "",
                            label_style=TextStyle(color="Black",italic=True),
                        )
                    ])
                ),
            ]
        )

        self.dmtrGrsrCore = PopupMenuButton(    # GENERAL
            Text("Diametro y Grosor de Core"),
            bgcolor="white",
            menu_position=PopupMenuPosition.OVER,
            items=[ 
                PopupMenuItem(
                    content= Column(width=200,controls=[
                        Text("Diametro"),
                        TextField(
                            label="Diametro",
                            border= InputBorder.OUTLINE,
                            #width=100,
                            border_color="black",
                            value=0,
                            error_text = "",
                            label_style=TextStyle(color="black",italic=True),
                        )
                    ])
                ),
                PopupMenuItem(
                    content= Column([
                        Text("Grosor de Core"),
                        TextField(
                            label="grosor",
                            border= InputBorder.OUTLINE,
                            border_color="Black",
                            value=0,
                            error_text = "",
                            label_style=TextStyle(color="Black",italic=True),
                        )
                    ])
                ),
            ]
        )

        self.dmtrBob_Tol = PopupMenuButton(     # GENERAL
            Text("Diametro de Bobina y Tolerancia"),
            bgcolor="white",
            menu_position=PopupMenuPosition.OVER,
            items=[ 
                PopupMenuItem(
                    content= Column(width=200,controls=[
                        Text("Diametro Bobina"),
                        TextField(
                            label="Diametro",
                            border= InputBorder.OUTLINE,
                            #width=100,
                            border_color="black",
                            value=0,
                            error_text = "",
                            label_style=TextStyle(color="black",italic=True),
                        )
                    ])
                ),
                PopupMenuItem(
                    content= Column([
                        Text("Tolerancia"),
                        TextField(
                            label="tolerancia",
                            border= InputBorder.OUTLINE,
                            border_color="Black",
                            value=0,
                            error_text = "",
                            label_style=TextStyle(color="Black",italic=True),
                        )
                    ])
                ),
            ]
        )

        self.mxmEmplBob = TextField(            # GENERAL
            label="Maximo de Empalmes por Bobina",
            border= InputBorder.OUTLINE,
            border_color="Black",
            value=0,
            error_text = "",
            label_style=TextStyle(color="Black",italic=True),
        )

        self.orntBobRck = TextField(            # GENERAL
            label="Orientación de Bobina en Rack",
            border= InputBorder.OUTLINE,
            border_color="Black",
            value="N/A",
            error_text = "",
            label_style=TextStyle(color="Black",italic=True),
        )

        self.tipEmpqBob = TextField(            # GENERAL
            label="Tipo de Empaque para Bobina",
            border= InputBorder.OUTLINE,
            border_color="Black",
            value="N/A",
            error_text = "",
            label_style=TextStyle(color="Black",italic=True),
        )

        self.etiquetado = Dropdown(             # GENERAL
            label="Etiquetado",
            hint_text="etiquetado",
            value="N/A",
            error_text = "",
            options=[
                dropdown.Option("N/A"),
                dropdown.Option("ROLLO INDIVIDUAL"),
                dropdown.Option("TARIMA"),
                dropdown.Option("AMBAS"),
            ],
            autofocus=True,
            #on_change= lambda e: print(e.control.value)  # Imprimir el resultado
        )

        self.psrPrdct = Dropdown(               # GENERAL
            label="Pesar producto por : ",
            hint_text="pesar por ..",
            value="N/A",
            error_text = "",
            options=[
                dropdown.Option("N/A"),
                dropdown.Option("TARIMA"),
                dropdown.Option("BOBINA"),
                dropdown.Option("AMBAS"),
            ],
            autofocus=True,
            #on_change= lambda e: print(e.control.value)  # Imprimir el resultado
        )
    
        self.psNtPromBob = TextField(           # GENERAL
            label="Peso Neto Promedio de Bobina",
            border= InputBorder.OUTLINE,
            border_color="Black",
            value="N/A",
            error_text = "",
            label_style=TextStyle(color="Black",italic=True),
        )
    ##########################################################

    ###  MATERIAL IMPRESO ###

        self.mtlImpr = TextField(               # MatrImprs
            label="Material Impreso",
            border= InputBorder.OUTLINE,
            border_color="Black",
            value="N/A",
            error_text = "",
            label_style=TextStyle(color="Black",italic=True),
        )

        self.clPlc_Tol = PopupMenuButton(       # MatrImprs
            Text("Calibre de Pelicula y Tolerancia"),
            bgcolor="white",
            menu_position=PopupMenuPosition.OVER,
            items=[ 
                PopupMenuItem(
                    content= Column(width=200,controls=[
                        Text("Calibre"),
                        TextField(
                            label="calibre",
                            border= InputBorder.OUTLINE,
                            #width=100,
                            border_color="black",
                            value=0,
                            error_text = "",
                            label_style=TextStyle(color="black",italic=True),
                        )
                    ])
                ),
                PopupMenuItem(
                    content= Column([
                        Text("Tolerancia"),
                        TextField(
                            label="tolerancia",
                            border= InputBorder.OUTLINE,
                            border_color="Black",
                            value=0,
                            error_text = "",
                            label_style=TextStyle(color="Black",italic=True),
                        )
                    ])
                ),
            ]
        )

        self.anchBob_Tol = PopupMenuButton(       # MatrImprs
            Text("Ancho de Bobina y Tolerancia"),
            bgcolor="white",
            menu_position=PopupMenuPosition.OVER,
            items=[ 
                PopupMenuItem(
                    content= Column(width=200,controls=[
                        Text("Ancho"),
                        TextField(
                            label="ancho",
                            border= InputBorder.OUTLINE,
                            #width=100,
                            border_color="black",
                            value=0,
                            error_text = "",
                            label_style=TextStyle(color="black",italic=True),
                        )
                    ])
                ),
                PopupMenuItem(
                    content= Column([
                        Text("Tolerancia"),
                        TextField(
                            label="tolerancia",
                            border= InputBorder.OUTLINE,
                            border_color="Black",
                            value=0,
                            error_text = "",
                            label_style=TextStyle(color="Black",italic=True),
                        )
                    ])
                ),
            ]
        )
    
        self.tipTratado = Dropdown(             # MatrImprs
            label="Tratado : ",
            hint_text="tratado",
            value="N/A",
            error_text = "",
            options=[
                dropdown.Option("N/A"),
                dropdown.Option("UNA CARA"),
                dropdown.Option("AMBAS CARAS")
            ],
            autofocus=True,
            #on_change= lambda e: print(e.control.value)  # Imprimir el resultado
        )
    
    #########################

        ### LAMINAR ####

    ### LAMINACIÓN N.1 ###

        #### INGRESAR ESTE TEXTFIELD QUE FALTO JIJIJA ###
        self.LN1mtrLam = TextField(           # GENERAL
            label="Material para Laminar",
            border= InputBorder.OUTLINE,
            border_color="Black",
            value="N/A",
            error_text = "",
            label_style=TextStyle(color="Black",italic=True),
        )

        self.LN1clbPel_Tol = PopupMenuButton(
            Text("Calibre de Pelicula y Tolerancia"),
            bgcolor="white",
            menu_position=PopupMenuPosition.OVER,
            items=[ 
                PopupMenuItem(
                    content= Column(width=200,controls=[
                        Text("Calibre"),
                        TextField(
                            label="calibre",
                            border= InputBorder.OUTLINE,
                            #width=100,
                            border_color="black",
                            value=0,
                            error_text = "",
                            label_style=TextStyle(color="black",italic=True),
                        )
                    ])
                ),
                PopupMenuItem(
                    content= Column([
                        Text("Tolerancia"),
                        TextField(
                            label="tolerancia",
                            border= InputBorder.OUTLINE,
                            border_color="Black",
                            value=0,
                            error_text = "",
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
                            label="ancho",
                            border= InputBorder.OUTLINE,
                            #width=100,
                            border_color="black",
                            value=0,
                            error_text = "",
                            label_style=TextStyle(color="black",italic=True),
                        )
                    ])
                ),
                PopupMenuItem(
                    content= Column([
                        Text("Tolerancia"),
                        TextField(
                            label="Tolerancia",
                            border= InputBorder.OUTLINE,
                            border_color="Black",
                            value=0,
                            error_text = "",
                            label_style=TextStyle(color="Black",italic=True),
                        )
                    ])
                ),
            ]
        )

        self.LN1tipTratado = Dropdown(
            label="Tipo de Tratado",
            hint_text="etiquetado",
            value="N/A",
            error_text = "",
            options=[
                dropdown.Option("N/A"),
                dropdown.Option("UNA CARA"),
                dropdown.Option("AMBAS CARAS"),
                dropdown.Option("SIN TRATADO"),
            ],
            autofocus=True,
            #on_change= lambda e: print(e.control.value)  # Imprimir el resultado
        )

        self.LN1tipLam = Dropdown(
            label="Tipo de Laminación",
            hint_text="Laminación",
            value="N/A",
            error_text = "",
            options=[
                dropdown.Option("N/A"),
                dropdown.Option("INTERNA"),
                dropdown.Option("EXTERNA"),
            ],
            autofocus=True,
            #on_change= lambda e: print(e.control.value)  # Imprimir el resultado
        )

    ###############################

    ### LAMINACIÓN N.2 ###
        self.LN2mtrLam = TextField(           # GENERAL
            label="Material para Laminar",
            border= InputBorder.OUTLINE,
            border_color="Black",
            value="N/A",
            error_text = "",
            label_style=TextStyle(color="Black",italic=True),
        )

        self.LN2clbPel_Tol = PopupMenuButton(
            Text("Calibre de Pelicula y Tolerancia"),
            bgcolor="white",
            menu_position=PopupMenuPosition.OVER,
            items=[ 
                PopupMenuItem(
                    content= Column(width=200,controls=[
                        Text("Calibre"),
                        TextField(
                            label="calibre",
                            border= InputBorder.OUTLINE,
                            #width=100,
                            border_color="black",
                            value=0,
                            error_text = "",
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
                            value=0,
                            error_text = "",
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
                            label="Ancho",
                            border= InputBorder.OUTLINE,
                            #width=100,
                            border_color="black",
                            value=0,
                            error_text = "",
                            label_style=TextStyle(color="black",italic=True),
                        )
                    ])
                ),
                PopupMenuItem(
                    content= Column([
                        Text("Tolerancia"),
                        TextField(
                            label="Tolerancia",
                            border= InputBorder.OUTLINE,
                            border_color="Black",
                            value=0,
                            error_text = "",
                            label_style=TextStyle(color="Black",italic=True),
                        )
                    ])
                ),
            ]
        )

        self.LN2tipTratado = Dropdown(
            label="Tipo de Tratado",
            hint_text="etiquetado",
            value="N/A",
            error_text = "",
            options=[
                dropdown.Option("N/A"),
                dropdown.Option("UNA CARA"),
                dropdown.Option("AMBAS CARAS"),
                dropdown.Option("SIN TRATADO"),
            ],
            autofocus=True,
            on_change= lambda e: print(e.control.value)  # Imprimir el resultado
        )

        self.LN2tipLam = Dropdown(
            label="Tipo de Laminación",
            hint_text="Laminación",
            value="N/A",
            error_text = "",
            options=[
                dropdown.Option("N/A"),
                dropdown.Option("INTERNA"),
                dropdown.Option("EXTERNA"),
            ],
            autofocus=True,
            #on_change= lambda e: print(e.control.value)  # Imprimir el resultado
        )

    ### LAMINACIÓN N.3 ###
        self.LN3mtrLam = TextField(           # GENERAL
            label="Material para Laminar",
            border= InputBorder.OUTLINE,
            border_color="Black",
            value="N/A",
            error_text = "",
            label_style=TextStyle(color="Black",italic=True),
        )

        self.LN3clbPel_Tol = PopupMenuButton(
            Text("Calibre de Pelicula y Tolerancia"),
            bgcolor="white",
            menu_position=PopupMenuPosition.OVER,
            items=[ 
                PopupMenuItem(
                    content= Column(width=200,controls=[
                        Text("Calibre"),
                        TextField(
                            label="Calibre",
                            border= InputBorder.OUTLINE,
                            #width=100,
                            border_color="black",
                            value=0,
                            error_text = "",
                            label_style=TextStyle(color="black",italic=True),
                        )
                    ])
                ),
                PopupMenuItem(
                    content= Column([
                        Text("Tolerancia"),
                        TextField(
                            label="Tolerancia",
                            border= InputBorder.OUTLINE,
                            border_color="Black",
                            value=0,
                            error_text = "",
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
                            label="Ancho",
                            border= InputBorder.OUTLINE,
                            #width=100,
                            border_color="black",
                            value=0,
                            error_text = "",
                            label_style=TextStyle(color="black",italic=True),
                        )
                    ])
                ),
                PopupMenuItem(
                    content= Column([
                        Text("Tolerancia"),
                        TextField(
                            label="Tolerancia",
                            border= InputBorder.OUTLINE,
                            border_color="Black",
                            value=0,
                            error_text = "",
                            label_style=TextStyle(color="Black",italic=True),
                        )
                    ])
                ),
            ]
        )

        self.LN3tipTratado = Dropdown(
            label="Tipo de Tratado",
            hint_text="etiquetado",
            value="N/A",
            error_text = "",
            options=[
                dropdown.Option("N/A"),
                dropdown.Option("UNA CARA"),
                dropdown.Option("AMBAS CARAS"),
                dropdown.Option("SIN TRATADO"),
            ],
            autofocus=True,
            on_change= lambda e: print(e.control.value)  # Imprimir el resultado
        )

        self.LN3tipLam = Dropdown(
            label="Tipo de Laminación",
            hint_text="Laminación",
            value="N/A",
            error_text = "",
            options=[
                dropdown.Option("N/A"),
                dropdown.Option("INTERNA"),
                dropdown.Option("EXTERNA"),
            ],
            autofocus=True,
            #on_change= lambda e: print(e.control.value)  # Imprimir el resultado
        )

    ### LAMINACIÓN N.4 ###
        
        self.LN4mtrLam = TextField(           # GENERAL
            label="Material para Laminar",
            border= InputBorder.OUTLINE,
            border_color="Black",
            value="N/A",
            error_text = "",
            label_style=TextStyle(color="Black",italic=True),
        )

        self.LN4clbPel_Tol = PopupMenuButton(
            Text("Calibre de Pelicula y Tolerancia"),
            bgcolor="white",
            menu_position=PopupMenuPosition.OVER,
            items=[ 
                PopupMenuItem(
                    content= Column(width=200,controls=[
                        Text("Calibre"),
                        TextField(
                            label="Calibre",
                            border= InputBorder.OUTLINE,
                            #width=100,
                            border_color="black",
                            value=0,
                            error_text = "",
                            label_style=TextStyle(color="black",italic=True),
                        )
                    ])
                ),
                PopupMenuItem(
                    content= Column([
                        Text("Tolerancia"),
                        TextField(
                            label="Tolerancia",
                            border= InputBorder.OUTLINE,
                            border_color="Black",
                            value=0,
                            error_text = "",
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
                            value=0,
                            error_text = "",
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
                            value=0,
                            error_text = "",
                            label_style=TextStyle(color="Black",italic=True),
                        )
                    ])
                ),
            ]
        )

        self.LN4tipTratado = Dropdown(
            label="Tipo de Tratado",
            hint_text="etiquetado",
            value="N/A",
            error_text = "",
            options=[
                dropdown.Option("N/A"),
                dropdown.Option("UNA CARA"),
                dropdown.Option("AMBAS CARAS"),
                dropdown.Option("SIN TRATADO"),
            ],
            autofocus=True,
            #on_change= lambda e: print(e.control.value)  # Imprimir el resultado
        )

        self.LN4tipLam = Dropdown(
            label="Tipo de Laminación",
            hint_text="Laminación",
            value="N/A",
            error_text = "",
            options=[
                dropdown.Option("N/A"),
                dropdown.Option("INTERNA"),
                dropdown.Option("EXTERNA"),
            ],
            autofocus=True,
            #on_change= lambda e: print(e.control.value)  # Imprimir el resultado
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
                        #on_click= self.subMnuLamFunc
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
                        #on_click= self.subMnuLamFunc
                    )        
                ])
        )

    def tplInptsLam(self):
        return [
            self.estrcPrdct,
            self.mxmEmplBob,
            self.orntBobRck,
            self.tipEmpqBob,
            self.etiquetado,
            self.psrPrdct,
            self.psNtPromBob,

            self.medMngTransf,
            self.anchCore_Tol,
            self.dmtrGrsrCore,
            self.dmtrBob_Tol,

            [   # --- MATERIAL IMPRESO --- #
                self.mtlImpr,
                self.tipTratado,
                self.clPlc_Tol,
                self.anchBob_Tol,
            ],

            [   # --- LAMINAR 1 --- #
                self.LN1mtrLam,
                self.LN1tipTratado,
                self.LN1tipLam,
                self.LN1clbPel_Tol,
                self.LN1anchBob_Tol,
            ],

            [   # --- LAMINAR 2 --- #
                self.LN2mtrLam,
                self.LN2tipTratado,
                self.LN2tipLam,
                self.LN2clbPel_Tol,
                self.LN2anchBob_Tol,
            ],

            [   # --- LAMINAR 3 --- #
                self.LN3mtrLam,
                self.LN3tipTratado,
                self.LN3tipLam,
                self.LN3clbPel_Tol,
                self.LN3anchBob_Tol,
            ],

            [   # --- LAMINAR 4 --- #
                self.LN4mtrLam,
                self.LN4tipTratado,
                self.LN4tipLam,
                self.LN4clbPel_Tol,
                self.LN4anchBob_Tol,
            ]

        ]





