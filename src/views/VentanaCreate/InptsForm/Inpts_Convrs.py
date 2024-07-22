from flet import *
from src.views.VentanaCreate.Verificaciones import verificaciones
from src.app.filExcel.filtroExcel import filter

class Inpts_Convrs():
    def __init__(self,page):
        super().__init__()

    ### INPUTS DE LA TABLA CONVERSIÓN ###

    ### SESSIÓN 1 ###

        self.medEmpq = PopupMenuButton(
            Text("Medida del Empaque"),
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
                        Text("Alto"),
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

        self.tipEmpq = TextField(
                label="Tipo de Empaque",
                border= InputBorder.OUTLINE,
                border_color="Black",
                label_style=TextStyle(color="Black",italic=True),
        )

        self.tipSello = TextField(
                label="Tipo de Sello",
                border= InputBorder.OUTLINE,
                border_color="Black",
                label_style=TextStyle(color="Black",italic=True),
        )

        self.tipAcbd = TextField(
                label="Tipo de Acabado",
                border= InputBorder.OUTLINE,
                border_color="Black",
                label_style=TextStyle(color="Black",italic=True),
        )

        self.prdctPerf = Dropdown(
            label="El producto llevara Perforaciónes",
            hint_text="Perforaciónes",
            options=[
                dropdown.Option("N/A"),
                dropdown.Option("APLICA"),
            ],
            autofocus=True,
            on_change= lambda e: print(e.control.value)  # Imprimir el resultado
        )
        # Validar de tipo String ya que "13 de 8 mm"
        self.cntPerf = TextField(
                label="Cantidad de Perforaciónes",
                border= InputBorder.OUTLINE,
                border_color="Black",
                label_style=TextStyle(color="Black",italic=True),
        )

        self.prdctSuaje = Dropdown(
            label="El Producto lleva Suaje : ",
            hint_text="Suaje",
            options=[
                dropdown.Option("N/A"),
                dropdown.Option("APLICA"),
            ],
            autofocus=True,
            on_change= lambda e: print(e.control.value)  # Imprimir el resultado
        )

        self.tipSuaje = TextField(
                label="Tipo de Suaje",
                border= InputBorder.OUTLINE,
                border_color="Black",
                label_style=TextStyle(color="Black",italic=True),
        )

        self.empcdPrdct = Dropdown(
            label="Empacado de Producto",
            hint_text="Empacado",
            options=[
                dropdown.Option("N/A"),
                dropdown.Option("KILEADO"),
                dropdown.Option("PIEZAS"),
                dropdown.Option("GRANEL"),
            ],
            autofocus=True,
            on_change= lambda e: print(e.control.value)  # Imprimir el resultado
        )

        self.cntPzsPacq = TextField(
                label="Cantidad de Piezas por Paquete",
                border= InputBorder.OUTLINE,
                border_color="Black",
                label_style=TextStyle(color="Black",italic=True),
        )

        self.tipEmblj = Dropdown(
            label="Tipo de Embalaje",
            hint_text="Embalaje",
            options=[
                dropdown.Option("N/A"),
                dropdown.Option("BOLSA"),
                dropdown.Option("CAJA"),
            ],
            autofocus=True,
            on_change= lambda e: print(e.control.value)  # Imprimir el resultado
        )

        self.mdEmblj = TextField(
            label="Medida del Embalaje",
            border= InputBorder.OUTLINE,
            border_color="Black",
            label_style=TextStyle(color="Black",italic=True),
        )

        self.psrPrdct = Dropdown(
            label="Pesar Producto Por :",
            hint_text="Pesar",
            options=[
                dropdown.Option("N/A"),
                dropdown.Option("TARIMA"),
                dropdown.Option("BULTO"),
                dropdown.Option("CAJA")
            ],
            autofocus=True,
            on_change= lambda e: print(e.control.value)  # Imprimir el resultado
        )

        self.psProm = Dropdown(
            label="Peso Neto Promedio De : ",
            hint_text="Peso",
            options=[
                dropdown.Option("N/A"),
                dropdown.Option("BULTO"),
                dropdown.Option("CAJA"),
                dropdown.Option(
                    TextField(
                        label="Cantidad de Piezas por Paquete",
                        border= InputBorder.OUTLINE,
                        border_color="Black",
                        label_style=TextStyle(color="Black",italic=True),
                    ))
            ],
            autofocus=True,
            on_change= lambda e: print(e.control.value)  # Imprimir el resultado
        )

        self.etiquetado = Dropdown(
            label="Etiquetado",
            hint_text="etiquetado",
            options=[
                dropdown.Option("N/A"),
                dropdown.Option("BULTO O CAJA INDIVIDUAL"),
                dropdown.Option("TARIMA"),
                dropdown.Option("AMBOS")
            ],
            autofocus=True,
            on_change= lambda e: print(e.control.value)  # Imprimir el resultado
        )

        self.numBltsCjsCam_CmsTam = PopupMenuButton(
            Text("Numero de Bultos / Cajas por Cama y Camas por Tarima"),
            bgcolor="white",
            menu_position=PopupMenuPosition.OVER,
            items=[ 
                PopupMenuItem(
                    content= Column(width=200,controls=[
                        Text("Num. Bultos / Cajas por Tarima"),
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

        self.numBlts_CjsTam = PopupMenuButton(
            Text("Numero de Bultos ó Cajas por Tarima"),
            bgcolor="white",
            menu_position=PopupMenuPosition.OVER,
            items=[ 
                PopupMenuItem(
                    content= Column(width=200,controls=[
                        Text("Bultos/Cajas"),
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
       
        self.psPromTam = PopupMenuButton(
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

        self.tamEmply = Dropdown(
            label="La tarima llevara Emplaye",
            hint_text="Emplaye",
            options=[
                dropdown.Option("N/A"),
                dropdown.Option("APLICA")
            ],
            autofocus=True,
            on_change= lambda e: print(e.control.value)  # Imprimir el resultado
        )

        self.tamRef = Dropdown(
            label="La tarima sera Refilada",
            hint_text="Refilada",
            options=[
                dropdown.Option("N/A"),
                dropdown.Option("APLICA")
            ],
            autofocus=True,
            on_change= lambda e: print(e.control.value)  # Imprimir el resultado
        )