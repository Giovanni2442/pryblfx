import fitz  # PyMuPDF
from src.Controllers.appSec import appSec

class prInrs:
    def __init__(self,page):
        self.page = page
        template = "Template/Template.pdf"
        self.doc = fitz.open(template)                      # Asegúrate de abrir el PDF correcto
        self.text_color = (0,0,0)                           # Color del texto
        self.fill_color = (0.75, 0.75, 0.75)                # Color de fondo
        self.Text_PrdctTerm = 14.7                          # Tamaño de la fuente de Producto terminado
        self.text_size = 24   
        self.color = (0.25, 0.25, 0.25)                     # Color gris claro, con valores RGB entre 0 y 1
        self.lstSec = ['N/A','N/A','N/A','N/A','N/A']       # Lista de secuencias para almacenar en la BD
        self.estd = self.page.client_storage.get("estado")

        # Controlador secuencias de procesos#
        self.appSec = appSec

    def pdfProcExtrs(self,page,Proceso,bnd,fuente):
            ## -- PROCESO  EXTRS -- ##
        rectExtrs = fitz.Rect(880, 810, 1045, 865)  # Img. Extrusión
        page.draw_rect(rectExtrs, color=self.color, fill = self.fill_color)

                ## -- AGREGAR TEXTO -- ##
        page.insert_textbox(rectExtrs,f"{Proceso}", fontsize=fuente, fontname="helv", color=self.text_color, align=1)       # EN POSICIÓN [1] SE ENCIENTRA EL NUM. FIGURA

        if bnd != False:
            ## -- FLECHA EXTRUSION -- ##
            arrwExtrs = [
            # X , Y
            fitz.Point(955,870),  # punta Izq de la Base SUPERIOR    P1
            fitz.Point(975,870),  # punta derch de la Base SUPERIOR  P2
            fitz.Point(975,880),  # Base derecha   INFERIOR          P3
            fitz.Point(985,880),  # Punta derecha de la flecha       P4
            fitz.Point(965,890),  # Punta de la flecha (INFERIOR)    P5
            fitz.Point(945,880),  # Punta izquierda de la flecha     P6   
            fitz.Point(955,880),  # Base izquierda INFERIOR          P7
            ]

            # Dibuja el polígono con los puntos especificados
            page.draw_polyline(arrwExtrs, color=self.color, fill=self.color) 

    def pdfProcImprs(self,page,Proceso,bnd,fuente):
                ## -- PROCESO IMPRS -- ##
        rectImprs = fitz.Rect(880, 895, 1045, 950)  # Img. Extrusión
        page.draw_rect(rectImprs, color=self.color , fill=self.fill_color)

                ## -- AGREGAR TEXTO -- ##
        page.insert_textbox(rectImprs,Proceso, fontsize=fuente, fontname="helv", color=self.text_color, align=1)       # EN POSICIÓN [1] SE ENCIENTRA EL NUM. FIGURA

    
        if bnd != False:
            ## -- FLECHA EXTRUSION -- ##
            arrwImprs = [
                # X , Y
                fitz.Point(955,955),  # punta Izq de la Base SUPERIOR    P1
                fitz.Point(975,955),  # punta derch de la Base SUPERIOR  P2
                fitz.Point(975,965),  # Base derecha   INFERIOR          P3
                fitz.Point(985,965),  # Punta derecha de la flecha       P4
                fitz.Point(965,975),  # Punta de la flecha (INFERIOR)    P5
                fitz.Point(945, 965),  # Punta izquierda de la flecha     P6   
                fitz.Point(955,965),  # Base izquierda INFERIOR          P7
            ]

            # Dibuja el polígono con los puntos especificados
            page.draw_polyline(arrwImprs, color=self.color, fill=self.color) 

    def pdfProcLam(self,page,Proceso,bnd,fuente):
                 ## -- PROCESO rectangulo -- ##
        rectLam = fitz.Rect(880, 975, 1045, 1030)  # Img. Extrusión
        page.draw_rect(rectLam, color=self.color, fill=self.fill_color)
            
                    ## -- AGREGAR TEXTO -- ##
        page.insert_textbox(rectLam, Proceso, fontsize=fuente, fontname="helv", color=self.text_color, align=1)       # EN POSICIÓN [1] SE ENCIENTRA EL NUM. FIGURA

        if bnd != False:
            ## -- FLECHA EXTRUSION -- ##
            arrwImprs = [
                # X , Y
                fitz.Point(955,1035),  # punta Izq de la Base SUPERIOR    P1
                fitz.Point(975,1035),  # punta derch de la Base SUPERIOR  P2
                fitz.Point(975,1045),  # Base derecha   INFERIOR          P3
                fitz.Point(985,1045),  # Punta derecha de la flecha       P4
                fitz.Point(965,1055),  # Punta de la flecha (INFERIOR)    P5
                fitz.Point(945, 1045),  # Punta izquierda de la flecha     P6   
                fitz.Point(955,1045),  # Base izquierda INFERIOR          P7
            ]

            # Dibuja el polígono con los puntos especificados
            page.draw_polyline(arrwImprs, color=self.color, fill=self.color) 

    def pdfProcRef(self,page,Proceso,bnd,fuente):
                ## -- PROCESO rectangulo -- ##
        rectRefil = fitz.Rect(880, 1055, 1045, 1110)  # Img. Extrusión
        page.draw_rect(rectRefil, color=self.color, fill=self.fill_color)
                
                    ## -- AGREGAR TEXTO -- ##
        page.insert_textbox(rectRefil, Proceso, fontsize=fuente, fontname="helv", color=self.text_color, align=1)       # EN POSICIÓN [1] SE ENCIENTRA EL NUM. FIGURA

        if bnd != False:
            ## -- FLECHA EXTRUSION -- ##
            arrwImprs = [
                # X , Y
                fitz.Point(955,1115),  # punta Izq de la Base SUPERIOR    P1
                fitz.Point(975,1115),  # punta derch de la Base SUPERIOR  P2
                fitz.Point(975,1125),  # Base derecha   INFERIOR          P3
                fitz.Point(985,1125),  # Punta derecha de la flecha       P4
                fitz.Point(965,1135),  # Punta de la flecha (INFERIOR)    P5
                fitz.Point(945, 1125),  # Punta izquierda de la flecha     P6   
                fitz.Point(955,1125),  # Base izquierda INFERIOR          P7
            ]

            # Dibuja el polígono con los puntos especificados
            page.draw_polyline(arrwImprs, color=self.color, fill=self.color) 
    
    def pdfProcCnvrs(self,page,Proceso,bnd,fuente):
                ## -- PROCESO rectangulo -- ##
        rectCnvrs = fitz.Rect(880, 1135, 1045, 1190)  # Img. Extrusión
        page.draw_rect(rectCnvrs, color=self.color, fill=self.fill_color)
                
                ## -- AGREGAR TEXTO -- ##
        page.insert_textbox(rectCnvrs, Proceso, fontsize=fuente, fontname="helv", color=self.text_color, align=1)       # EN POSICIÓN [1] SE ENCIENTRA EL NUM. FIGURA
        
        if bnd != False:
            ## -- FLECHA EXTRUSION -- ##
            arrwImprs = [
                # X , Y
                fitz.Point(955,1195),  # punta Izq de la Base SUPERIOR    P1
                fitz.Point(975,1195),  # punta derch de la Base SUPERIOR  P2
                fitz.Point(975,1205),  # Base derecha   INFERIOR          P3
                fitz.Point(985,1205),  # Punta derecha de la flecha       P4
                fitz.Point(965,1215),  # Punta de la flecha (INFERIOR)    P5
                fitz.Point(945, 1205),  # Punta izquierda de la flecha     P6   
                fitz.Point(955,1205),  # Base izquierda INFERIOR          P7
            ]

            # Dibuja el polígono con los puntos especificados
            page.draw_polyline(arrwImprs, color=self.color, fill=self.color) 

    def pdfProcPrdctTerm(self,page):
                ## -- PROCESO rectangulo -- ##
        rectPrdctTerm = fitz.Rect(880, 1215, 1045, 1260)  # Img. Extrusión
        page.draw_rect(rectPrdctTerm, color=self.color, fill=self.fill_color)

         ## -- AGREGAR TEXTO -- ##
        page.insert_textbox(rectPrdctTerm,"PRODUCTO TERMINADO", fontsize=14.7, fontname="helv", color=self.text_color, align=1)       # EN POSICIÓN [1] SE ENCIENTRA EL NUM. FIGURA
    
    # SECUENCIAS DEL PRINDCARD
    def pruSec(self,pagePdf,idpdf):
        dicObsrvc = self.page.client_storage.get("id_Img")
        count = 0 # ACOMULA EL ULTIMO EL ULTIMO VALOR DE LA SECUENCIA
        # DICCIÓNARIO DONDE ACCEDE A LAS COORDENADAS DE SECUENCIAS
        pdfPros = {
            0 : self.pdfProcExtrs,
            1 : self.pdfProcImprs,
            2 : self.pdfProcLam,
            3 : self.pdfProcRef,
            4 : self.pdfProcCnvrs,
            5 : self.pdfProcPrdctTerm
        }

        # UPDATE
        if self.estd != "Insert":
            dataBd = self.appSec().transGetProceso(idpdf)[1:]
            #print(f"EL ID : {idpdf} TIENE -> {dataBd}")
            
            # Si preciono el boton de imagen en una de las secuencias, se reinicia
            if dicObsrvc: 
                for i,key in enumerate(dicObsrvc):
                    print("--SECUENCIAS---",i,key)
                    fun = pdfPros.get(i)
                    fun(pagePdf,key,True,self.text_size)
                    self.lstSec[i] = key
                    count=i
            
                print(count)
                #print(".-.",self.lstSec)
                # ASEGURA EN COLOCAR EL PRODUCTO TERMINADO AL FINAL DE CADA SECUENCIA
                if count != 4:
                    fun = pdfPros.get(count+1)
                    fun(pagePdf,"PRODUCTO TERMINADO",False,self.Text_PrdctTerm)
                else:
                    fun = pdfPros.get(5)
                    fun(pagePdf)

            # DIBUJA EL PROCESO LA DATA TRAIDA EN BD
            else: 
                for i,key in enumerate(dataBd):
                    if key != 'N/A':
                        fun = pdfPros.get(i)
                        fun(pagePdf,key,True,self.text_size)
                        self.lstSec[i] = key
                        count=i
                        #count=i
                print(count)
                #print(".-.",self.lstSec)
                # ASEGURA EN COLOCAR EL PRODUCTO TERMINADO AL FINAL DE CADA SECUENCIA
                if count != 4:
                    fun = pdfPros.get(count+1)
                    fun(pagePdf,"PRODUCTO TERMINADO",False,self.Text_PrdctTerm)
                else:
                    fun = pdfPros.get(5)
                    fun(pagePdf)
        # INSERT
        else:
            # SI EL DICCIÓNARIO "NO" ESTA VACIO..
            if dicObsrvc:
                #'''
                for i,key in enumerate(dicObsrvc):
                    print("--SECUENCIAS---",i,key)
                    fun = pdfPros.get(i)
                    fun(pagePdf,key,True,self.text_size)
                    self.lstSec[i] = key
                    count=i
                
                print(count)
                #print(".-.",self.lstSec)
                # ASEGURA EN COLOCAR EL PRODUCTO TERMINADO AL FINAL DE CADA SECUENCIA
                if count != 4:
                    fun = pdfPros.get(count+1)
                    fun(pagePdf,"PRODUCTO TERMINADO",False,self.Text_PrdctTerm)
                else:
                    fun = pdfPros.get(5)
                    fun(pagePdf)
                    
            # DICCIÓNARIO VACIÓ EN SECUENCIAS
            else : 
                print("VACIO!")
                fun = pdfPros.get(5)
                fun(pagePdf)
        return self.lstSec
    
# Ejecuta la prueba
#crpdf = prInrs()
#crpdf.pruebas()