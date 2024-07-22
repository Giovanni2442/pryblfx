from flet import * 
from src.views.VentanaCreate.Verificaciones import verificaciones
from src.app.filExcel.filtroExcel import filter


class InptsExtrc():
    def __init__(self,page):
        super().__init__()

        self.page = page
        self.valida = verificaciones(page)

        ### INPUTS DE TABLA EXTRUCIÓN ###
        
        ### SECCIÓN 1 ##
        self.tipMtrlExtr = TextField(
            label="Ingresar tipo de material",
            border= InputBorder.OUTLINE,
            border_color="Black",
            label_style=TextStyle(color="Black",italic=True),
        )
    
        self.dinajeReq = TextField(
            label="Dinaje",
            border= InputBorder.OUTLINE,
            border_color="Black",
            label_style=TextStyle(color="Black",italic=True),
        )

        self.frmlExtr = TextField(
            label="Formula Extrusión",
            border= InputBorder.OUTLINE,
            border_color="Black",
            label_style=TextStyle(color="Black",italic=True),
        )

        self.pigmPelc = TextField(
            label="Dinaje",
            border= InputBorder.OUTLINE,
            border_color="Black",
            label_style=TextStyle(color="Black",italic=True),
        )
    
        self.tipBob = Dropdown(
            label="Laminado",
            hint_text="Producto Laminado",
            options=[
                dropdown.Option("N/A"),
                dropdown.Option("Lamina"),
                dropdown.Option("Tabular Abierta"),
            ],
            autofocus=True,
            on_change= lambda e: print(e.control.value)  # Imprimir el resultado
        )

        self.tipTratado =  Dropdown(
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
        )
        #####################

        #GestureDetector(),
        ### SECCION 2 ###
        self.anchBob_Tol = PopupMenuButton(
            Text("Ancho de Bobina y Tolerancia!"),
            bgcolor="red",
            #padding=10,
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

        self.anchCore_Tol = PopupMenuButton(
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

        self.maxEmplBob = TextField(
            label="N/A",
            border= InputBorder.OUTLINE,
            border_color="Black",
            label_style=TextStyle(color="Black",italic=True),
        )

        self.orntBobTam = Dropdown(
            label="Orientación",
            hint_text="Orientación de Bobina",
            options=[
                dropdown.Option("N/A"),
                dropdown.Option("Horizontal"),
                dropdown.Option("Vertical"),
            ],
            autofocus=True,
            on_change= lambda e: print(e.control.value)  # Imprimir el resultado
        )

        self.tipEmpqBob = Dropdown(
            label="Empaque",
            hint_text="Tipo de Empaque",
            options=[
                dropdown.Option("N/A"),
                dropdown.Option("Emplaye"),
                dropdown.Option("Bolsa"),
                
            ],
            autofocus=True,
            on_change= lambda e: print(e.control.value)  # Imprimir el resultado
        )

        self.psrPrdct = Dropdown(
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
        )
    
        self.psPromBob = PopupMenuButton(
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
    
        ################################
    
        ### SECCIÓN 3 ###
        self.DimBob_Tol = PopupMenuButton(
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

        self.etiquetado = Dropdown(
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
        )

        self.numBobCma_CmaTrm = PopupMenuButton(
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

        self.numBobTam = TextField(
            label="Ingresar Numero de Bobinas",
            border= InputBorder.OUTLINE,
            border_color="Black",
            label_style=TextStyle(color="Black",italic=True),
        )

        self.psNtPromTam = PopupMenuButton(
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

        self.tamEmplaye = Dropdown(
            label="Ingresar opción",
            hint_text="Emplaye",
            options=[
                dropdown.Option("N/A"),
                dropdown.Option("Aplica"),
            ],
            autofocus=True,
            on_change= lambda e: print(e.control.value)  # Imprimir el resultado
        )

        self.tamRefila = Dropdown(
            label="Ingresar opción",
            hint_text="Refilado",
            options=[
                dropdown.Option("N/A"),
                dropdown.Option("Aplica"),
            ],
            autofocus=True,
            on_change= lambda e: print(e.control.value)  # Imprimir el resultado
        )
