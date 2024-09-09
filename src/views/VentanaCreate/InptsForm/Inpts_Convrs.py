from flet import *
from src.views.VentanaCreate.Verificaciones import verificaciones
from src.app.filExcel.filtroExcel import filter
from src.views.VentanaCreate.InptsForm.InpstAux import InptsAux
from src.Controllers.appConvrs import appConvrs


class Inpts_Convrs():
    def __init__(self,page):
        
        self.page = page
        self.valida = verificaciones(page)

         # -- ACTUALIZA SI ES INSERT O UPDATE --#
        self.aux = InptsAux
        self.Cnvrs = appConvrs
    
        # ESTADO IDENTIFICADOR DE INSERT Y UPDATE
        self.estd = self.page.client_storage.get("estado")
        # ID DEL PRODUCTO HA EDITAR
        self.id = self.page.client_storage.get("id")

        # QURY DATA FORM #
            # QUERY GET REFILADO
        self.dtaCvrs = self.Cnvrs().transGetConvrs(self.id)


    ### INPUTS DE LA TABLA CONVERSIÓN ###

    ### SESSIÓN 1 ###

        self.medEmpq = PopupMenuButton(
            Text("Medida del Empaque",color=colors.WHITE),
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
                            value=self.dataCnvrs('0.0',18),
                            error_text = "",
                            label_style=TextStyle(color="black",italic=True),
                            on_change= lambda e: self.valida.verInpts(e,filter.vrfIsNumber)
                        )
                    ])
                ),
                PopupMenuItem(
                    content= Column([
                        Text("Alto"),
                        TextField(
                            label="Alto",
                            border= InputBorder.OUTLINE,
                            border_color="Black",
                            value=self.dataCnvrs('0.0',19),
                            error_text = "",
                            label_style=TextStyle(color="Black",italic=True),
                            on_change= lambda e: self.valida.verInpts(e,filter.vrfIsNumber)
                        )
                    ])
                ),
            ]
        )

        self.tipEmpq = TextField(
                label="Tipo de Empaque",
                border= InputBorder.OUTLINE,
                border_color="Black",
                value=self.dataCnvrs("N/A",1),
                error_text = "",
                label_style=TextStyle(color="Black",italic=True),
                on_change= lambda e: self.valida.verInpts(e,filter.vrfAny)
        )

        self.tipSello = TextField(
                label="Tipo de Sello",
                border= InputBorder.OUTLINE,
                border_color="Black",
                value=self.dataCnvrs("N/A",2),
                error_text = "",
                label_style=TextStyle(color="Black",italic=True),
                on_change= lambda e: self.valida.verInpts(e,filter.vrfIsletter)
        )

        self.tipAcbd = TextField(
                label="Tipo de Acabado",
                border= InputBorder.OUTLINE,
                border_color="Black",
                value=self.dataCnvrs("N/A",3),
                error_text = "",
                label_style=TextStyle(color="Black",italic=True),
                on_change= lambda e: self.valida.verInpts(e,filter.vrfAny)
        )

        self.prdctPerf = Dropdown(
            label="El producto llevara Perforaciónes",
            hint_text="Perforaciónes",
            value=self.dataCnvrs("N/A",4),
            error_text = "",
            options=[
                dropdown.Option("N/A"),
                dropdown.Option("APLICA"),
            ],
            autofocus=True,
            #on_change= lambda e: print(e.control.value)  # Imprimir el resultado
        )
        # Validar de tipo String ya que "13 de 8 mm"
        self.cntPerf = TextField(
                label="Cantidad de Perforaciónes",
                border= InputBorder.OUTLINE,
                border_color="Black",
                value=self.dataCnvrs('0',5),
                error_text = "",
                label_style=TextStyle(color="Black",italic=True),
                on_change= lambda e: self.valida.verInpts(e,filter.vrfIsNumber)
        )

        self.prdctSuaje = Dropdown(
            label="El Producto lleva Suaje : ",
            hint_text="Suaje",
            value=self.dataCnvrs('N/A',6),
            error_text = "",
            options=[
                dropdown.Option("N/A"),
                dropdown.Option("APLICA"),
            ],
            autofocus=True,
            #on_change= lambda e: print(e.control.value)  # Imprimir el resultado
        )

        self.tipSuaje = TextField(
                label="Tipo de Suaje",
                border= InputBorder.OUTLINE,
                border_color="Black",
                value=self.dataCnvrs('N/A',7),
                error_text = "",
                label_style=TextStyle(color="Black",italic=True),
                on_change= lambda e: self.valida.verInpts(e,filter.vrfAny)
        )

        self.empcdPrdct = Dropdown(
            label="Empacado de Producto",
            hint_text="Empacado",
            value=self.dataCnvrs('N/A',8),
            error_text = "",
            options=[
                dropdown.Option("N/A"),
                dropdown.Option("KILEADO"),
                dropdown.Option("PIEZAS"),
                dropdown.Option("GRANEL"),
            ],
            autofocus=True,
            #on_change= lambda e: print(e.control.value)  # Imprimir el resultado
        )

        self.cntPzsPacq = TextField(
                label="Cantidad de Piezas por Paquete",
                border= InputBorder.OUTLINE,
                border_color="Black",
                value=self.dataCnvrs('0',9),
                error_text = "",
                label_style=TextStyle(color="Black",italic=True),
                on_change= lambda e: self.valida.verInpts(e,filter.vrfIsNumber)
        )

        self.tipEmblj = Dropdown(
            label="Tipo de Embalaje",
            hint_text="Embalaje",
            value=self.dataCnvrs('N/A',10),
            error_text = "",
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
            value=self.dataCnvrs('0',11),
            error_text = "",
            label_style=TextStyle(color="Black",italic=True),
            on_change= lambda e: self.valida.verInpts(e,filter.vrfIsNumber)
        )

        self.psrPrdct = Dropdown(
            label="Pesar Producto Por :",
            hint_text="Pesar",
            value=self.dataCnvrs('N/A',12),
            error_text = "",
            options=[
                dropdown.Option("N/A"),
                dropdown.Option("TARIMA"),
                dropdown.Option("BULTO"),
                dropdown.Option("CAJA")
            ],
            autofocus=True,
            on_change= lambda e: print(e.control.value)  # Imprimir el resultado
        )

        self.psProm = TextField(
            label="Peso neto promedio de bobina",
            border= InputBorder.OUTLINE,
            border_color="Black",
            value=self.dataCnvrs('0',13),
            error_text = "",
            label_style=TextStyle(color="Black",italic=True),
            on_change= lambda e: self.valida.verInpts(e,filter.vrfIsNumber)
        )

        self.etiquetado = Dropdown(
            label="Etiquetado",
            hint_text="etiquetado",
            value=self.dataCnvrs('N/A',14),
            error_text = "",
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
            Text("Numero de Bultos / Cajas por Cama y Camas por Tarima",color=colors.WHITE),
            bgcolor="white",
            menu_position=PopupMenuPosition.OVER,
            items=[ 
                PopupMenuItem(
                    content= Column(width=200,controls=[
                        Text("Num. Bultos / Cajas por Tarima"),
                        TextField(
                            label="Bultos",
                            border= InputBorder.OUTLINE,
                            #width=100,
                            border_color="black",
                            value=self.dataCnvrs('0.0',21),
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
                            label="Camas",
                            border= InputBorder.OUTLINE,
                            border_color="Black",
                            value=self.dataCnvrs('0.0',22),
                            error_text = "",
                            label_style=TextStyle(color="Black",italic=True),
                            on_change= lambda e: self.valida.verInpts(e,filter.vrfIsNumber)
                        )
                    ])
                ),
            ]
        )

        self.numBlts_CjsTam = PopupMenuButton(
            Text("Numero de Bultos ó Cajas por Tarima",color=colors.WHITE),
            bgcolor="white",
            menu_position=PopupMenuPosition.OVER,
            items=[ 
                PopupMenuItem(
                    content= Column(width=200,controls=[
                        Text("Bultos/Cajas"),
                        TextField(
                            label="bultos/cajas",
                            border= InputBorder.OUTLINE,
                            #width=100,
                            border_color="black",
                            value=self.dataCnvrs('0.0',24),
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
                            value=self.dataCnvrs('0.0',25),
                            error_text = "",
                            label_style=TextStyle(color="Black",italic=True),
                            on_change= lambda e: self.valida.verInpts(e,filter.vrfIsNumber)
                        )
                    ])
                ),
            ]
        )
       
        self.psPromTam = PopupMenuButton(
            Text("Peso neto Promedio por Tarima",color=colors.WHITE),
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
                            value=self.dataCnvrs('0.0',27),
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
                            value=self.dataCnvrs('0.0',28),
                            error_text = "",
                            label_style=TextStyle(color="Black",italic=True),
                            on_change= lambda e: self.valida.verInpts(e,filter.vrfIsNumber)
                        )
                    ])
                ),
            ]
        )

        self.tamEmply = Dropdown(
            label="La tarima llevara Emplaye",
            hint_text="Emplaye",
            value=self.dataCnvrs('N/A',15),
            error_text = "",
            options=[
                dropdown.Option("N/A"),
                dropdown.Option("APLICA")
            ],
            autofocus=True,
            #on_change= lambda e: print(e.control.value)  # Imprimir el resultado
        )

        self.tamFlej = Dropdown(
            label="La tarima sera Flejada",
            hint_text="Fleje",
            value=self.dataCnvrs('N/A',16),
            error_text = "",
            options=[
                dropdown.Option("N/A"),
                dropdown.Option("APLICA")
            ],
            autofocus=True,
            #on_change= lambda e: print(e.control.value)  # Imprimir el resultado
        )

    # GET CNVRS
    def dataCnvrs(self,default_value,Indx):
        if self.estd != "Insert" and self.estd != "UpdateMsv":  
            #print(self.dtaCvrs)             
            #return self.dtaCvrs[Indx]
            return f"{Indx}"
        else:
            return default_value

    def tplInptsConvrs(self):
        return [
            self.tipEmpq,       # -  Tributos de la tabla padre - #
            self.tipSello,
            self.tipAcbd,
            self.prdctPerf,
            self.cntPerf,
            self.prdctSuaje,
            self.tipSuaje,
            self.empcdPrdct,
            self.cntPzsPacq,
            self.tipEmblj,
            self.mdEmblj,
            self.psrPrdct,
            self.psProm,
            self.etiquetado,
            self.tamEmply,
            self.tamFlej,

            self.medEmpq,
            self.numBltsCjsCam_CmsTam,
            self.numBlts_CjsTam,
            self.psPromTam,
        ]