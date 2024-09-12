from flet import *
#from src.Controllers.appdb import appDb

from src.app.filExcel.filtroExcel import filter
from src.Controllers.appInserts import appInserts
from src.Controllers.appUpdate import appUpdate
from src.Controllers.appUpdateMsv import appUpdateMasivo     # <- UPDATE MASIVO
from src.Controllers.appFichVent import appFichVent
from src.views.VentanaCreate.createFicha.createPdf import CreatePdf
from src.views.VentanaCreate.Mdls import Mdls
from src.pruebas.pru2 import FileUploaderApp
from src.views.VentanaCreate.InptsForm.InpstAux import InptsAux

class verificaciones():
    def __init__(self,page):
        super().__init__()
        # EXPRECIÓNES REGULARES # 
        self.filter = filter().vrfPrintCard
        self.page = page
        # QURY DE TABLA FICHA / VENTAS
        self.dataTbl = appFichVent
        # BTN LABEL INSRT / UPDATE
        self.aux = InptsAux
        # CREA LOS PDF #
        self.crtPdf = CreatePdf(page)

        self.tpl = []
        self.tpl2 = []
 
        #Inserción de todas las tablas#
        self.Insrt = appInserts
        # UPDATE DE LAS TABLAS#
        self.Update = appUpdate
        # UPDATE MASIVE
        self.UpdtMsv = appUpdateMasivo

        #Abrir y Cerrar Modales
        self.mdl = Mdls(page)

###### PRUEBAS PARA FILTRADO ###########
    def verInpts(self,e,rejex):
        inpt = e.control
        jer = len(e.control.value)
        trimmed_value = inpt.value.strip()
        #print(jer)
        if jer != 0 and trimmed_value:      # trimed_value : localiza espacios en blanco 
            if rejex(inpt.value):
                #print(f"{inpt.label}  : {inpt.value}")
                inpt.border_color="green"
                inpt.error_text=""
            else:
                #inpt.border_color="red"
                inpt.error_text=f"{inpt.label} Incorrecto!"
                #print("Incorrecto")
        else:
            #e.control.border_color="red"
            inpt.error_text="Favor de ingresar un valor!"
            self.page.update()
            #print("Campo Vacio")

        inpt.update()  # Actualiza el control para reflejar los cambios
        #'''
######################################################

