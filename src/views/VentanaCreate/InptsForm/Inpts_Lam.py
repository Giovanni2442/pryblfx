from flet import * 
from src.views.VentanaCreate.Verificaciones import verificaciones
from src.app.filExcel.filtroExcel import filter
from src.views.VentanaCreate.InptsForm.InpstAux import InptsAux
from src.Controllers.appLam import appLam

class Inpts_Lam():
    def __init__(self,page):

        self.page = page
        self.valida = verificaciones(page)

        # -- ACTUALIZA SI ES INSERT O UPDATE --#
        self.aux = InptsAux
        self.dtaLam = appLam
    
        # ID PRODUCT UPDATE 
        self.id = self.page.client_storage.get("id")

        # QURY DATA FORM #
            # QUERY LAMINADO
        self.dtaGen = self.dtaLam().transctGetLamGen(self.id)
            # QUERY LAMINADO
        self.dtaLmns = self.dtaLam().transctGetLmns(self.id)
    
    ### INPUTS DE LAS TABLAS DE LAMINADO ###

    ### GENERAL ###
        self.estrcPrdct = TextField(            # GENERAL
            label="Estructura del Producto",
            border= InputBorder.OUTLINE,
            border_color="Black",
            #value="N/A",
            value=self.dataLamGen('N/A',1),
            error_text = "",
            label_style=TextStyle(color="Black",italic=True),
            on_change= lambda e: self.valida.verInpts(e,filter.vrfEstrcProd)     
        )

        self.medMngTransf = PopupMenuButton(    # GENERAL
            Text("Medida de la Manga para Transferencia",color=colors.WHITE),
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
                            #value='0',
                            value=self.dataLamGen('0.0',9),
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
                            label="tolerancia",
                            border= InputBorder.OUTLINE,
                            border_color="Black",
                            #value='0',
                            value=self.dataLamGen('0.0',10),
                            error_text = "",
                            label_style=TextStyle(color="Black",italic=True),
                            on_change= lambda e: self.valida.verInpts(e,filter.vrfIsNumber)
                        )
                    ])
                ),
            ]
        )

        self.anchCore_Tol = PopupMenuButton(    # GENERAL
            Text("Ancho de Core y Tolerancia",color=colors.WHITE),
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
                            #value='0',
                            value=self.dataLamGen('0.0',12),
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
                            label="tolerancia",
                            border= InputBorder.OUTLINE,
                            border_color="Black",
                            #value='0',
                            value=self.dataLamGen('0.0',13),
                            error_text = "",
                            label_style=TextStyle(color="Black",italic=True),
                            on_change= lambda e: self.valida.verInpts(e,filter.vrfIsNumber)
                        )
                    ])
                ),
            ]
        )

        self.dmtrGrsrCore = PopupMenuButton(    # GENERAL
            Text("Diametro y Grosor de Core",color=colors.WHITE),
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
                            #value='0',
                            value=self.dataLamGen('0.0',15),
                            error_text = "",
                            label_style=TextStyle(color="black",italic=True),
                            on_change= lambda e: self.valida.verInpts(e,filter.vrfIsNumber)
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
                            #value='0',
                            value=self.dataLamGen('0.0',16),
                            error_text = "",
                            label_style=TextStyle(color="Black",italic=True),
                            on_change= lambda e: self.valida.verInpts(e,filter.vrfIsNumber)
                        )
                    ])
                ),
            ]
        )

        self.dmtrBob_Tol = PopupMenuButton(     # GENERAL
            Text("Diametro de Bobina y Tolerancia",color=colors.WHITE),
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
                            #value='0',
                            value=self.dataLamGen('0.0',18),
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
                            label="tolerancia",
                            border= InputBorder.OUTLINE,
                            border_color="Black",
                            #value='0',
                            value=self.dataLamGen('0.0',19),
                            error_text = "",
                            label_style=TextStyle(color="Black",italic=True),
                            on_change= lambda e: self.valida.verInpts(e,filter.vrfIsNumber)
                        )
                    ])
                ),
            ]
        )

        self.mxmEmplBob = TextField(            # GENERAL
            label="Maximo de Empalmes por Bobina",
            border= InputBorder.OUTLINE,
            border_color="Black",
            #value='0',
            value=self.dataLamGen('0',2),
            error_text = "",
            label_style=TextStyle(color="Black",italic=True),
            on_change= lambda e: self.valida.verInpts(e,filter.vrfIsNumber)
        )

        self.orntBobRck = TextField(            # GENERAL
            label="Orientación de Bobina en Rack",
            border= InputBorder.OUTLINE,
            border_color="Black",
            #value="N/A",
            value=self.dataLamGen('N/A',3),
            error_text = "",
            label_style=TextStyle(color="Black",italic=True),
            on_change= lambda e: self.valida.verInpts(e,filter.vrfAny)
        )

        self.tipEmpqBob = TextField(            # GENERAL
            label="Tipo de Empaque para Bobina",
            border= InputBorder.OUTLINE,
            border_color="Black",
            #value="N/A",
            value=self.dataLamGen('N/A',4),
            error_text = "",
            label_style=TextStyle(color="Black",italic=True),
            on_change= lambda e: self.valida.verInpts(e,filter.vrfAny)
        )

        self.etiquetado = Dropdown(             # GENERAL
            label="Etiquetado",
            hint_text="etiquetado",
            #value="N/A",
            value=self.dataLamGen('N/A',5),
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
            #value="N/A",
            value=self.dataLamGen('N/A',6),
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
            #value="N/A",
            value=self.dataLamGen('N/A',7),
            error_text = "",
            label_style=TextStyle(color="Black",italic=True),
            on_change= lambda e: self.valida.verInpts(e,filter.vrfAny)
        )
    ##########################################################

    ###  MATERIAL IMPRESO ###

        self.mtlImpr = TextField(               # MatrImprs
            label="Material Impreso",
            border= InputBorder.OUTLINE,
            border_color="Black",
            #value="N/A",
            value=self.dataLamGen('N/A',21),
            error_text = "",
            label_style=TextStyle(color="Black",italic=True),
            on_change= lambda e: self.valida.verInpts(e,filter.vrfAny)
        )

        self.clPlc_Tol = PopupMenuButton(       # MatrImprs
            Text("Calibre de Pelicula y Tolerancia",color=colors.WHITE),
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
                            #value='0',
                            value=self.dataLamGen('0.0',24),
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
                            label="tolerancia",
                            border= InputBorder.OUTLINE,
                            border_color="Black",
                            #value='0',
                            value=self.dataLamGen('0.0',25),
                            error_text = "",
                            label_style=TextStyle(color="Black",italic=True),
                            on_change= lambda e: self.valida.verInpts(e,filter.vrfIsNumber)
                        )
                    ])
                ),
            ]
        )

        self.anchBob_Tol = PopupMenuButton(       # MatrImprs
            Text("Ancho de Bobina y Tolerancia",color=colors.WHITE),
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
                            #value='0',
                            value=self.dataLamGen('0.0',27),
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
                            label="tolerancia",
                            border= InputBorder.OUTLINE,
                            border_color="Black",
                            #value='0',
                            value=self.dataLamGen('0.0',28),
                            error_text = "",
                            label_style=TextStyle(color="Black",italic=True),
                            on_change= lambda e: self.valida.verInpts(e,filter.vrfIsNumber)
                        )
                    ])
                ),
            ]
        )
    
        self.tipTratado = Dropdown(             # MatrImprs
            label="Tratado : ",
            hint_text="tratado",
            #value="N/A",
            value=self.dataLamGen('N/A',22),
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
            #value="N/A",
            value=self.dataLamns('N/A',1),
            error_text = "",
            label_style=TextStyle(color="Black",italic=True),
            on_change= lambda e: self.valida.verInpts(e,filter.vrfEstrcProd)
        )

        self.LN1clbPel_Tol = PopupMenuButton(
            Text("Calibre de Pelicula y Tolerancia",color=colors.WHITE),
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
                            value=self.dataLamns('0.0',5),
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
                            label="tolerancia",
                            border= InputBorder.OUTLINE,
                            border_color="Black",
                            value=self.dataLamns('0.0',6),
                            error_text = "",
                            label_style=TextStyle(color="Black",italic=True),
                            on_change= lambda e: self.valida.verInpts(e,filter.vrfIsNumber)
                        )
                    ])
                ),
            ]
        )

        self.LN1anchBob_Tol = PopupMenuButton(
            Text("Ancho de Bobina y Tolerancia",color=colors.WHITE),
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
                            value=self.dataLamns('0.0',8),
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
                            value=self.dataLamns('0.0',9),
                            error_text = "",
                            label_style=TextStyle(color="Black",italic=True),
                            on_change= lambda e: self.valida.verInpts(e,filter.vrfIsNumber)
                        )
                    ])
                ),
            ]
        )

        self.LN1tipTratado = Dropdown(
            label="Tipo de Tratado",
            hint_text="etiquetado",
            #value="N/A",
            value=self.dataLamns('N/A',2),
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
            value=self.dataLamns('N/A',3),
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
            value=self.dataLamns('N/A',11),
            error_text = "",
            label_style=TextStyle(color="Black",italic=True),
            on_change= lambda e: self.valida.verInpts(e,filter.vrfEstrcProd)
        )

        self.LN2clbPel_Tol = PopupMenuButton(
            Text("Calibre de Pelicula y Tolerancia",color=colors.WHITE),
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
                            value=self.dataLamns('0.0',15),
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
                            label="N/A",
                            border= InputBorder.OUTLINE,
                            border_color="Black",
                            value=self.dataLamns('0.0',16),
                            error_text = "",
                            label_style=TextStyle(color="Black",italic=True),
                            on_change= lambda e: self.valida.verInpts(e,filter.vrfIsNumber)
                        )
                    ])
                ),
            ]
        )

        self.LN2anchBob_Tol = PopupMenuButton(
            Text("Ancho de Bobina y Tolerancia",color=colors.WHITE),
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
                            value=self.dataLamns('0.0',18),
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
                            value=self.dataLamns('0.0',19),
                            error_text = "",
                            label_style=TextStyle(color="Black",italic=True),
                            on_change= lambda e: self.valida.verInpts(e,filter.vrfIsNumber)
                        )
                    ])
                ),
            ]
        )

        self.LN2tipTratado = Dropdown(
            label="Tipo de Tratado",
            hint_text="etiquetado",
            value=self.dataLamns('N/A',12),
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
            value=self.dataLamns('N/A',13),
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
            value=self.dataLamns('N/A',21),
            error_text = "",
            label_style=TextStyle(color="Black",italic=True),
            on_change= lambda e: self.valida.verInpts(e,filter.vrfEstrcProd)
        )

        self.LN3clbPel_Tol = PopupMenuButton(
            Text("Calibre de Pelicula y Tolerancia",color=colors.WHITE),
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
                            value=self.dataLamns('0.0',25),
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
                            value=self.dataLamns('0.0',26),
                            error_text = "",
                            label_style=TextStyle(color="Black",italic=True),
                            on_change= lambda e: self.valida.verInpts(e,filter.vrfIsNumber)
                        )
                    ])
                ),
            ]
        )

        self.LN3anchBob_Tol = PopupMenuButton(
            Text("Ancho de Bobina y Tolerancia",color=colors.WHITE),
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
                            value=self.dataLamns('0.0',28),
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
                            value=self.dataLamns('0.0',29),
                            error_text = "",
                            label_style=TextStyle(color="Black",italic=True),
                            on_change= lambda e: self.valida.verInpts(e,filter.vrfIsNumber)
                        )
                    ])
                ),
            ]
        )

        self.LN3tipTratado = Dropdown(
            label="Tipo de Tratado",
            hint_text="etiquetado",
            value=self.dataLamns('N/A',22),
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
            value=self.dataLamns('N/A',23),
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
            value=self.dataLamns('N/A',31),
            error_text = "",
            label_style=TextStyle(color="Black",italic=True),
            on_change= lambda e: self.valida.verInpts(e,filter.vrfEstrcProd)
        )

        self.LN4clbPel_Tol = PopupMenuButton(
            Text("Calibre de Pelicula y Tolerancia",color=colors.WHITE),
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
                            value=self.dataLamns('0.0',35),
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
                            value=self.dataLamns('0.0',36),
                            error_text = "",
                            label_style=TextStyle(color="Black",italic=True),
                            on_change= lambda e: self.valida.verInpts(e,filter.vrfIsNumber)
                        )
                    ])
                ),
            ]
        )

        self.LN4anchBob_Tol = PopupMenuButton(
            Text("Ancho de Bobina y Tolerancia",color=colors.WHITE),
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
                            value=self.dataLamns('0.0',38),
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
                            value=self.dataLamns('0.0',39),
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
            value=self.dataLamns('N/A',32),
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
            value=self.dataLamns('N/A',33),
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

    # GET LAM
    def dataLamGen(self,default_value,Indx):
    #def dataLamGen(self,default_value):
        if self.id != "Insert":
            #print(self.dtaGen)                  
            #return self.dtaGen[Indx]
            return f"{Indx}"
        else:
            return default_value
        
    def dataLamns(self,default_value,Indx):
    #def dataLamns(self,default_value):
        if self.id != "Insert":                  
            #print(self.dtaLmns)
            #return self.dtaLmns[Indx]
            return f"{Indx}"
        else:
            return default_value


    def tplInptsLam(self):
        return [
            self.estrcPrdct,
            self.mxmEmplBob,
            self.orntBobRck,
            self.tipEmpqBob,
            self.etiquetado,
            self.psrPrdct,
            self.psNtPromBob, # 6

            self.medMngTransf,
            self.anchCore_Tol,
            self.dmtrGrsrCore,
            self.dmtrBob_Tol, # 10

            [   # --- MATERIAL IMPRESO --- # 11
                self.mtlImpr,
                self.tipTratado,
                self.clPlc_Tol,
                self.anchBob_Tol, # 14
            ],

            [   # --- LAMINAR 1 --- #        12
                self.LN1mtrLam,
                self.LN1tipTratado,
                self.LN1tipLam,
                self.LN1clbPel_Tol,
                self.LN1anchBob_Tol, # 19
            ],

            [   # --- LAMINAR 2 --- #          13
                self.LN2mtrLam,
                self.LN2tipTratado,
                self.LN2tipLam,
                self.LN2clbPel_Tol,
                self.LN2anchBob_Tol, # 24
            ],

            [   # --- LAMINAR 3 --- #           14
                self.LN3mtrLam,
                self.LN3tipTratado,
                self.LN3tipLam,
                self.LN3clbPel_Tol,
                self.LN3anchBob_Tol, # 29
            ],

            [   # --- LAMINAR 4 --- #           15
                self.LN4mtrLam,
                self.LN4tipTratado,
                self.LN4tipLam,
                self.LN4clbPel_Tol,
                self.LN4anchBob_Tol, # 34
            ]

        ]





