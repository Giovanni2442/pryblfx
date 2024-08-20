from flet import *
from src.views.VentanaCreate.Verificaciones import verificaciones
from src.app.filExcel.filtroExcel import filter
from src.views.VentanaCreate.InptsForm.InpstAux import InptsAux

### ENTRADAS DE TEXTO Y COMPONENTES PARA LA TABLA FichaTecnica y Ventas ###
class Inpts_FichaTec_Ventas():  
    def __init__(self,page):
        
        self.page = page
        self.valida = verificaciones(page)
        
        # -- ACTUALIZA SI ES INSERT O UPDATE --#
        self.aux = InptsAux()
        # IDENTIFICADOR DE INSERT Y UPDATE
        self.id = self.page.client_storage.get("id")
        
    ### INPUTS DE TABLA FichaTecnica ###
        self.id_product = TextField(
            label="PrindCard",
            border= InputBorder.OUTLINE,
            border_color="Black",
            #value = self.aux.pruUpdate(self.id ,"",0),
            value=self.aux.getData(self.id,'FICHA',0,""),
            label_style=TextStyle(color="Black",italic=True),
            on_change= lambda e: self.valida.verInpts(e,filter.vrfPrintCard),       # Traba con la expreción regular del input
            disabled= lambda _: self.edit()
        )

        self.cliente = TextField(
            label="Ingresar el Cliente",
            border= InputBorder.OUTLINE,
            error_text="",
            border_color="Black",
            value = self.aux.getData(self.id,'FICHA',1,""),
            label_style=TextStyle(color="Black",italic=True),
            on_change= lambda e: self.valida.verInpts(e,filter.vrfCliente)
        )

        self.fecha_Elav = TextField(
            label="dd/MM/YYYY",
            border= InputBorder.OUTLINE,
            border_color="Black",
            value = self.aux.getData(self.id,'FICHA',2,""),
            label_style=TextStyle(color="Black",italic=True),
            on_change= lambda e: self.valida.verInpts(e,filter.vrfFechas)
        )

        self.fecha_Rev = TextField(
            label="dd/MM/YYYY",
            #label_style=,
            border= InputBorder.OUTLINE,
            border_color="Black",
            value=self.aux.getData(self.id,'FICHA',3,""),
            label_style=TextStyle(color="Black",italic=True),
            on_change= lambda e: self.valida.verInpts(e,filter.vrfFechas)
        )

        self.producto = TextField(
            label="Producto",
            border= InputBorder.OUTLINE,       
            border_color="Black",
            value= self.aux.getData(self.id,'FICHA',4,""),
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

    # DESACTIVAR EDICIÓN
    def edit(self):
        if  self.aux.changeBtn(self.page.client_storage.get("id")) != "Insert":
            return True
        else:
            return False

    # OBTIENE DATOS POR MEDIO DE SU ID
    def data(self,tbl,indx,vlDlfd):
        return self.aux.getData(self.id,tbl,indx,vlDlfd)
    
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
        
