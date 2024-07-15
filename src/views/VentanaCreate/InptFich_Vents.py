from flet import *
from src.app.filExcel.filtroExcel import filter
from src.Controllers.appTable import Controllers


# Tareas : 
# * Mejorar Las validadicones de cambio de color rojo 
# * Implementar las expreciones regulares adecuadas a cada Input
# * Implementar el boton de edicción
# * Implementar los modales de errores, Inserción y Modificación
# * Implementar los inputs y las vistas para el formulario restante e ingresar sus validaciónes
# * Hacer sus respetivas conexiónes y controllers a la base de datos
# * Modularizarlo
# * Hacer un prototipo para Editar el PDF de la ficha tecnica


class InptsTable():
    def __init__(self):
        super().__init__()

        #self.page = page
        self.filter = filter().vrfPrintCard
        self.b1 = True
        self.dataTbl = Controllers()

    ### INPUTS DE TABLA FichaTecnica ###
        self.id_product = TextField(
            label="PrindCard",
            border= InputBorder.OUTLINE,
            border_color="Black",
            label_style=TextStyle(color="Black",italic=True),
            on_change= lambda e: self.verInpts(e,filter.vrfPrintCard)       # Traba con la expreción regular del input
        )

        self.cliente = TextField(
            label="Ingresar el Cliente",
            border= InputBorder.OUTLINE,
            value="N/A",
            border_color="Black",
            label_style=TextStyle(color="Black",italic=True),
            on_change= lambda e: self.verInpts(e,filter.vrfCliente)
        )

        self.fecha_Elav = TextField(
            label="dd/MM/YYYY",
            border= InputBorder.OUTLINE,
            border_color="Black",
            label_style=TextStyle(color="Black",italic=True),
            on_change= lambda e: self.verInpts(e,filter.vrfFechas)
        )

        self.fecha_Rev = TextField(
            label="dd/MM/YYYY",
            #label_style=,
            border= InputBorder.OUTLINE,
            border_color="Black",
            label_style=TextStyle(color="Black",italic=True),
            on_change= lambda e: self.verInpts(e,filter.vrfFechas)
        )

        self.producto = TextField(
            label="Producto",
            border= InputBorder.OUTLINE,       
            border_color="Black",
            label_style=TextStyle(color="Black",italic=True),
            on_change= lambda e: self.verInpts(e,filter.vrfIsletter)
        )


    ### INPUTS DE TABLA VENTAS ###
        self.AsesorCmrcl = TextField(
            label="Asesor Comercial",
            border= InputBorder.OUTLINE,       
            border_color="Black",
            label_style=TextStyle(color="Black",italic=True),
            on_change= lambda e: self.verInpts(e,filter.vrfIsletter) # change it
        )

        self.TipEmpq = TextField(
            label="Tipo de Empaque",
            border= InputBorder.OUTLINE,       
            border_color="Black",
            label_style=TextStyle(color="Black",italic=True),
            on_change= lambda e: self.verInpts(e,filter.vrfIsletter) # change it
        )

        self.prdcLam = Dropdown(
            label="Laminado",
            hint_text="Producto Laminado",
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
            on_change= lambda e: self.verInpts(e,filter.vrfEstrcProd) # change it
        )

        self.PrdctEmpq = TextField(
            label="Producto que se empaca",
            border= InputBorder.OUTLINE,       
            border_color="Black",
            label_style=TextStyle(color="Black",italic=True),
            on_change= lambda e: self.verInpts(e,filter.vrfIsletter) # change it
        )

    
    # Tupla de TextFields
    def tplInpts(self):
        dic = [
            self.id_product,
            self.cliente,
            self.producto,
            self.fecha_Elav,
            self.fecha_Rev
        ]
        return dic

    # Limpiar Labels
    def clean_fields(self):
        tpl = self.tplInpts()
        for i in tpl:
            i.value = ""
            i.border_color = "black"

    def jer(self):
        tpl = self.tplInpts()
        self.dataTbl.post_data(
            id=tpl[0].value,
            cln=tpl[1].value,
            fch1=tpl[2].value,
            fch2=tpl[3].value,
            prdct=tpl[4].value)
        self.clean_fields()
        #print(self.dataTbl.get_row_Table())

    def ji(self,id):
        self.id_product.value = id
        print("--",id)
        self.id_product.update()
        
    
###### PRUEBAS PARA FILTRADO ###########
    def verInpts(self,e,rejex):
        inpt = e.control
        jer = len(e.control.value)
        trimmed_value = inpt.value.strip()
        #print(jer)
        if jer != 0 and trimmed_value:      # trimed_value : localiza espacios en blanco 
            if rejex(inpt.value):
                print(f"{inpt.label}  : {inpt.value}")
                inpt.border_color="green"
                inpt.error_text=""
            else:
                #inpt.border_color="red"
                inpt.error_text=f"{inpt.label} Incorrecto!"
                print("Incorrecto")
        else:
            #e.control.border_color="red"
            inpt.error_text="Favor de ingresar un valor!"
            print("Campo Vacio")

        inpt.update()  # Actualiza el control para reflejar los cambios

######################################################

###### INSERCIÓN A LA BASE DE DATOS ##########################

    def prCero(self):
        tpl = self.tplInpts()
        ji = []
        #print(len(tpl[0].value))
        for i in tpl:
            if len(i.value) != 0:
               continue
            else:
                ji.append(i.label)
        print(ji)

    def pruData(self):
        dic2 = [] # Tupla de Errores  
        tpl = self.tplInpts()

        # Recolecta los errores para mostrarlos en Modal
        for i in tpl:
            if i.border_color != "red":
                continue
            else:
                dic2.append(i.label)
        
        if len(dic2) !=0:
            print("Errores",dic2)
        else:       # Comprobar si ya existe en la base de datos, evitando sobre escritura
            contact_exists = False
            for row in self.dataTbl.get_row_Table():
                if row[1] == tpl[0].value:
                    contact_exists = True
                    break
            if not contact_exists:
                self.dataTbl.post_data(
                    id=tpl[0].value,
                    cln=tpl[1].value,
                    fch1=tpl[2].value,
                    fch2=tpl[3].value,
                    prdct=tpl[4].value)
                self.clean_fields()
            else:
                print("El contacto ya existe en la base de datos.")
            #print("Escriba sus datos")