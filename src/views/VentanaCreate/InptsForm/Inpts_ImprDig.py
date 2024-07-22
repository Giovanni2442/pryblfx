from flet import * 
from src.views.VentanaCreate.Verificaciones import verificaciones
from src.app.filExcel.filtroExcel import filter

class Inpst_ImprDig():
    def __init__(self,page):
        super().__init__()

    ### INPUTS DE LA TABLA IMPRECIÓN DIGITAL ###

    ### SECCIÓN 1 num : 9###
        self.mtrlImpr = TextField(
            label="Material Imprimir",
            border= InputBorder.OUTLINE,
            border_color="Black",
            label_style=TextStyle(color="Black",italic=True),
        )

        self.dnjReq = TextField(
            label="Dinaje Requerido",
            border= InputBorder.OUTLINE,
            border_color="Black",
            label_style=TextStyle(color="Black",italic=True),
        )

        self.calMtrlImpr_Tol = PopupMenuButton(
            Text("Calibre de Material a Imprimir y Tolerancia"),
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

        self.anchBobImpr_Tol = PopupMenuButton(
            Text("Ancho de Bobina a Imprimir y Tolerancia"),
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

        self.grosorCore = TextField(
            label="Grosor de Core",
            border= InputBorder.OUTLINE,
            border_color="Black",
            label_style=TextStyle(color="Black",italic=True),
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

        self.dsrImpr = TextField(
            label="Desarrollo a Imprimir",
            border= InputBorder.OUTLINE,
            border_color="Black",
            label_style=TextStyle(color="Black",italic=True),
        )
    
        self.repEje = TextField(
            label="Repeticiónes al Eje",
            border= InputBorder.OUTLINE,
            border_color="Black",
            label_style=TextStyle(color="Black",italic=True),
        )

        self.repDesr = TextField(
            label="Repeticiónes al Desarrollo",
            border= InputBorder.OUTLINE,
            border_color="Black",
            label_style=TextStyle(color="Black",italic=True),
        )
    ### SECCIÓN 2 num: 7 ###

        #Verificar esta entrada#
        self.cntTintasImpr = TextField(
            label="Cantidad de Tintas a Imprimir",
            border= InputBorder.OUTLINE,
            border_color="Black",
            label_style=TextStyle(color="Black",italic=True),
        )

        self.tipImpr = Dropdown(
            label="Tipo de Impresión",
            hint_text="Tipo",
            options=[
                dropdown.Option("N/A"),
                dropdown.Option("INTERNA"),
                dropdown.Option("EXTERNA"),
            ],
            autofocus=True,
            on_change= lambda e: print(e.control.value)  # Imprimir el resultado
        )

        self.tipTintUtlzr = TextField(
            label="Tipo de Tinta a Utilizar",
            border= InputBorder.OUTLINE,
            border_color="Black",
            label_style=TextStyle(color="Black",italic=True),
        )

        self.tipBrnzImpr = Dropdown(
            label="Tipo de Barniz",
            hint_text="Barniz",
            options=[
                dropdown.Option("N/A"),
                dropdown.Option("MATE"),
                dropdown.Option("BRILLANTE"),
            ],
            autofocus=True,
            on_change= lambda e: print(e.control.value)  # Imprimir el resultado
        )
        # Figura de Embobinado al salir
        self.figEmbImpr = Dropdown(
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

        self.vldClr = PopupMenuButton(
            Text("Validación de Color"),
            bgcolor="white",
            menu_position=PopupMenuPosition.OVER,
            items=[ 
                PopupMenuItem(
                    content= Dropdown(
                        label="Color",
                        hint_text="Color",
                        options=[
                            dropdown.Option("N/A"),
                            dropdown.Option("MATE"),
                            dropdown.Option("BRILLANTE"),
                        ],
                        autofocus=True,
                        on_change= lambda e: print(e.control.value)  # Imprimir el resultado
                    )
                ),
                PopupMenuItem(
                    content= Column([
                        Text("Tolerancia en Deltas"),
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

        self.maxEmplmBob = TextField(
            label="Maximo Emplames por Bobina",
            border= InputBorder.OUTLINE,
            border_color="Black",
            label_style=TextStyle(color="Black",italic=True),
        )

        self.tipEmpqBob = Dropdown(
            label="Tipo de Barniz",
            hint_text="Barniz",
            options=[
                dropdown.Option("N/A"),
                dropdown.Option("BOLSA"),
                dropdown.Option("EMPLAYE"),
            ],
            autofocus=True,
            on_change= lambda e: print(e.control.value)  # Imprimir el resultado
        )

        self.orntBobTam = Dropdown(
            label="Tipo de Barniz",
            hint_text="Barniz",
            options=[
                dropdown.Option("N/A"),
                dropdown.Option("HORIZONTAL"),
                dropdown.Option("VERTICAL"),
            ],
            autofocus=True,
            on_change= lambda e: print(e.control.value)  # Imprimir el resultado
        )
    
    ### SECCIÓN 3 num: 6 ###
        #Verificar el Dropdown
        
        self.psrPrdct = Dropdown(
            label="Tipo de Barniz",
            hint_text="Barniz",
            options=[
                dropdown.Option("N/A"),
                dropdown.Option("TARIMA"),
                dropdown.Option("BOBINA"),
                dropdown.Option("AMBAS"),
            ],
            autofocus=True,
            on_change= lambda e: print(e.control.value)  # Imprimir el resultado
        )

        self.dimtrBob_Tol = PopupMenuButton(
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

        self.psPromBob = PopupMenuButton(
            Text("Peso Neto Promedio de Bobina"),
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

        self.etiquetado = Dropdown(
            label="Etiquetado",
            hint_text="Etiquetado",
            options=[
                dropdown.Option("N/A"),
                dropdown.Option("ROLLO INDIVIDUAL"),
                dropdown.Option("TARIMA"),
                dropdown.Option("AMBAS"),
            ],
            autofocus=True,
            on_change= lambda e: print(e.control.value)  # Imprimir el resultado
        )

        self.numBobCam_CamTam = PopupMenuButton(
            Text("Numero de Bobinas por Camas y Camas por Tarima"),
            bgcolor="white",
            menu_position=PopupMenuPosition.OVER,
            items=[ 
                PopupMenuItem(
                    content= Column(width=200,controls=[
                        Text("Bobinas por Cama"),
                        TextField(
                            label="N/A",
                            border= InputBorder.OUTLINE,
                            border_color="black",
                            label_style=TextStyle(color="black",italic=True),
                        )
                    ])
                ),
                PopupMenuItem(
                    content= Column([
                        Text("Camas por Bobinas"),
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

        self.psNtPromTam = PopupMenuButton(
            Text("Peso Neto Promedio por Tarima"),
            bgcolor="white",
            menu_position=PopupMenuPosition.OVER,
            items=[ 
                PopupMenuItem(
                    content= Column(width=200,controls=[
                        Text("Peso"),
                        TextField(
                            label="N/A",
                            border= InputBorder.OUTLINE,
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

        self.tamEmply = Dropdown(
            label="La tarima llevara emplaye",
            hint_text="Emplaye",
            options=[
                dropdown.Option("N/A"),
                dropdown.Option("APLICA")
            ],
            autofocus=True,
            on_change= lambda e: print(e.control.value)  # Imprimir el resultado
        )

        self.tamFlej = Dropdown(
            label="La tarima sera flejada",
            hint_text="Fleje",
            options=[
                dropdown.Option("N/A"),
                dropdown.Option("APLICA")
            ],
            autofocus=True,
            on_change= lambda e: print(e.control.value)  # Imprimir el resultado
        )



        


