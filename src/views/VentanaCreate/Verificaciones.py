from flet import *
from src.app.filExcel.filtroExcel import filter
from src.Controllers.appInserts import appInserts
from src.Controllers.appFichVent import appFichVent
from src.views.VentanaCreate.createFicha.createPdf import CreatePdf

# Tareas :               
# * Implementar las expreciones regulares adecuadas a cada Input * 
# * Implementar el boton de edicción * 
# * Hacer sus respetivas conexiónes y controllers a la base de datos *
# * Modularizarlo
# * Hacer un prototipo para Editar el PDF de la ficha tecnica
# * Hacer la tabla de de para guardar los PDF
# * Implementar las OBSERVACIÓNES donde se pueda colocar Imagenes, sus comentarios y la secuencia de procesos de igual forma su Tabla en la bd

class verificaciones():
    def __init__(self,page):
        super().__init__()

        #self.page = page
        self.filter = filter().vrfPrintCard
        self.b1 = True
        self.page = page
        self.dataTbl = appFichVent()
        self.crtPdf = CreatePdf()

        self.tpl = []
        self.tpl2 = []
        self.bnd = 0
    
        #Inserción de todas las tablas#
        self.Insrt = appInserts(page)
    
    # Limpiar Labels
    def clean_fields(self,tpl):
        #tpl = self.tplInpts()
        for i in tpl:
            for j in i:
                j.value = ""
                j.update()
        self.page.update()


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
        print(tpl[2][6].items[0].content.controls)
        print(tpl[2][6].items[0].content.controls[0])
        # Obtener el valor de un PopupMenuItem HACERLO UNA FUNCIÓN
        # NOTAS : 
        # tpl[tbl][atr]     : [tbl] : la tabla que se va ha obtener ; [atr] : El atributo de la tabla
        # items[n]          : Agregar el Item que se desea Obtener 
        print("--->",tpl[2][6].items[0].content.controls[1].value)     
   
    def vlMnuPop(self, inx, tpl, j):
        print(len(tpl))      
      
        if self.bnd == inx:
            #print(f"id : {self.bnd}  :  {j}")
            self.tpl2.append(self.bnd)
        else:
              # Añade el último conjunto antes de vaciar self.tpl2 y cambiar self.bnd
            if self.tpl2:
                print(self.tpl2)
                #tpl.append(tuple(self.tpl2))
                #self.tpl2 = []
            self.bnd = inx
    
        #print(tuple(self.tpl))
            
    def dic(self,inx,tpl,j):
        # NOTA : El post solo acepta arreglos NO iteraci+ón
        funciones = {
            0: self.vlMnuPop,
            1: self.vlMnuPop,
            2: self.vlMnuPop,
           # 3: self.vlMnuPop, # Elemento NO funcional por bug
        }
        funcion = funciones.get(inx)
        if funcion:
            funcion(inx,tpl,j)
        else:
            print(f"No hay función definida para el índice {inx}")

    # Valida cada una de las entradas del formulario
    def vlVoid(self,tpl):           # Función que verifica si al Inicio del Fromulario los campos estan vaciós para evitar inserción de campos vacios
       # tpl = self.tplInpts()
        vlVoid = []      # Recolecta campos vaciós
        vlErr = []         
        sr = None
        
        # -- MODULARIZAR --
        for indx,i in enumerate(tpl):       # Recorre las listas de Inputs
            for j in i:                     # Recorre los valores de cada lista
                if isinstance(j, list):     # Verifica si el valor de la lista hay listas, para colocar los valores en la lista padre
                    for f in j:             # Recorre la sub lista desde el indice
                        if isinstance( f, PopupMenuButton):
                            for m in f.items:
                                txtFld = m.content.controls[1]
                                if txtFld.value != "":
                                    if txtfld.error_text !="":
                                        print(txtfld.label)
                                        vlErr.append(txtfld.label)       # Captura los campos vacios
                                    continue
                                else:
                                    txtfld.error_text = "Ingrese los valores"
                                    print(txtfld.label)
                                    vlVoid.append(txtfld.label)
                                    m.content.update()
                    continue
                else:
                    if isinstance(j, PopupMenuButton):
                        for k in j.items:
                            txtfld =  k.content.controls[1]
                            if txtfld.value != "":
                                if txtfld.error_text !="":
                                    print(txtfld.label)
                                    vlErr.append(txtfld.label)       # Captura los campos vacios
                                continue
                            else:
                                txtfld.error_text = "Ingrese los valores"
                                print(txtfld.label)
                                vlVoid.append(txtfld.label)
                                k.content.update()
        
                            #print(k.content.controls[1].value)
                    else:
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
        
    # Inserta los datos a la base de datos
    def insrtFicha(self,*data):
        #b1 = self.vlVoid(tpl)
        #print(b1) <-- bromita de 1 hora XD

        if self.vlVoid(data) != False:                   # Si ninguna validación se cumple
            contact_exists = False
            for row in self.dataTbl.get_row_Table():    # Recorre la tabla FichaTecnica ya que es la tabla padre       
                if row[0] == data[0][0].value:           # La primera tabla FichaTecnica contiene el ID asi que de la tupa toma el [FichaTec][Id]
                    contact_exists = True
                    break
                #### ARREGLAR ESTE PINCHE DESMADRE ####

            if not contact_exists:
                self.Insrt.qryPost(data)        # Insertar en bd
                #print(value)
                #self.crtPdf.jer(value) 
                #value = []

                ### VALORES DE LOS INPUTS ###
                #self.crtPdf.Insert(data)         # Crear el prindCard       
                #############################
                self.msgDlt = SnackBar(         # Insert exitoso!
                    content=Column(
                        controls=[
                            Container(
                                Text(f"PRODUCTO : {data[0][0].value} , INSERTADO CON EXITO!",size=20,color="white"),
                                alignment=alignment.center
                            ),
                        ],
                    ),
                    bgcolor="#5AE590",
                )
                self.open_dialog(self.msgDlt,self.page)
                lambda _: self.page.go('/cratePrindCard'),
                #self.clean_fields(data)
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