###### INSERCIÓN A LA BASE DE DATOS ##########################
            
    # Valida cada una de las entradas del formulario
    def vlVoid(self,tpl):           # Función que verifica si al Inicio del Fromulario los campos estan vaciós para evitar inserción de campos vacios
        #pass
        #'''
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
                                        #print(txtfld.label)
                                        vlErr.append(txtfld.label)       # Captura los campos vacios
                                    continue
                                else:
                                    txtfld.error_text = "Ingrese los valores"
                                    #print(txtfld.label)
                                    vlVoid.append(txtfld.label)
                                    m.content.update()
                    continue
                else:
                    if isinstance(j, PopupMenuButton):
                        for k in j.items:
                            txtfld =  k.content.controls[1]
                            if txtfld.value != "":
                                if txtfld.error_text !="":
                                    #print(txtfld.label)
                                    vlErr.append(txtfld.label)       # Captura los campos vacios
                                continue
                            else:
                                txtfld.error_text = "Ingrese los valores"
                                #print(txtfld.label)
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
                    title= Container(
                        #border= border.only(bottom=border.BorderSide(1, "black")),
                        shadow=BoxShadow(
                            spread_radius=0,
                            blur_radius=10,
                            offset=Offset(0, 4),  # Ajusta el desplazamiento de la sombra
                            color=colors.BLACK12,  # Cambia el color si es necesario
                        ),
                        content= Text(
                            "FALTAN CAMPOS POR LLENAR!",
                            color="black",
                            text_align="center",
                        ),
                    ),
                    bgcolor="ddddddcf",
                    actions=[
                        TextButton("CERRAR", on_click= lambda e: self.mdl.close_dialog(self.mdlVoidVl))
                    ]
                )
            self.mdl.open_dialog(self.mdlVoidVl)
            return False
        
        elif len(vlErr) > 0:
            self.mdlErrValue = AlertDialog(
                    modal=True,
                    title= Text(f"Los valores en {vlErr} , Son incorrectos!"),
                    actions=[
                        TextButton("CERRAR", on_click=lambda _: self.mdl.close_dialog(self.mdlErrValue))
                    ]
                )
            #self.mdl.open_Cntndr(self.cnt)
            self.mdl.open_dialog(self.mdlErrValue)
            return False
        else : 
            return True
        #'''

    # Inserta los datos a la base de datos
    def insrtFicha(self,*data):
       
        if self.vlVoid(data) != False:                   # Si ninguna validación se cumple
            contact_exists = False
            for row in self.dataTbl().get_row_Table():    # Recorre la tabla FichaTecnica ya que es la tabla padre       
                if row[0] == data[0][0].value:           # La primera tabla FichaTecnica contiene el ID asi que de la tupa toma el [FichaTec][Id]
                    contact_exists = True
                    break
             
            # --- INSERT ---
            if self.aux().changeBtn(self.page.client_storage.get("estado")) == "Ingresar":
                if not contact_exists: # SI NO EXISTE EN LA BD INSERTA!
                    
                    #  -- INSERTAR EN DB -- 
                    self.Insrt().qryPost(data)

                    #  -- INSERTAR TEXTO AL PDF -- 
                    self.crtPdf.InsertTxt(data)
        
                    self.msgInsrt = SnackBar(         # Insert exitoso!
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
                    #self.mdlErrValue(self.msgDlt)
                    self.mdl.open_dialog(self.msgInsrt)
                    #lambda _: self.page.go('/cratePrindCard'),

                else:  # YA EXISTE! EVITA REGISTROS DUPLICADOS
                    self.mdlDplctPrdct = AlertDialog(   # MODAL PRODUCTO DUPLICADO
                        modal=True,
                        title= Text(f"El Producto : {row[0]} ya Existe!"),
                        actions=[
                            TextButton("CERRAR", on_click=lambda e: self.mdl.close_dialog(self.mdlDplctPrdct))
                        ]
                    )
                    #self.msgDlt(self.mdlDplctPrdct)
                    self.mdl.open_dialog(self.mdlDplctPrdct)
                    return False
            # UPDATE   
            elif self.aux().changeBtn(self.page.client_storage.get("estado")) == "Update":
                if not contact_exists: 
                    self.mdlDplctPrdct = AlertDialog(   # MODAL PRODUCTO DUPLICADO
                        modal=True,
                        title= Text(f"El Producto : {row[0]} No Existe!"),
                        actions=[
                            TextButton("CERRAR", on_click=lambda e: self.mdl.close_dialog(self.mdlDplctPrdct))
                        ]
                    )
                    #self.msgDlt(self.mdlDplctPrdct)
                    self.mdl.open_dialog(self.mdlDplctPrdct)
                    return False
                else:
                    # UPDATE IN DB
                    self.Update().qryUpdate(data) 
                    
                    # INSERTAR TEXTO EN PDF
                    self.crtPdf.InsertTxt(data)

                    self.msgInsrt = SnackBar(         # Insert exitoso!
                        content=Column(
                            controls=[
                                Container(
                                    Text(f"PRODUCTO : {data[0][0].value} , ACTUALIZADO CON EXITO!",size=20,color="white"),
                                    alignment=alignment.center
                                ),
                            ],
                        ),
                        bgcolor="#5AE590",
                    )
                    #self.mdlErrValue(self.msgDlt)
                    self.mdl.open_dialog(self.msgInsrt)#'''
            
            # UPDATE MASIVO
            else:                   # <- CLAVE UPDATE MSV
                listPridCards = self.page.client_storage.get("id_masivo")
                
                ids_codProduct = ','.join(listPridCards)    # CONVIERTE LA LISTA EN UNA CADENA SEPARA POR COMAS
                print(ids_codProduct)
                
                self.UpdtMsv().qryUpdateMsv(data,ids_codProduct) 
                
                # INSERTAR TEXTO EN PDF
                #self.crtPdf.InsertTxt(data)  # <- trabajar las actualizaciónes masivas en los PDF

                self.msgInsrt = SnackBar(         # Insert exitoso!
                    content=Column(
                        controls=[
                            Container(
                                #Text(f"PrindCards {cliente} Actualizados!",size=20,color="white"),
                                Text(f"PrindCards Actualizados!",size=20,color="white"),
                                alignment=alignment.center
                            ),
                        ],
                    ),
                    bgcolor="#5AE590",
                )
                #self.mdlErrValue(self.msgDlt)
                self.mdl.open_dialog(self.msgInsrt)#'''