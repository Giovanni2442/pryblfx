from flet import *
from src.app.filExcel.filtroExcel import filter
from src.Controllers.appTable import Controllers
from src.views.VentanaCreate.createFicha.createPdf import CreatePdf

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
        self.crtPdf = CreatePdf()

        #self.InptsFichT = Inpts_FichaTec_Ventas(page)    # Inputs FichaTecnica
        
    # Limpiar Labels
    def clean_fields(self,tpl):
        #tpl = self.tplInpts()
        for i in tpl:
            for j in i:
                j.value = ""
                j.update()
        self.page.update()

    def seeVal(slef,*tpl):
        r = tpl[0][0].value = "Esto es una prueba"
        print( tpl[0][0].value)
        
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

    # Función para abrir el diálogo
    def open_dialog(slef,dialog,page):
        page.overlay.append(dialog)
        dialog.open = True
        page.update()
    # Función para cerrar el diálogo
    def close_dialog(self,e,dialog,page):
        dialog.open = False
        page.update()

#################################################


###### INSERCIÓN A LA BASE DE DATOS ##########################

    def prTpl(self,*tpl):
        print(tpl[1][2].label)

    def vlVoid(self,tpl):           # Función que verifica si al Inicio del Fromulario los campos estan vaciós para evitar inserción de campos vacios
       # tpl = self.tplInpts()
        vlVoid = []      # Recolecta campos vaciós
        vlErr = []         
        sr = None
        #print(len(tpl[0].value))
        for i in tpl:                               # Recorre las tuplas
            for j in i:                             # Recorre el conjunto de tuplas
                if j.value != "":
                    #if j.border_color != "red":
                    if j.error_text != "":
                        vlErr.append(j.label)       # Captura los campos vacios
                    continue
                else:
                    j.error_text = "Ingrese los valores"
                    vlVoid.append(j.label)
                    j.update()

        if len(vlVoid) > 0:
            #mdlVoidVl
            self.mdlVoidVl = AlertDialog(
                    modal=True,
                    title= Text(f"Faltan campos por llenar!"),
                    actions=[
                        TextButton("CERRAR", on_click= lambda e: self.close_dialog(e,self.mdlVoidVl,self.page))
                    ]
                )
            self.open_dialog(self.mdlVoidVl,self.page)
            return False
        elif len(vlErr) > 0:
            self.mdlErrValue = AlertDialog(
                    modal=True,
                    title= Text(f"Los valores en {vlErr} , Son incorrectos!"),
                    actions=[
                        TextButton("CERRAR", on_click=lambda e: self.close_dialog(e,self.mdlErrValue,self.page))
                    ]
                )
            self.open_dialog(self.mdlErrValue,self.page)
            return False
        else : 
            return True
        
    def pr3(self,*tpl):
        #b1 = self.vlVoid(tpl)
        #print(b1) <-- bromita de 1 hora XD

        if self.vlVoid(tpl) != False:                   # Si ninguna validación se cumple
            contact_exists = False
            for row in self.dataTbl.get_row_Table():    # Recorre la tabla FichaTecnica ya que es la tabla padre       
                if row[0] == tpl[0][0].value:           # La primera tabla FichaTecnica contiene el ID asi que de la tupa toma el [FichaTec][Id]
                    contact_exists = True
                    break
                #### ARREGLAR ESTE PINCHE DESMADRE ####

            if not contact_exists:
                # MODULARIZARLO
                ficha_tec_values = [item.value for item in tpl[0]]
                ventas_values = [item.value for item in tpl[1]]

                self.dataTbl.post_data(*ficha_tec_values)
                self.dataTbl.post_dataVentas(tpl[0][0],*ventas_values)            
                
                ### VALORES DE LOS INPUTS ###
                self.crtPdf.Inser(tpl)
                #############################
                self.msgDlt = SnackBar(
                    content=Column(
                        controls=[
                            Container(
                                Text(f"PRODUCTO : {tpl[0][0].value} , INSERTADO CON EXITO!",size=20,color="white"),
                                alignment=alignment.center
                            ),
                        ],
                    ),
                    bgcolor="#5AE590",
                )
                self.open_dialog(self.msgDlt,self.page)
                self.clean_fields(tpl)
            else:
                self.mdlDplctPrdct = AlertDialog(
                    modal=True,
                    title= Text(f"El Producto : {row[0]} ya Existe!"),
                    actions=[
                        TextButton("CERRAR", on_click=lambda e: self.close_dialog(e,self.mdlDplctPrdct,self.page))
                    ]
                )
                self.open_dialog(self.mdlDplctPrdct,self.page)
                return False
                #print("El contacto ya existe en la base de datos.")