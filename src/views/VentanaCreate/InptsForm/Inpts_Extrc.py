from flet import * 
from src.views.VentanaCreate.Verificaciones import verificaciones
from src.app.filExcel.filtroExcel import filter


class InptsExtrc():
    def __init__(self,page):
        super().__init__()

        self.page = page
        self.valida = verificaciones(page)

        ### INPUTS DE TABLA EXTRUCIÓN ###
        # on_change= lambda e: print(e.control.value)  # Imprimir el resultado

        ### SECCIÓN 1 ##

        self.tipMtrlExtr = Dropdown(               # Tipo de material a Extruir
            label="Material a Extruir",
            hint_text="Producto Laminado",
            value="N/A",
            error_text = "",
            options=[
                dropdown.Option("N/A"),
                dropdown.Option("LDPE"),
                dropdown.Option("HDPE"),
            ],
            autofocus=True,
        )

        self.dinajeReq = TextField(                 # Dinaje requerido
            label="Dinaje",                         
            border= InputBorder.OUTLINE,
            border_color="Black",
            value="N/A",
            error_text= "",
            label_style=TextStyle(color="Black",italic=True),
            on_change= lambda e: self.valida.verInpts(e,filter.vrfAny)
        )

        self.frmlExtr = TextField(                  # Formula que se Extruira la Bobina
            label="Formula Extrusión",
            border= InputBorder.OUTLINE,
            border_color="Black",
            value="N/A",
            error_text= "",
            label_style=TextStyle(color="Black",italic=True),
            on_change= lambda e: self.valida.verInpts(e,filter.vrfFrml)
        )

        self.pigmPelc = TextField(                  # Pigmento de Pelicula
            label="Pigmento",
            border= InputBorder.OUTLINE,
            border_color="Black",
            value="N/A",
            error_text= "",
            label_style=TextStyle(color="Black",italic=True),
            on_change= lambda e: self.valida.verInpts(e,filter.vrfAny)
        )
    
        self.tipBob = Dropdown(                     # Tipo de Bobina
            label="Tipo de bobina",
            hint_text="Producto Laminado",
            value="N/A",
            error_text = "",
            options=[
                dropdown.Option("N/A"),
                dropdown.Option("Lamina"),
                dropdown.Option("Tabular Abierta"),
            ],
            autofocus=True,
            #on_change= lambda e: print(e.control.value)  # Imprimir el resultado
        )

        self.calPel_Tol = PopupMenuButton(         # Calibre de pelicula y tolerancia
            Text("Calibre de pelicula y tolerancia"),
            bgcolor="red",
            #padding=10,
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
                            value = '0',
                            error_text= "",
                            label_style=TextStyle(color="black",italic=True),
                            on_change= lambda e: self.valida.verInpts(e,filter.vrfIsNumber)
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
                            value = '0',
                            error_text= "",
                            label_style=TextStyle(color="Black",italic=True),
                            on_change= lambda e: self.valida.verInpts(e,filter.vrfIsNumber)

                        )
                    ])
                ),
            ]
        )

        self.tipTratado =  Dropdown(                # Tipo de tratado
            label="Tipo de tratado",
            hint_text="Producto Laminado",
            error_text = "",
            value="N/A",
            options=[
                dropdown.Option("N/A"),
                dropdown.Option("Seccionado"),
                dropdown.Option("Una cara"),
                dropdown.Option("Ambas caras"),
                dropdown.Option("Sin tratado"),
            ],
            autofocus=True,
            #on_change= lambda e: print(e.control.value)  # Imprimir el resultado
        )
        #####################

        #GestureDetector(),
        ### SECCION 2 ###
        self.anchBob_Tol = PopupMenuButton(         # Ancho de Bobina y Tolerancia
            Text("Ancho de Bobina y Tolerancia!"),
            bgcolor="red",
            #padding=10,
            menu_position=PopupMenuPosition.OVER,
            items=[ 
                PopupMenuItem(
                    content= Column(width=200,controls=[
                        Text("Ancho de bobina"),
                        TextField(
                            label="Ancho de bobina",
                            border= InputBorder.OUTLINE,
                            #width=100,
                            border_color="black",
                            value = "0",
                            error_text= "",
                            label_style=TextStyle(color="black",italic=True),
                            on_change= lambda e: self.valida.verInpts(e,filter.vrfIsNumber)
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
                            value = "0",
                            error_text= "",
                            label_style=TextStyle(color="Black",italic=True),
                            on_change= lambda e: self.valida.verInpts(e,filter.vrfIsNumber)

                        )
                    ])
                ),
            ]
        )

        self.anchCore_Tol = PopupMenuButton(        # Ancho de core y Tolerancia
            Text("Ancho de Core y Tolerancia"),
            bgcolor="white",
            menu_position=PopupMenuPosition.OVER,
            items=[ 
                PopupMenuItem(
                    content= Column(width=200,controls=[
                        Text("Ancho de Core"),
                        TextField(
                            label="core",
                            border= InputBorder.OUTLINE,
                            #width=100,
                            border_color="black",
                            value = "0",
                            error_text= "",
                            label_style=TextStyle(color="black",italic=True),
                            on_change= lambda e: self.valida.verInpts(e,filter.vrfIsNumber)
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
                            value = "0",
                            error_text= "",
                            label_style=TextStyle(color="Black",italic=True),
                            on_change= lambda e: self.valida.verInpts(e,filter.vrfIsNumber)
                        )
                    ])
                ),
            ]
        )

        self.maxEmplBob = TextField(                # Maximo de Empalmes por bobina
            label="Empalmes",
            border= InputBorder.OUTLINE,
            border_color="Black",
            value = '0',
            error_text= "",
            label_style=TextStyle(color="Black",italic=True),
            on_change= lambda e: self.valida.verInpts(e,filter.vrfIsNumber)
        )

        self.orntBobTam = Dropdown(                 # Orientación de bobina en tarima 
            label="Orientación",
            hint_text="Orientación de Bobina",
            value = "N/A",
            error_text = "",
            options=[
                dropdown.Option("N/A"),
                dropdown.Option("Horizontal"),
                dropdown.Option("Vertical"),
            ],
            autofocus=True,
            #on_change= lambda e: print(e.control.value)  # Imprimir el resultado
        )

        self.tipEmpqBob = Dropdown(                 # Tipo de empaque para bobina
            label="Empaque",
            hint_text="Tipo de Empaque",
            value = "N/A",
            error_text = "",
            options=[
                dropdown.Option("N/A"),
                dropdown.Option("Emplaye"),
                dropdown.Option("Bolsa"),
            ],
            autofocus=True,
           # on_change= lambda e: print(e.control.value)  # Imprimir el resultado
        )

        self.psrPrdct = Dropdown(                   # Pesar producto por
            label="Pesar por..",
            hint_text="Pesar producto",
            value = "N/A",
            error_text = "",
            options=[
                dropdown.Option("N/A"),
                dropdown.Option("Tarima"),
                dropdown.Option("Bobina"),
                dropdown.Option("Ambos")
            ],
            autofocus=True,
            #on_change= lambda e: print(e.control.value)  # Imprimir el resultado
        )
    
        self.psPromBob = PopupMenuButton(           # Peso neto promedio de bobina
            Text("Peso neto Promedio de Bobina"),
            bgcolor="white",
            menu_position=PopupMenuPosition.OVER,
            items=[ 
                PopupMenuItem(
                    content= Column(width=200,controls=[
                        Text("Peso Neto"),
                        TextField(
                            label="Peso neto",
                            border= InputBorder.OUTLINE,
                            #width=100,
                            border_color="black",
                            value = "0",
                            error_text= "",
                            label_style=TextStyle(color="black",italic=True),
                            on_change= lambda e: self.valida.verInpts(e,filter.vrfIsNumber)
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
                            value = "0",
                            error_text= "",
                            label_style=TextStyle(color="Black",italic=True),
                            on_change= lambda e: self.valida.verInpts(e,filter.vrfIsNumber)
                        )
                    ])
                ),
            ]
        )
    
        ################################
    
        ### SECCIÓN 3 ###
        self.DimBob_Tol = PopupMenuButton(          # Diametro de Bobina y Tolerancia
            Text("Diametro de Bobina y Tolerancia"),
            bgcolor="white",
            menu_position=PopupMenuPosition.OVER,
            items=[ 
                PopupMenuItem(
                    content= Column(width=200,controls=[
                        Text("Diametro de Bobina"),
                        TextField(
                            label="Diametro de Bobina",
                            border= InputBorder.OUTLINE,
                            #width=100,
                            border_color="black",
                            value = "0",
                            error_text= "",
                            label_style=TextStyle(color="black",italic=True),
                            on_change= lambda e: self.valida.verInpts(e,filter.vrfIsNumber)
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
                            value = "0",
                            error_text= "",
                            label_style=TextStyle(color="Black",italic=True),
                            on_change= lambda e: self.valida.verInpts(e,filter.vrfIsNumber)
                        )
                    ])
                ),
            ]
        )

        self.etiquetado = Dropdown(                 # Etiquetado
            label="etiquetado",
            hint_text="etiquetado",
            value= "N/A",
            error_text = "",
            options=[
                dropdown.Option("N/A"),
                dropdown.Option("Rollo Individual"),
                dropdown.Option("Tarima"),
                dropdown.Option("Ambos")
            ],
            autofocus=True,
            #on_change= lambda e: print(e.control.value)  # Imprimir el resultado
        )

        self.numBobCma_CmaTrm = PopupMenuButton(    # Num bob X cama y cama X Tam
            Text("Numero de Bobinas por Cama y Camas por Tarima"),
            bgcolor="white",
            menu_position=PopupMenuPosition.OVER,
            items=[ 
                PopupMenuItem(
                    content= Column(width=200,controls=[
                        Text("Bobinas por Cama"),
                        TextField(
                            label="Bobinas por Cama",
                            border= InputBorder.OUTLINE,
                            #width=100,
                            border_color="black",
                            value = "0",
                            error_text= "",
                            label_style=TextStyle(color="black",italic=True),
                            on_change= lambda e: self.valida.verInpts(e,filter.vrfIsNumber)
                        )
                    ])
                ),
                PopupMenuItem(
                    content= Column([
                        Text("Camas por Bobina"),
                        TextField(
                            label="CamasBobina",
                            border= InputBorder.OUTLINE,
                            border_color="Black",
                            value = "0",
                            error_text= "",
                            label_style=TextStyle(color="Black",italic=True),
                            on_change= lambda e: self.valida.verInpts(e,filter.vrfIsNumber)
                        )
                    ])
                ),
            ]
        )

        self.numBobTam = TextField(                 # Num bob en Tarima
            label="Ingresar Numero de Bobinas",
            border= InputBorder.OUTLINE,
            border_color="Black",
            value = '0',
            error_text= "",
            label_style=TextStyle(color="Black",italic=True),
            on_change= lambda e: self.valida.verInpts(e,filter.vrfIsNumber)
        )

        self.psNtPromTam = PopupMenuButton(         # Peso neto Promedio por Tarima
            Text("Peso neto Promedio por Tarima"),  
            bgcolor="white",
            menu_position=PopupMenuPosition.OVER,
            items=[ 
                PopupMenuItem(
                    content= Column(width=200,controls=[
                        Text("Peso"),
                        TextField(
                            label="Peso",
                            border= InputBorder.OUTLINE,
                            #width=100,
                            border_color="black",
                            value = "0",
                            error_text= "",
                            label_style=TextStyle(color="black",italic=True),
                            on_change= lambda e: self.valida.verInpts(e,filter.vrfIsNumber)
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
                            value = "0",
                            error_text= "",
                            label_style=TextStyle(color="Black",italic=True),
                            on_change= lambda e: self.valida.verInpts(e,filter.vrfIsNumber)
                        )
                    ])
                ),
            ]
        )

        self.tamEmplaye = Dropdown(                 # LA TARIMA LLEVARA EMPLAYE
            label="Lleva Emplaye : ",
            hint_text="Emplaye",
            value = "N/A",
            error_text = "",
            options=[
                dropdown.Option("N/A"),
                dropdown.Option("Aplica"),
            ],
            autofocus=True,
            #on_change= lambda e: print(e.control.value)  # Imprimir el resultado
        )

        self.tamRefila = Dropdown(                  # LA TARIMA SERA FLEJADA
            label="Sera refilada : ",
            hint_text="Refilado",
            value = "N/A",
            error_text = "",
            options=[
                dropdown.Option("N/A"),
                dropdown.Option("Aplica"),
            ],
            autofocus=True,
            #on_change= lambda e: print(e.control.value)  # Imprimir el resultado
        )

    def tplInptsExtr(self):
        return [
            self.tipMtrlExtr,   # SECCIÓN 1
            self.dinajeReq,
            self.frmlExtr,
            self.pigmPelc,
            self.tipBob,
            self.tipTratado,
            self.maxEmplBob,
            self.orntBobTam,
            self.tipEmpqBob,
            self.psrPrdct,
            self.etiquetado,
            self.numBobTam,
            self.tamEmplaye,
            self.tamRefila, # 12
            

            self.calPel_Tol,
            self.anchBob_Tol,   # SECCIÓN 2
            self.anchCore_Tol,
            self.DimBob_Tol,     # SECCIÓN 3
            self.psPromBob, 
            self.numBobCma_CmaTrm,
            self.psNtPromTam, # 20
        ]