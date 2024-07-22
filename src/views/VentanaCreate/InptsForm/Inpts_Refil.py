from flet import *
from src.views.VentanaCreate.Verificaciones import verificaciones
from src.app.filExcel.filtroExcel import filter

class Inpts_Refil():
    def __init__(self,page):
        super().__init__()

    ### INPUTS DE LA TABLA REFILADO ###

    ### SESSIÓN 1 ###
        self.procRef = Dropdown(
            label="Proceso Refilado",
            hint_text="Proceso",
            options=[
                dropdown.Option("N/A"),
                dropdown.Option("DOBLADO"),
                dropdown.Option("REFILADO"),
                dropdown.Option("AMBOS"),
            ],
            autofocus=True,
            on_change= lambda e: print(e.control.value)  # Imprimir el resultado
        )

        self.anchBobRefDbl = PopupMenuButton(
            Text("Ancho Final de Bobina al Refilarse/Doblarse"),
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

        self.acabdBob = Dropdown(
            label="Proceso Refilado",
            hint_text="Proceso",
            options=[
                dropdown.Option("N/A"),
                dropdown.Option("COMERCIAL"),
                dropdown.Option("ESPEJO"),
            ],
            autofocus=True,
            on_change= lambda e: print(e.control.value)  # Imprimir el resultado
        )
        
        self.anchCre_Tol = PopupMenuButton(
            Text("Ancho de Core y Tolerancia"),
            bgcolor="white",
            menu_position=PopupMenuPosition.OVER,
            items=[ 
                PopupMenuItem(
                    content= Column(width=200,controls=[
                        Text("Ancho Core"),
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
        
        self.grsrCore = TextField(
                label="Grosor de Core",
                border= InputBorder.OUTLINE,
                border_color="Black",
                label_style=TextStyle(color="Black",italic=True),
        )

    ### SECCIÓN 2 ###
        self.figEmb = Dropdown(
            label="Figura de Embobinado",
            hint_text="Figura",
            options=[
                dropdown.Option(0),
                dropdown.Option(1),
                dropdown.Option(2),
                dropdown.Option(3),
                dropdown.Option(4),
                dropdown.Option(5),
                dropdown.Option(6),
                dropdown.Option(7),
                dropdown.Option(8),
            ],
            autofocus=True,
            on_change= lambda e: print(e.control.value)  # Imprimir el resultado
        )

        self.bobRef_Dbl = Dropdown(
            label="La bobina se Refilira / Doblara",
            hint_text="Proceso",
            options=[
                dropdown.Option("N/A"),
                dropdown.Option("METROS"),
                dropdown.Option("DIAMETRO"),
                dropdown.Option("PESO"),
            ],
            autofocus=True,
            on_change= lambda e: print(e.control.value)  # Imprimir el resultado
        )

        self.mtrBobRefl = PopupMenuButton(
            Text("Metros de bobina al Refilarse"),
            bgcolor="white",
            menu_position=PopupMenuPosition.OVER,
            items=[ 
                PopupMenuItem(
                    content= Column(width=200,controls=[
                        Text("Metros"),
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

        self.dmtrBob_Tol = PopupMenuButton(
            Text("Diametro de Bobina y Tolerancia"),
            bgcolor="white",
            menu_position=PopupMenuPosition.OVER,
            items=[ 
                PopupMenuItem(
                    content= Column(width=200,controls=[
                        Text("Diametro Bobina "),
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

        self.mxEmplBob = TextField(
                label="Maximo de Empalmes por Bobina",
                border= InputBorder.OUTLINE,
                border_color="Black",
                label_style=TextStyle(color="Black",italic=True),
        )

    ### SECCIÓN 3 ###
        self.sñlEmplm = TextField(
                label="Señalización de Empalme",
                border= InputBorder.OUTLINE,
                border_color="Black",
                label_style=TextStyle(color="Black",italic=True),
        )

        self.orntBobTam = Dropdown(
            label="Orientación de Bobina en Tarima",
            hint_text="Proceso",
            options=[
                dropdown.Option("N/A"),
                dropdown.Option("HORIZONTAL"),
                dropdown.Option("VERTICAL"),
            ],
            autofocus=True,
            on_change= lambda e: print(e.control.value)  # Imprimir el resultado
        )

        self.tipEmpqBob = Dropdown(
            label="Tipo de Empaque para Bobina",
            hint_text="Proceso",
            options=[
                dropdown.Option("N/A"),
                dropdown.Option("EMPLAYE"),
                dropdown.Option("BOLSA"),
            ],
            autofocus=True,
            on_change= lambda e: print(e.control.value)  # Imprimir el resultado
        )

        self.psrPrdct = Dropdown(
            label="Pesar producto por : ",
            hint_text="Proceso",
            options=[
                dropdown.Option("N/A"),
                dropdown.Option("TARIMA"),
                dropdown.Option("BOBINA"),
                dropdown.Option("AMBAS"),
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
                        Text("Peso Neto "),
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

    ### SECCIÓN 4 ###
        self.etiquetado = Dropdown(
            label="Tipo de Empaque para Bobina",
            hint_text="Proceso",
            options=[
                dropdown.Option("N/A"),
                dropdown.Option("ROLLO INDIVIDUAL"),
                dropdown.Option("TARIMA"),
                dropdown.Option("AMBAS"),
            ],
            autofocus=True,
            on_change= lambda e: print(e.control.value)  # Imprimir el resultado
        )

        self.numBobCma_CmsTam = PopupMenuButton(
            Text("Numero de bobinas por cama y Camas por tarima"),
            bgcolor="white",
            menu_position=PopupMenuPosition.OVER,
            items=[ 
                PopupMenuItem(
                    content= Column(width=200,controls=[
                        Text("Bobinas por cama"),
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
                        Text("Camas por Tarima"),
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
                label="Numero de Bobinas en Tarima",
                border= InputBorder.OUTLINE,
                border_color="Black",
                label_style=TextStyle(color="Black",italic=True),
        )

        self.psPromTam = PopupMenuButton(
            Text("Peso neto promedio por tarima"),
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
            label="La tarima llevara Emplaye",
            hint_text="Emplaye",
            options=[
                dropdown.Option("N/A"),
                dropdown.Option("Aplica"),
            ],
            autofocus=True,
            on_change= lambda e: print(e.control.value)  # Imprimir el resultado
        )

        self.tamRefila = Dropdown(
            label="La tarima sera refilada",
            hint_text="Refilado",
            options=[
                dropdown.Option("N/A"),
                dropdown.Option("Aplica"),
            ],
            autofocus=True,
            on_change= lambda e: print(e.control.value)  # Imprimir el resultado
        )
