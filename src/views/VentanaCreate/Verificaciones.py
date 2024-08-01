from flet import *
from src.app.filExcel.filtroExcel import filter
from src.Controllers.appFichVent import appFichVent
from src.Controllers.appExtr import appExtr
from src.Controllers.appImpr import appImpr
from src.Controllers.appLam import appLam

#from src.views.VentanaCreate.createFicha.createPdf import CreatePdf

# Librerias de Prueba con los inputs 
#from src.views.VentanaCreate.InptsForm.Inpts_FichaTecVentas import Inpts_FichaTec_Ventas

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
        self.dtaExtr = appExtr()
        self.dtaImpr = appImpr()
        self.dtaLam = appLam()

        self.tpl = []
        self.tpl2 = []
        self.bnd = 0
    
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
    
    
    def prImprs(slef,*tpl):
        for indx,i in enumerate(tpl):
            for j in i:
                if isinstance(j, PopupMenuButton):
                    for k in j.items:
                        print(k.content.label)
    
    # --- MODULARIZAR ESTE METODO --- 
    def pru(self,*tpl):                     # Recorre las listas de Inputs para colocarlas en una lista
        #vle = tpl[2][0].items[0].content.controls[1].value
        for indx,i in enumerate(tpl):       # Recorre las listas de Inputs
            for j in i:                     # Recorre los valores de cada lista
                if isinstance(j, list):     # Verifica si el valor de la lista hay listas, para colocar los valores en la lista padre
                    for f in j:             # Recorre la sub lista desde el indice
                        if isinstance( f, PopupMenuButton):
                            for m in f.items:
                                txtFld = m.content.controls[1]
                                #print("--- **** ", txtFld.label)
                                self.tpl2.append(txtFld.value)
                        else:
                            #print(f" --xx {f.label}")
                            self.tpl2.append(f.value)
                        #print("-->" ,f) 
                    continue
                if isinstance(j, PopupMenuButton):
                    for k in j.items:
                        txtFld = k.content.controls[1]
                        #print("--- **** ", txtFld.label)
                        self.tpl2.append(txtFld.value)
                else:
                    #print(f" --xx {inx}  : {j.label} : {j.value}")
                    self.tpl2.append(j.value)
            
        #-- INSERCIÓN --#
        je = self.tpl2[108:] # Laminación
        #print(je)
        #print(self.tpl2)
        print(je)
        
        #'''        # --- INSERCIÓN POR REBANADAS ---   
            # --- FICHA --- 
        self.dataTbl.post_data(*self.tpl2[:5])
            # --- VENTAS ---
        self.dataTbl.post_dataVentas(self.tpl2[0],*self.tpl2[5:10])
            # --- EXTRUCIÓN ---
        self.dtaExtr.postExtr(self.tpl2[0],*self.tpl2[10:24])                  # TABLA PADRE EXTEUSIÓN
        self.dtaExtr.postCalibrePel_Tolr(self.tpl2[0],*self.tpl2[24:26])       # Calibre_Tol
        self.dtaExtr.postAnchoBob_Tolr(self.tpl2[0],*self.tpl2[26:28])         # Calibre_Tol
        self.dtaExtr.postAnchoCore_Tolr(self.tpl2[0],*self.tpl2[28:30])        # Calibre_Tol
        self.dtaExtr.postDiametroBob_Tolr(self.tpl2[0],*self.tpl2[30:32])      # Calibre_Tol
        self.dtaExtr.postPeso_Prom_Bob(self.tpl2[0],*self.tpl2[32:34])         # Calibre_Tol
        self.dtaExtr.postNum_BobCama_CamTam(self.tpl2[0],*self.tpl2[34:36])    # Calibre_Tol
        self.dtaExtr.postPeso_prom_tarima(self.tpl2[0],*self.tpl2[36:38])      # Calibre_Tol
             # --- IMPRESION ---
        self.dtaImpr.postImprs(self.tpl2[0],*self.tpl2[38:57])                  # TABLA PADRE IMPRESION
        self.dtaImpr.postVldClr(self.tpl2[0],*self.tpl2[57:59])  
        self.dtaImpr.postCalMater_Tolr(self.tpl2[0],*self.tpl2[59:61])  
        self.dtaImpr.postAnchoBobImpr_Tolr(self.tpl2[0],*self.tpl2[61:63])  
        self.dtaImpr.postAnchoCore_TolrImpr(self.tpl2[0],*self.tpl2[63:65])  
        self.dtaImpr.postAnchoDiamBob_Tolr(self.tpl2[0],*self.tpl2[65:67])  
        self.dtaImpr.postPesoPromBob(self.tpl2[0],*self.tpl2[67:69])  
        self.dtaImpr.postNum_BobCama_CamaTarima(self.tpl2[0],*self.tpl2[69:71])  
        self.dtaImpr.postPeso_prom_tarimaImpr(self.tpl2[0],*self.tpl2[71:73]) 
            # --- LAMINADO ---
        self.dtaLam.postLam(self.tpl2[0],*self.tpl2[73:80])
        self.dtaLam.postMedidManga(self.tpl2[0],*self.tpl2[80:82])
        self.dtaLam.postAnchoCore_TolrLam(self.tpl2[0],*self.tpl2[82:84])
        self.dtaLam.postDiametro_GrosCore(self.tpl2[0],*self.tpl2[84:86])
        self.dtaLam.postDiametro_Bob_Tolr(self.tpl2[0],*self.tpl2[86:88])

                        # - Material Impreso -
        self.dtaLam.postMaterial_Impreso(self.tpl2[0],*self.tpl2[88:90]) 
        self.dtaLam.postCalibrePelic_Tolr(self.tpl2[0],*self.tpl2[90:92]) 
        self.dtaLam.postAnchoBob_TolrMtrlr(self.tpl2[0],*self.tpl2[92:94])  
                        # - Lam #1 -
        self.dtaLam.postMaterial_Laminar_1(self.tpl2[0],*self.tpl2[94:97])  
        self.dtaLam.postCalibrePelic_TolrLam1(self.tpl2[0],*self.tpl2[97:99])  
        self.dtaLam.postAnchoBob_TolrLam1(self.tpl2[0],*self.tpl2[99:101])
                        # - Lam #2 -
        self.dtaLam.postMaterial_Laminar_2(self.tpl2[0],*self.tpl2[101:104])  
        self.dtaLam.postCalibrePelic_TolrLam2(self.tpl2[0],*self.tpl2[104:106])  
        self.dtaLam.postAnchoBob_TolrLam2(self.tpl2[0],*self.tpl2[106:108])  
                         # - Lam #3 -
        self.dtaLam.postMaterial_Laminar_3(self.tpl2[0],*self.tpl2[108:111])  
        self.dtaLam.postCalibrePelic_TolrLam3(self.tpl2[0],*self.tpl2[111:113])  
        self.dtaLam.postAnchoBob_TolrLam3(self.tpl2[0],*self.tpl2[113:115])  #'''
                         # - Lam #4 -
        self.dtaLam.postMaterial_Laminar_4(self.tpl2[0],*self.tpl2[115:118])  
        self.dtaLam.postCalibrePelic_TolrLam4(self.tpl2[0],*self.tpl2[118:120])  
        self.dtaLam.postAnchoBob_TolrLam4(self.tpl2[0],*self.tpl2[120:122])  #'''


        self.tpl2 = []

        
    def vlVoid(self,tpl):           # Función que verifica si al Inicio del Fromulario los campos estan vaciós para evitar inserción de campos vacios
       # tpl = self.tplInpts()
        vlVoid = []      # Recolecta campos vaciós
        vlErr = []         
        sr = None
        
        for i in tpl:
            for j in i:
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
     # Recorre el conjunto de tuplas
                
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
                #self.pru(tpl)
                #values = [field.value for field in tpl[0]]
                #self.dataTbl.post_data(*values)
                
                ### VALORES DE LOS INPUTS ###
                #self.crtPdf.Inser(tpl)
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