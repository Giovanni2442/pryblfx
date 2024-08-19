from flet import *
from src.views.VentanaCreate.Verificaciones import verificaciones
from src.app.filExcel.filtroExcel import filter
from src.views.VentanaCreate.InptsForm.InpstAux import InptsAux

### ENTRADAS DE TEXTO Y COMPONENTES PARA LA TABLA FichaTecnica y Ventas ###
class Inpts_FichaTec_Ventas():  
    def __init__(self,page):
        
        self.page = page
        self.valida = verificaciones(page)
        self.prUpdt = InptsAux()
        
    ### INPUTS DE TABLA FichaTecnica ###
        self.id_product = TextField(
            label="PrindCard",
            border= InputBorder.OUTLINE,
            border_color="Black",
            value = self.prUpdt.pruUpdate(),
            label_style=TextStyle(color="Black",italic=True),
            on_change= lambda e: self.valida.verInpts(e,filter.vrfPrintCard)       # Traba con la expreción regular del input
        )

        self.cliente = TextField(
            label="Ingresar el Cliente",
            border= InputBorder.OUTLINE,
            #value="N/A",
            error_text="",
            border_color="Black",
            value = "",
            label_style=TextStyle(color="Black",italic=True),
            on_change= lambda e: self.valida.verInpts(e,filter.vrfCliente)
        )

        self.fecha_Elav = TextField(
            label="dd/MM/YYYY",
            border= InputBorder.OUTLINE,
            border_color="Black",
            label_style=TextStyle(color="Black",italic=True),
            on_change= lambda e: self.valida.verInpts(e,filter.vrfFechas)
        )

        self.fecha_Rev = TextField(
            label="dd/MM/YYYY",
            #label_style=,
            border= InputBorder.OUTLINE,
            border_color="Black",
            label_style=TextStyle(color="Black",italic=True),
            on_change= lambda e: self.valida.verInpts(e,filter.vrfFechas)
        )

        self.producto = TextField(
            label="Producto",
            border= InputBorder.OUTLINE,       
            border_color="Black",
            label_style=TextStyle(color="Black",italic=True),
            on_change= lambda e: self.valida.verInpts(e,filter.vrfIsletter)
        )


    ### --- INPUTS DE TABLA VENTAS --- ###
        self.AsesorCmrcl = TextField(
            label="Asesor Comercial",
            border= InputBorder.OUTLINE,       
            border_color="Black",
            label_style=TextStyle(color="Black",italic=True),
            on_change= lambda e: self.valida.verInpts(e,filter.vrfIsletter) # change it
        )

        self.TipEmpq = TextField(
            label="Tipo de Empaque",
            border= InputBorder.OUTLINE,       
            border_color="Black",
            label_style=TextStyle(color="Black",italic=True),
            on_change= lambda e: self.valida.verInpts(e,filter.vrfIsletter) # change it
        )

        self.prdcLam = Dropdown(
            label="Laminado",
            hint_text="Producto Laminado",
            value="N/A",
            error_text="",
            options=[
                dropdown.Option("N/A"),
                dropdown.Option("APLICA"),
            ],
            autofocus=True,
            on_change= lambda e: print(e.control.value)  # Imprimir el resultado
        )

        self.EstrcPrdct = TextField(
            label="Estructura del Producto",
            border= InputBorder.OUTLINE,       
            border_color="Black",
            label_style=TextStyle(color="Black",italic=True),
            on_change= lambda e: self.valida.verInpts(e,filter.vrfEstrcProd) # change it
        )

        self.PrdctEmpq = TextField(
            label="Producto que se empaca",
            border= InputBorder.OUTLINE,       
            border_color="Black",
            label_style=TextStyle(color="Black",italic=True),
            on_change= lambda e: self.valida.verInpts(e,filter.vrfIsletter) # change it
        )
    
    def tplInptsFichTec(self):
        return [
            self.id_product,
            self.cliente,
            self.fecha_Elav,
            self.fecha_Rev,
            self.producto
        ]
    
    def tplInptsVentas(self):
        return [
            self.AsesorCmrcl,
            self.TipEmpq,
            self.prdcLam,
            self.EstrcPrdct,
            self.PrdctEmpq
        ]
        
