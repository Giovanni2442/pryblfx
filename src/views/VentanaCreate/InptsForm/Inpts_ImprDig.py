from flet import * 
from src.views.VentanaCreate.Verificaciones import verificaciones
from src.app.filExcel.filtroExcel import filter

class Inpst_ImprDig():
    def __init__(self,page):

        self.page = page
        self.valida = verificaciones(page)

    ### INPUTS DE LA TABLA IMPRECIÓN DIGITAL ###

    ### SECCIÓN 1 num : 9###
        self.mtrlImpr = TextField(
            label="Material Imprimir",
            border= InputBorder.OUTLINE,
            border_color="Black",
            value="N/A",
            error_text = "",
            label_style=TextStyle(color="Black",italic=True),
            on_change= lambda e: self.valida.verInpts(e,filter.vrfEstrcProd)      
        )

        self.dnjReq = TextField(
            label="Dinaje Requerido",
            border= InputBorder.OUTLINE,
            border_color="Black",
            value="N/A",
            error_text = "",
            label_style=TextStyle(color="Black",italic=True),
            on_change= lambda e: self.valida.verInpts(e,filter.vrfAny)      

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
                            label="Calibre",
                            border= InputBorder.OUTLINE,
                            #width=100,
                            border_color="black",
                            value='0',
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
                            value='0',
                            error_text = "",
                            label_style=TextStyle(color="Black",italic=True),
                            on_change= lambda e: self.valida.verInpts(e,filter.vrfIsNumber) 
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
                            label="Ancho",
                            border= InputBorder.OUTLINE,
                            #width=100,
                            border_color="black",
                            value='0',
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
                            value='0',
                            error_text = "",
                            label_style=TextStyle(color="Black",italic=True),
                            on_change= lambda e: self.valida.verInpts(e,filter.vrfIsNumber) 
                        )
                    ])
                ),
            ]
        )

        self.grosorCore = TextField(
            label="Grosor de Core",
            border= InputBorder.OUTLINE,
            border_color="Black",
            value='0',
            error_text = "",
            label_style=TextStyle(color="Black",italic=True),
            on_change= lambda e: self.valida.verInpts(e,filter.vrfIsNumber) 
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
                            label="Ancho",
                            border= InputBorder.OUTLINE,
                            #width=100,
                            border_color="black",
                            value='0',
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
                            value='0',
                            error_text = "",
                            label_style=TextStyle(color="Black",italic=True),
                            on_change= lambda e: self.valida.verInpts(e,filter.vrfIsNumber) 
                        )
                    ])
                ),
            ]
        )

        self.dsrImpr = TextField(
            label="Desarrollo a Imprimir",
            border= InputBorder.OUTLINE,
            border_color="Black",
            value='0',
            error_text = "",
            label_style=TextStyle(color="Black",italic=True),
            on_change= lambda e: self.valida.verInpts(e,filter.vrfIsNumber) 
        )
    
        self.repEje = TextField(
            label="Repeticiónes al Eje",
            border= InputBorder.OUTLINE,
            border_color="Black",
            value='0',
            error_text = "",
            label_style=TextStyle(color="Black",italic=True),
            on_change= lambda e: self.valida.verInpts(e,filter.vrfIsNumber) 
        )

        self.repDesr = TextField(
            label="Repeticiónes al Desarrollo",
            border= InputBorder.OUTLINE,
            border_color="Black",
            value='0',
            error_text = "",
            label_style=TextStyle(color="Black",italic=True),
            on_change= lambda e: self.valida.verInpts(e,filter.vrfIsNumber) 
        )
    ### SECCIÓN 2 num: 7 ###

        #Verificar esta entrada#
        self.cntTintasImpr = TextField(
            label="Cantidad de Tintas a Imprimir",
            border= InputBorder.OUTLINE,
            border_color="Black",
            value='0',
            error_text = "",
            label_style=TextStyle(color="Black",italic=True),
            on_change= lambda e: self.valida.verInpts(e,filter.vrfIsNumber) 
        )

        self.tipImpr = Dropdown(
            label="Tipo de Impresión",
            hint_text="Tipo",
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

        self.tipTintUtlzr = TextField(
            label="Tipo de Tinta a Utilizar",
            border= InputBorder.OUTLINE,
            border_color="Black",
            value="N/A",
            error_text = "",
            label_style=TextStyle(color="Black",italic=True),
            on_change= lambda e: self.valida.verInpts(e,filter.vrfAny) 
        )

        self.tipBrnzImpr = Dropdown(
            label="Tipo de Barniz",
            hint_text="Barniz",
            value="N/A",
            error_text = "",
            options=[
                dropdown.Option("N/A"),
                dropdown.Option("MATE"),
                dropdown.Option("BRILLANTE"),
            ],
            autofocus=True,
            #on_change= lambda e: print(e.control.value)  # Imprimir el resultado
        )
        # Figura de Embobinado al salir
        self.figEmbImpr = Dropdown(
            label="Figura de Embobinado",
            hint_text="Figura",
            value='0',
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
            on_change= lambda e: print(e.control.value)  # Imprimir el resultado
        )

        # --- REVISAR ESTA ENTRADA --
        self.vldClr = PopupMenuButton(
            Text("Validación de Color"),
            bgcolor="white",
            menu_position=PopupMenuPosition.OVER,
            items=[ 
                PopupMenuItem(
                    content= Column([
                        Text("Color"),
                        TextField(
                            label="Color",
                            border= InputBorder.OUTLINE,
                            border_color="Black",
                            value="N/A",
                            error_text = "",
                            label_style=TextStyle(color="Black",italic=True),
                            on_change= lambda e: self.valida.verInpts(e,filter.vrfAny) 
                        )
                    ])
                ),
                PopupMenuItem(
                    content= Column([
                        Text("Tolerancia en Deltas"),
                        TextField(
                            label="Tol. Deltas",
                            border= InputBorder.OUTLINE,
                            border_color="Black",
                            value="N/A",
                            error_text = "",
                            label_style=TextStyle(color="Black",italic=True),
                            on_change= lambda e: self.valida.verInpts(e,filter.vrfAny) 
                        )
                    ])
                ),
            ]
        )

        self.maxEmplmBob = TextField(
            label="Maximo Emplames por Bobina",
            border= InputBorder.OUTLINE,
            border_color="Black",
            value='0',
            error_text = "",
            label_style=TextStyle(color="Black",italic=True),
            on_change= lambda e: self.valida.verInpts(e,filter.vrfIsNumber) 
        )

        self.tipEmpqBob = Dropdown(
            label="Tipo de Barniz",
            hint_text="Barniz",
            value="N/A",
            error_text = "",
            options=[
                dropdown.Option("N/A"),
                dropdown.Option("BOLSA"),
                dropdown.Option("EMPLAYE"),
            ],
            autofocus=True,
            #on_change= lambda e: print(e.control.value)  # Imprimir el resultado
        )

        self.orntBobTam = Dropdown(
            label="Tipo de Barniz",
            hint_text="Barniz",
            value="N/A",
            error_text = "",
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

        self.dimtrBob_Tol = PopupMenuButton(
            Text("Diametro de Bobina y Tolerancia"),
            bgcolor="white",
            menu_position=PopupMenuPosition.OVER,
            items=[ 
                PopupMenuItem(
                    content= Column(width=200,controls=[
                        Text("Diametro Bobina"),
                        TextField(
                            label="Dinaje",
                            border= InputBorder.OUTLINE,
                            #width=100,
                            border_color="black",
                            value='0',
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
                            value='0',
                            error_text = "",
                            label_style=TextStyle(color="Black",italic=True),
                            on_change= lambda e: self.valida.verInpts(e,filter.vrfIsNumber) 
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
                            label="Peso",
                            border= InputBorder.OUTLINE,
                            #width=100,
                            border_color="black",
                            value='0',
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
                            value='0',
                            error_text = "",
                            label_style=TextStyle(color="Black",italic=True),
                            on_change= lambda e: self.valida.verInpts(e,filter.vrfIsNumber) 

                        )
                    ])
                ),
            ]
        )

        self.etiquetado = Dropdown(
            label="Etiquetado",
            hint_text="Etiquetado",
            value="N/A",
            error_text = "",
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
                            label="Bob. cama",
                            border= InputBorder.OUTLINE,
                            border_color="black",
                            value='0',
                            error_text = "",
                            label_style=TextStyle(color="black",italic=True),
                            on_change= lambda e: self.valida.verInpts(e,filter.vrfIsNumber) 
                        )
                    ])
                ),
                PopupMenuItem(
                    content= Column([
                        Text("Camas por Bobinas"),
                        TextField(
                            label="Camas Bob.",
                            border= InputBorder.OUTLINE,
                            border_color="Black",
                            value='0',
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
            value='0',
            error_text = "",
            label_style=TextStyle(color="Black",italic=True),
            on_change= lambda e: self.valida.verInpts(e,filter.vrfIsNumber) 
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
                            label="Peso",
                            border= InputBorder.OUTLINE,
                            border_color="black",
                            value='0',
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
                            value='0',
                            error_text = "",
                            label_style=TextStyle(color="Black",italic=True),
                        )
                    ])
                ),
            ]
        )

        self.tamEmply = Dropdown(
            label="La tarima llevara emplaye",
            hint_text="Emplaye",
            value="N/A",
            error_text = "",
            options=[
                dropdown.Option("N/A"),
                dropdown.Option("APLICA")
            ],
            autofocus=True,
            #on_change= lambda e: print(e.control.value)  # Imprimir el resultado
        )

        self.tamFlej = Dropdown(
            label="La tarima sera flejada",
            hint_text="Fleje",
            value="N/A",
            error_text = "",
            options=[
                dropdown.Option("N/A"),
                dropdown.Option("APLICA")
            ],
            autofocus=True,
            #on_change= lambda e: print(e.control.value)  # Imprimir el resultado
        )

    def tplInptsImprDig(self):
        return [
            self.mtrlImpr,
            self.dnjReq,
            self.grosorCore,
            self.dsrImpr,
            self.repEje,
            self.repDesr,
            self.cntTintasImpr,
            self.tipImpr,
            self.tipTintUtlzr,
            self.tipBrnzImpr,
            self.figEmbImpr,
            self.maxEmplmBob,
            self.tipEmpqBob,
            self.orntBobTam,
            self.psrPrdct,
            self.etiquetado,
            self.numBobTam,
            #self.vldClr,
            self.tamEmply,
            self.tamFlej,

            self.vldClr,
            self.calMtrlImpr_Tol,
            self.anchBobImpr_Tol,
            self.anchCore_Tol,
            self.dimtrBob_Tol,
            self.psPromBob,
            self.numBobCam_CamTam,
            self.psNtPromTam
        ]    

        


