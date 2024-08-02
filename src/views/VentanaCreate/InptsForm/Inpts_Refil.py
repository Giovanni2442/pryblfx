from flet import *
from src.views.VentanaCreate.Verificaciones import verificaciones
from src.app.filExcel.filtroExcel import filter

class Inpts_Refil():
    def __init__(self,page):
        self.page = page
        self.valida = verificaciones(page)

    ### INPUTS DE LA TABLA REFILADO ###

    ### SESSIÓN 1 ###
        self.procRef = Dropdown(
            label="Proceso Refilado",
            hint_text="Proceso",
            value="N/A",
            error_text = "",
            options=[
                dropdown.Option("N/A"),
                dropdown.Option("DOBLADO"),
                dropdown.Option("REFILADO"),
                dropdown.Option("AMBOS"),
            ],
            autofocus=True,
            #on_change= lambda e: print(e.control.value)  # Imprimir el resultado
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
                            label="Ancho",
                            border= InputBorder.OUTLINE,
                            #width=100,
                            border_color="black",
                            value=0,
                            error_text = "",
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
                            value=0,
                            error_text = "",
                            label_style=TextStyle(color="Black",italic=True),
                            on_change= lambda e: self.valida.verInpts(e,filter.vrfIsNumber)
                        )
                    ])
                ),
            ]
        )

        self.acabdBob = Dropdown(
            label="Proceso Refilado",
            hint_text="Proceso",
            value="N/A",
            error_text = "",
            options=[
                dropdown.Option("N/A"),
                dropdown.Option("COMERCIAL"),
                dropdown.Option("ESPEJO"),
            ],
            autofocus=True,
            #on_change= lambda e: print(e.control.value)  # Imprimir el resultado
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
                            label="Ancho",
                            border= InputBorder.OUTLINE,
                            #width=100,
                            border_color="black",
                            value=0,
                            error_text = "",
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
                            value=0,
                            error_text = "",
                            label_style=TextStyle(color="Black",italic=True),
                            on_change= lambda e: self.valida.verInpts(e,filter.vrfIsNumber)
                        )
                    ])
                ),
            ]
        )
        
        self.grsrCore = TextField(
                label="Grosor de Core",
                border= InputBorder.OUTLINE,
                border_color="Black",
                value="N/A",
                error_text = "",
                label_style=TextStyle(color="Black",italic=True),
                on_change= lambda e: self.valida.verInpts(e,filter.vrfAny)
        )

    ### SECCIÓN 2 ###
        self.figEmb = Dropdown(
            label="Figura de Embobinado",
            hint_text="Figura",
            value=0,
            error_text = "",
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
            #on_change= lambda e: print(e.control.value)  # Imprimir el resultado
        )

        self.bobRef_Dbl = Dropdown(
            label="La bobina se Refilira / Doblara",
            hint_text="Proceso",
            value="N/A",
            error_text = "",
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
                            label="metros",
                            border= InputBorder.OUTLINE,
                            #width=100,
                            border_color="black",
                            value=0,
                            error_text = "",
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
                            value=0,
                            error_text = "",
                            label_style=TextStyle(color="Black",italic=True),
                            on_change= lambda e: self.valida.verInpts(e,filter.vrfIsNumber)
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
                            label="Diametro",
                            border= InputBorder.OUTLINE,
                            #width=100,
                            border_color="black",
                            value=0,
                            error_text = "",
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
                            value=0,
                            error_text = "",
                            label_style=TextStyle(color="Black",italic=True),
                            on_change= lambda e: self.valida.verInpts(e,filter.vrfIsNumber)
                        )
                    ])
                ),
            ]
        )

        self.mxEmplBob = TextField(
                label="Maximo de Empalmes por Bobina",
                border= InputBorder.OUTLINE,
                border_color="Black",
                value=0,
                error_text = "",
                label_style=TextStyle(color="Black",italic=True),
                on_change= lambda e: self.valida.verInpts(e,filter.vrfIsNumber)
        )

    ### SECCIÓN 3 ###


        self.sñlEmplm = TextField(
                label="Señalización de Empalme",
                border= InputBorder.OUTLINE,
                border_color="Black",
                value="N/A",
                error_text = "",
                label_style=TextStyle(color="Black",italic=True),
                on_change= lambda e: self.valida.verInpts(e,filter.vrfAny)
        )

        self.orntBobTam = Dropdown(
            label="Orientación de Bobina en Tarima",
            hint_text="Proceso",
            value="N/A",
            error_text = "",
            options=[
                dropdown.Option("N/A"),
                dropdown.Option("HORIZONTAL"),
                dropdown.Option("VERTICAL"),
            ],
            autofocus=True,
            #on_change= lambda e: print(e.control.value)  # Imprimir el resultado
        )

        self.tipEmpqBob = Dropdown(
            label="Tipo de Empaque para Bobina",
            hint_text="Proceso",
            value="N/A",
            error_text = "",
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
            value="N/A",
            error_text = "",
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
                            label="Peso",
                            border= InputBorder.OUTLINE,
                            #width=100,
                            border_color="black",
                            value=0,
                            error_text = "",
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
                            value=0,
                            error_text = "",
                            label_style=TextStyle(color="Black",italic=True),
                            on_change= lambda e: self.valida.verInpts(e,filter.vrfIsNumber)
                        )
                    ])
                ),
            ]
        )

        self.anchFnlBob_Tol = PopupMenuButton(
            Text("Ancho final de Bobina y Tol."),
            bgcolor="white",
            menu_position=PopupMenuPosition.OVER,
            items=[ 
                PopupMenuItem(
                    content= Column(width=200,controls=[
                        Text("Ancho Final"),
                        TextField(
                            label="Ancho",
                            border= InputBorder.OUTLINE,
                            #width=100,
                            border_color="black",
                            value=0,
                            error_text = "",
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
                            value=0,
                            error_text = "",
                            label_style=TextStyle(color="Black",italic=True),
                            on_change= lambda e: self.valida.verInpts(e,filter.vrfIsNumber)
                        )
                    ])
                ),
            ]
        )

    ### SECCIÓN 4 ###
        self.etiquetado = Dropdown(
            label="Tipo de Empaque para Bobina",
            hint_text="Proceso",
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

        self.numBobCma_CmsTam = PopupMenuButton(
            Text("Numero de bobinas por cama y Camas por tarima"),
            bgcolor="white",
            menu_position=PopupMenuPosition.OVER,
            items=[ 
                PopupMenuItem(
                    content= Column(width=200,controls=[
                        Text("Bobinas por cama"),
                        TextField(
                            label="bob. cama",
                            border= InputBorder.OUTLINE,
                            #width=100,
                            border_color="black",
                            value=0,
                            error_text = "",
                            label_style=TextStyle(color="black",italic=True),
                            on_change= lambda e: self.valida.verInpts(e,filter.vrfIsNumber)
                        )
                    ])
                ),
                PopupMenuItem(
                    content= Column([
                        Text("Camas por Tarima"),
                        TextField(
                            label="camas tarm.",
                            border= InputBorder.OUTLINE,
                            border_color="Black",
                            value=0,
                            error_text = "",
                            label_style=TextStyle(color="Black",italic=True),
                            on_change= lambda e: self.valida.verInpts(e,filter.vrfIsNumber)
                        )
                    ])
                ),
            ]
        )

        self.numBobTam = TextField(
                label="Numero de Bobinas en Tarima",
                border= InputBorder.OUTLINE,
                border_color="Black",
                value="N/A",
                error_text = "",
                label_style=TextStyle(color="Black",italic=True),
                on_change= lambda e: self.valida.verInpts(e,filter.vrfAny)
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
                            label="Peso",
                            border= InputBorder.OUTLINE,
                            #width=100,
                            border_color="black",
                            value=0,
                            error_text = "",
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
                            value=0,
                            error_text = "",
                            label_style=TextStyle(color="Black",italic=True),
                            on_change= lambda e: self.valida.verInpts(e,filter.vrfIsNumber)
                        )
                    ])
                ),
            ]
        )

        self.tamEmplaye = Dropdown(
            label="La tarima llevara Emplaye",
            hint_text="Emplaye",
            value="N/A",
            error_text = "",
            options=[
                dropdown.Option("N/A"),
                dropdown.Option("Aplica"),
            ],
            autofocus=True,
            #on_change= lambda e: print(e.control.value)  # Imprimir el resultado
        )

        self.tamflejada = Dropdown(
            label="La tarima sera flejada",
            hint_text="Flejada",
            value="N/A",
            error_text = "",
            options=[
                dropdown.Option("N/A"),
                dropdown.Option("Aplica"),
            ],
            autofocus=True,
            #on_change= lambda e: print(e.control.value)  # Imprimir el resultado
        )

    def tplInptsRef(self):
        return [
            self.procRef,       # Principal
            self.acabdBob,
            self.grsrCore,
            self.figEmb,
            self.bobRef_Dbl,
            self.mxEmplBob,
            self.sñlEmplm,
            self.orntBobTam,
            self.tipEmpqBob,
            self.psrPrdct,
            self.etiquetado,
            self.tamEmplaye,
            self.tamflejada,

            self.anchFnlBob_Tol,
            self.mtrBobRefl,
            self.dmtrBob_Tol,
            self.psPromBob,
            self.numBobCma_CmsTam,
            self.psPromTam,
        ]