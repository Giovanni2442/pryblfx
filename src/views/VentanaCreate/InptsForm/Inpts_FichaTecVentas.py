from flet import *
#import asyncio
from src.views.VentanaCreate.Verificaciones import verificaciones
from src.app.filExcel.filtroExcel import filter
from src.views.VentanaCreate.InptsForm.InpstAux import InptsAux
from src.Controllers.appFichVent import appFichVent

### ENTRADAS DE TEXTO Y COMPONENTES PARA LA TABLA FichaTecnica y Ventas ###
class Inpts_FichaTec_Ventas():  
    def __init__(self,page):
        
        self.page = page
        self.valida = verificaciones(page)

        # PRUEBA DE OPTIMIZACIÓN
        self.dtaFich = appFichVent
        
        # -- ACTUALIZA SI ES INSERT O UPDATE --#
        self.aux = InptsAux
        
        # ESTADO IDENTIFICADOR DE INSERT Y UPDATE
        self.estd = self.page.client_storage.get("estado")
        # ID DEL PRODUCTO HA EDITAR
        self.id = self.page.client_storage.get("id")
        #print(self.id)
        
        self.dta = self.dtaFich().getFicha(self.id)
        self.dtaVnts = self.dtaFich().get_Ventas(self.id)

        
    ### INPUTS DE TABLA FichaTecnica ###
        self.id_product = TextField(
            label="PrindCard",
            border= InputBorder.OUTLINE,
            border_color="Black",
            #value=self.aux().getData(self.id,'FICHA',0,""),
            value=self.data("",0),
            error_text = "",
            label_style=TextStyle(color="Black",italic=True),
            on_change= lambda e: self.valida.verInpts(e,filter.vrfPrintCard),       # Traba con la expreción regular del input
            disabled= self.edit()
        )

        self.cliente = TextField(
            label="Ingresar el Cliente",
            border= InputBorder.OUTLINE,
            error_text="",
            border_color="Black",
            value=self.data("",1),
            #value=self.aux().getData(self.id,'FICHA',1,""),
            label_style=TextStyle(color="Black",italic=True),
            on_change= lambda e: self.valida.verInpts(e,filter.vrfCliente),
            disabled= self.editCliente()

        )

        self.producto = TextField(
            label="Producto",
            border= InputBorder.OUTLINE,       
            border_color="Black",
            value=self.data("",2),
            error_text = "",
            #value=self.aux().getData(self.id,'FICHA',4,""),
            label_style=TextStyle(color="Black",italic=True),
            on_change= lambda e: self.valida.verInpts(e,filter.vrfIsletter)
        )

        self.fecha_Elav = TextField(
            label="dd/MM/YYYY",
            border= InputBorder.OUTLINE,
            border_color="Black",
            value=self.data("",3),
            error_text = "",
            #value=self.aux().getData(self.id,'FICHA',2,""),
            label_style=TextStyle(color="Black",italic=True),
            on_change= lambda e: self.valida.verInpts(e,filter.vrfFechas)
        )

        #'''
        self.fecha_Rev = TextField(
            label="dd/MM/YYYY",
            #label_style=,
            border= InputBorder.OUTLINE,
            border_color="Black",
            #value=self.data("",4),
            value='NULL',
            error_text = "",
            #value=self.aux().getData(self.id,'FICHA',3,""),
            label_style=TextStyle(color="Black",italic=True),
            on_change= lambda e: self.valida.verInpts(e,filter.vrfFechas)
        )#'''

    ### --- INPUTS DE TABLA VENTAS --- ###
        self.AsesorCmrcl = TextField(
            label="Asesor Comercial",
            border= InputBorder.OUTLINE,       
            border_color="Black",
            value=self.dataVentas("",1),
            error_text = "",
            #value=self.aux().getData(self.id,'VENTAS',3,""),
            label_style=TextStyle(color="Black",italic=True),
            on_change= lambda e: self.valida.verInpts(e,filter.vrfIsletter) # change it
        )

        self.TipEmpq = TextField(
            label="Tipo de Empaque",
            border= InputBorder.OUTLINE,       
            border_color="Black",
            value=self.dataVentas("",2),
            error_text = "",
            #value=self.aux().getData(self.id,'VENTAS',2,""),
            label_style=TextStyle(color="Black",italic=True),
            on_change= lambda e: self.valida.verInpts(e,filter.vrfIsletter) # change it
        )

        self.prdcLam = Dropdown(
            label="Laminado",
            hint_text="Producto Laminado",
            #value="N/A",
            value=self.dataVentas("N/A",3),
            error_text = "",
            #value=self.aux().getData(self.id,'VENTAS',3,"N/A"),
            options=[
                dropdown.Option("N/A"),
                dropdown.Option("APLICA"),
            ],
            autofocus=True,
            #on_change= lambda e: print(e.control.value)  # Imprimir el resultado
        )

        self.EstrcPrdct = TextField(
            label="Estructura del Producto",
            border= InputBorder.OUTLINE,       
            border_color="Black",
            value=self.dataVentas("",4),
            error_text = "",
            #value=self.aux().getData(self.id,'VENTAS',4,""),
            #value=self.data(""),
            label_style=TextStyle(color="Black",italic=True),
            on_change= lambda e: self.valida.verInpts(e,filter.vrfEstrcProd) # change it
        )

        self.PrdctEmpq = TextField(
            label="Producto que se empaca",
            border= InputBorder.OUTLINE,       
            border_color="Black",
            #value=self.aux().getData(self.id,'VENTAS',4,""),
            value=self.dataVentas("",5),
            error_text = "",
            label_style=TextStyle(color="Black",italic=True),
            on_change= lambda e: self.valida.verInpts(e,filter.vrfIsletter) # change it
        )

    # GET FICHA
    def data(self,default_value,Indx):
        
        #print("--",dta)
        if self.estd == "Insert":   
            return default_value
        elif self.estd == "UpdateMsv":
            return 'N/A'
        else:
            return self.dta[Indx] if self.dta else default_value
            #return f"{Indx}"

    # GET VENTAS
    def dataVentas(self,default_value,Indx):
        #if self.id != "Insert":
        if self.estd == "Insert":   
            return default_value
        elif self.estd == "UpdateMsv":
            return 'N/A'
        else:
            return self.dtaVnts[Indx] if self.dtaVnts else default_value

    # DESACTIVAR EDICIÓN
    def edit(self):
        #if  self.id != "Insert":
        if self.estd != "Update" and self.estd != "UpdateMsv":
            return False
        else:
            return True
    
    def editCliente(self):
        if self.estd == "UpdateMsv":
            return True
        else:
            return False

    # OBTIENE DATOS POR MEDIO DE SU ID
    def tplInptsFichTec(self):
        return [
            self.id_product,
            self.cliente,
            self.producto,
            self.fecha_Elav,
            self.fecha_Rev
        ]
    
    def tplInptsVentas(self):
        return [
            self.AsesorCmrcl,
            self.TipEmpq,
            self.prdcLam,
            self.EstrcPrdct,
            self.PrdctEmpq
        ]
        
