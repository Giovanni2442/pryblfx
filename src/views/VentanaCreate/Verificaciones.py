from flet import *
from src.app.filExcel.filtroExcel import filter
from src.Controllers.appTable import Controllers

# Librerias de Prueba con los inputs 
#from src.views.VentanaCreate.InptsForm.Inpts_FichaTecVentas import Inpts_FichaTec_Ventas

# Tareas : 
# * Mejorar Las validadicones de cambio de color rojo               
# * Implementar las expreciones regulares adecuadas a cada Input
# * Implementar el boton de edicción
# * Implementar los modales de errores, Inserción y Modificación
# * Implementar los inputs y las vistas para el formulario restante e ingresar sus validaciónes
# * Hacer sus respetivas conexiónes y controllers a la base de datos
# * Modularizarlo
# * Hacer un prototipo para Editar el PDF de la ficha tecnica

class verificaciones():
    def __init__(self,page):
        super().__init__()

        #self.page = page
        self.filter = filter().vrfPrintCard
        self.b1 = True
        self.page = page
        self.dataTbl = Controllers()

        #self.InptsFichT = Inpts_FichaTec_Ventas(page)    # Inputs FichaTecnica
        
    # Tupla de TextFields
    '''def tplInpts(self,*any):
        dic = []
        dic = (
            #self.InptsFichT.tplInptsFichTec
            any
        )
        return dic'''
    

    # Limpiar Labels
    def clean_fields(self):
    #    tpl = self.tplInpts()
    #    for i in tpl:
    #        i.value = ""
    #        i.border_color = "black"
        pass

    # Este es un Metodo de Prueba hacer caso Omiso
    #def jer(self):      # Obtiene el conjunto de valores de los TextFields
    #    #tpl = self.tplInpts()
    #    self.dataTbl.post_data(
    #        id=tpl[0].value,
    #        cln=tpl[1].value,
    #        fch1=tpl[2].value,
    #        fch2=tpl[3].value,
    #        prdct=tpl[4].value)
    #    self.clean_fields()
        #print(self.dataTbl.get_row_Table())

        
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

################# MODALES #######################

       # Función para cerrar el diálogo

    def open_dialog(slef,dialog,page):
        page.overlay.append(dialog)
        dialog.open = True
        page.update()
        
    def close_dialog(self,dialog, page):
        dialog.open = False
        page.update()
        

#################################################


###### INSERCIÓN A LA BASE DE DATOS ##########################

    def prTpl(self,*tpl):
        #for i in tpl:
        #    for j in i: 
        #        print(j.label)
        print(tpl[1][2].label)

    def vlVoid(self,tpl):           # Función que verifica si al Inicio del Fromulario los campos estan vaciós para evitar inserción de campos vacios
       # tpl = self.tplInpts()
        vlVoid = []      # Recolecta campos vaciós
        vlErr = []         
        sr = None
        #print(len(tpl[0].value))
        for i in tpl:
            for j in i:
                if j.value != "":
                    #if j.border_color != "red":
                    if j.error_text != "":
                        vlErr.append(j.label)
                    continue
                else:
                    j.error_text = "Ingrese los valores"
                    vlVoid.append(j.label)
                    j.update()

        if len(vlVoid) > 0:
            self.mdlVoidVl = AlertDialog(
                    modal=True,
                    title= Text("Faltan campos por llenar!"),
                    actions=[
                        TextButton("CERRAR", on_click=lambda e: self.close_dialog(self.mdlVoidVl,self.page))
                    ]
                )
            
            self.open_dialog(self.mdlVoidVl,self.page)
            return False
        elif len(vlErr) > 0:
            self.mdlErrValue = AlertDialog(
                    modal=True,
                    title= Text(f"Los valores en {vlErr} , Son incorrectos!"),
                    actions=[
                        TextButton("CERRAR", on_click=lambda e: self.close_dialog(self.mdlErrValue,self.page))
                    ]
                )
            self.open_dialog(self.mdlErrValue,self.page)
            #print(False)
            return False
        else : 
            return True
        
    def pr3(self,*tpl):
        b1 = self.vlVoid(tpl)
        print(b1)


    def pruData(self,*dic):
        dic2 = [] # Tupla de Errores  
        #tpl = self.tplInpts()
        tpl = dic
        bnd = 0
        
        # Recolecta los errores para mostrarlos en Modal
        #for i in tpl:
        #    for j in i:
        #        pass
        
        if self.vlVoid(tpl) != False:
        #else:       # Comprobar si ya existe en la base de datos, evitando sobre escritura
            contact_exists = False
            for row in self.dataTbl.get_row_Table():
                if row[0] == tpl[0][0].value:
                    contact_exists = True
                    #bnd = 1
                    break
                #if bnd !=0:
                #    break ### ARREGLAR ESTE PINCHE DESMADRE ####

            if not contact_exists:
                #param_values = [item.value for item in j]     # Recorre las tuplas con el valor de los Inputs y le asigna su valor
                self.dataTbl.post_data(     # Ingresar en la Tabla de Ficha [0][elmt]
                    tpl[0][0].value,
                    tpl[0][1].value,
                    tpl[0][2].value,
                    tpl[0][3].value,
                    tpl[0][4].value
                )  
                
                print("Insertado!")
                self.clean_fields()
            else:
                self.mdlDplctPrdct = AlertDialog(
                    modal=True,
                    title= Text(f"El Producto : {row[0]} ya Existe!"),
                    actions=[
                        TextButton("CERRAR", on_click=lambda e: self.close_dialog(self.mdlDplctPrdct,self.page))
                    ]
                )
                self.open_dialog(self.mdlDplctPrdct,self.page)
                #print("El contacto ya existe en la base de datos.")