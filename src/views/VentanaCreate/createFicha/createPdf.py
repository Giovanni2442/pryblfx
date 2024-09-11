import fitz  # PyMuPDF
import shutil
from PIL import Image
from flet import *  
import os
import io

from src.views.VentanaCreate.createFicha.Insrt_FichaVentas import Insrt_FichaVentas
from src.views.VentanaCreate.createFicha.Insrt_Extr import Insrt_Extr
from src.views.VentanaCreate.createFicha.Insrt_Impr import Insrt_Impr
from src.views.VentanaCreate.createFicha.Insrt_Laminado import Insrt_Laminado
from src.views.VentanaCreate.createFicha.Insrt_Refilado import Instr_Refilado
from src.views.VentanaCreate.createFicha.Insrt_Convrs import Insrt_Convrs
from src.views.VentanaCreate.createFicha.InsrtImgs import InstrImgs
from src.Controllers.appPrindCard import appPrindCard

#### TAREAS ###
# * Obtener los datos de la bd
# * Configurar las Coordenadas para cada elemento de las tablas (Minimo llegar a Extrusión)
# * crear tabla para almacenar los PDF y asi obtenerlos
# * Agregar un boton desde el conjunto de Herramientas para visualizar el PrindCard creado 

# src\views\VentanaCreate\createFicha\Template

class CreatePdf():
    def __init__(self,page):
        self.page = page
        self.pdfFichVent = Insrt_FichaVentas()
        self.pdfExtr = Insrt_Extr()
        self.pdfImpr = Insrt_Impr()
        self.pdfLam = Insrt_Laminado()
        self.pdfRef = Instr_Refilado()
        self.pdfCnvrs = Insrt_Convrs()
        self.pdfImg = InstrImgs(self.page)

        self.tmpl = "Template/Template.pdf"

        #self.tmpl = "C:/Users/csanchez/Desktop/pryblfx/venv/src/views/VentanaCreate/createFicha/Template/Template.pdf"
        self.doc = fitz.open(self.tmpl)

        # ESTADO IDENTIFICADOR DE INSERT Y UPDATE
        self.estd = self.page.client_storage.get("estado")
        # ID DEL PRODUCTO HA EDITAR
        self.id = self.page.client_storage.get("id")


        # -- ELEMENTOS DE PRUEBA --
        self.tplImg={} 
        self.dta = []       # ALMACENA LOS DATOS QUE SE VAN A INGRESAR EN LA BD

        ########################### 

        # ADD TO DATABASE
        self.postpdf = appPrindCard
        # PAGINA "0" DEL PDF
        self.pagPdf = self.doc[0]
        
    # agregar tpl
    #def InsertImg(self,id,dicImg):
    def InsertImg(self):
        #print(dicImg)
        #### -- PREUBAS PARA IMAGEN -- #####
        #self.pdfImg.main(self.page,id,dicImg)
        self.pdfImg.main2(self.pagPdf)
        #self.Btnid = dicImg
        #print(self.Btnid)
        self.temp_filename = "Template/Template_temp.pdf"
        self.doc.save(self.temp_filename)

    def InsertTxt(self,tpl):
    #def Insert(self):
        # Ejemplo: añadir texto en la primera página
        #txtFld = tpl[2][15]items[0].content.controls[1].value
        #print(tpl[5])
        idpdf = tpl[0][0].value

        #'''
        #### -- TABLA EXTRUSIÓN -- #####       
        self.pdfFichVent.pdfFichVent(self.pagPdf,tpl)
        #### -- TABLA EXTRUSIÓN -- #####       
        self.pdfExtr.pdfExtru(self.pagPdf,tpl)
        #### -- TABLA IMPRESION -- #####       
        self.pdfImpr.pdfImpr(self.pagPdf,tpl)
        #### -- TABLA LAMINADO -- #####
        self.pdfLam.pdfLam(self.pagPdf,tpl)
        #self.pdfLam.pru(tpl)
        #### -- TABLA REFILADO -- #####
        self.pdfRef.pdfRefil(self.pagPdf,tpl)
        #### -- TABLA CONVERSIÓN -- #####
        self.pdfCnvrs.pdfConvrs(self.pagPdf,tpl)#'''

        # -- LISTA DE  IMAGENES --# 
        lstImg = self.pdfImg.main2(self.pagPdf,idpdf)
        print("IMG --",lstImg)      # <- EYY! Q CHECA LA LISTA
        #self.pdfImg.main(self.page,tpl)

        for pros in lstImg:       # Recorre el proceso
            for lst in pros:
                #print("--.i.- ",lst)
                self.dta.append(lst)

        self.pdf = f"FilePdf/{idpdf}.pdf"
        self.doc.save(self.pdf)

        # pdf : Url y nombre donde se guarda el pdf
        # idpdf : Id del Prindcard
        # 
        #print("--INSERTA AQUI -- : ",self.dta)
        self.postPdfLOCAL(idpdf,self.pdf,self.dta) # ----- MOVERLE A ESTE PEDO

        ###########################################################################################

        ###### INSERCIÓN DESDE LA BASE DE DATOS (MINIMISA EL RENDEMIENTO EN BD) ###########

        #self.pdfImg.main(self.page,tpl)
        #self.temp_filename = "Template/Template_temp.pdf"
        #self.doc.save(self.temp_filename)

        '''
        ####Prueba sin archivos Temporales####
        pdf_buffer = io.BytesIO()               # Transforma el archivo en Bytes
        self.doc.save(pdf_buffer)
        pdf_binary = pdf_buffer.getvalue()      # Archivo Binario
        #self.postpdf().postPridCardPdf(tpl[0][0].value,pdf_binary)

        if self.id != "Insert":
            # UPDATE
            self.postpdf().transctUpdatePrindCard(pdf_binary,tpl[0][0].value)
            self.doc.close()
        else:
            # INSERT
            self.postpdf().transctInsertPrindCard(tpl[0][0].value,pdf_binary)
            self.doc.close()#'''
        
        ###########################################################################################
        
        # --- FUNCIÓN POST PDF ----
        #self.postPdf(pdf_binary,idpdf)

    def postPdfSQL(self,pdf,id_pdf):
        if self.estd != "Insert":
            # UPDATE
            self.postpdf().transctUpdatePrindCard(pdf,id_pdf)
            self.doc.close()
        else:
            # INSERT
            self.postpdf().transctInsertPrindCard(id_pdf,pdf)
            self.doc.close()#'''

    def postPdfLOCAL(self,id_pdf,url_pef,dta):
        if self.estd != "Insert":
                    # UPDATE
            # IMAGENES  =       [:15:3]
            # FIGURAS   =       [1:15:3]
            # DESCRIPCIÓNES =   [2:15:3]
            self.postpdf().transctUpdatePrindCardLOCAL(url_pef,*dta[:15:3],*dta[1:15:3],*dta[2:15:3],id_pdf)
            self.doc.close()
            #print("PROXIMAMENTE!")
        else:
                    # INSERT
            # IMAGENES  =   [:15:3]
           # DESCRIPCIÓNES = [2:15:3]
             # FIGURAS   =   [1:15:3]
            self.postpdf().transctInsertPrindCardLOCAL(id_pdf,url_pef,*dta[:15:3],*dta[1:15:3],*dta[2:15:3])
            self.doc.close()#'''

class prInrs:
    def __init__(self):
        template = "Template/Template.pdf"
        self.doc = fitz.open(template)  # Asegúrate de abrir el PDF correcto
        self.text_color = (0,0,0)               # Color del Recuadro(ELIMINAR)
        self.text_size = 24    

    def pruebas(self):
        color = (0, 1, 0)  # Color gris claro, con valores RGB entre 0 y 1

        # Asegúrate de acceder a la página correcta del PDF
        page = self.doc[0]  # Cambia el índice a la página que necesites

        ########### PRUEBAS #################

         # Otro rectángulo para una imagen
        # X = Representa el ancho de la figura
        # Y = Altura de la figura
        # X1 , Y1 , X2 , Y2

 ############################EXTRUSION PROCESO############################################
                ## -- PROCESO rectangulo EXTRS -- ##
        rectExtrs = fitz.Rect(880, 810, 1045, 865)  # Img. Extrusión
        page.draw_rect(rectExtrs, color=color)

                ## -- AGREGAR TEXTO -- ##
        page.insert_textbox(rectExtrs,"EXTRUSION", fontsize=self.text_size, fontname="helv", color=self.text_color, align=1)       # EN POSICIÓN [1] SE ENCIENTRA EL NUM. FIGURA


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
        page.draw_polyline(arrwExtrs, color=color, fill=color) 
##########################################################################################

 ############################IMPRESION PROCESO############################################
                ## -- PROCESO rectangulo -- ##
        rectImprs = fitz.Rect(880, 895, 1045, 950)  # Img. Extrusión
        page.draw_rect(rectImprs, color=color)

                ## -- AGREGAR TEXTO -- ##
        page.insert_textbox(rectImprs,"IMPRECIÓN", fontsize=self.text_size, fontname="helv", color=self.text_color, align=1)       # EN POSICIÓN [1] SE ENCIENTRA EL NUM. FIGURA

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
        page.draw_polyline(arrwImprs, color=color, fill=color) 
##########################################################################################

 ############################LAMINADO PROCESO############################################
                ## -- PROCESO rectangulo -- ##
        rectLam = fitz.Rect(880, 975, 1045, 1030)  # Img. Extrusión
        page.draw_rect(rectLam, color=color)
            
                    ## -- AGREGAR TEXTO -- ##
        page.insert_textbox(rectLam,"LAMINADO", fontsize=self.text_size, fontname="helv", color=self.text_color, align=1)       # EN POSICIÓN [1] SE ENCIENTRA EL NUM. FIGURA

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
        page.draw_polyline(arrwImprs, color=color, fill=color) 
##########################################################################################

 ############################REFILADO PROCESO############################################
                ## -- PROCESO rectangulo -- ##
        rectRefil = fitz.Rect(880, 1055, 1045, 1110)  # Img. Extrusión
        page.draw_rect(rectRefil, color=color)
                
                    ## -- AGREGAR TEXTO -- ##
        page.insert_textbox(rectRefil,"REFILADO", fontsize=self.text_size, fontname="helv", color=self.text_color, align=1)       # EN POSICIÓN [1] SE ENCIENTRA EL NUM. FIGURA

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
        page.draw_polyline(arrwImprs, color=color, fill=color) 
##########################################################################################

 ############################CONVERSION PROCESO############################################
                ## -- PROCESO rectangulo -- ##
        rectCnvrs = fitz.Rect(880, 1135, 1045, 1190)  # Img. Extrusión
        page.draw_rect(rectCnvrs, color=color)
                
                ## -- AGREGAR TEXTO -- ##
        page.insert_textbox(rectCnvrs,"CONVERSIÓN", fontsize=self.text_size, fontname="helv", color=self.text_color, align=1)       # EN POSICIÓN [1] SE ENCIENTRA EL NUM. FIGURA
        
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
        page.draw_polyline(arrwImprs, color=color, fill=color) 
##########################################################################################

 ############################PROCESO TERMINADO############################################
                ## -- PROCESO rectangulo -- ##
        rectPrdctTerm = fitz.Rect(880, 1215, 1045, 1260)  # Img. Extrusión
        page.draw_rect(rectPrdctTerm, color=color)

         ## -- AGREGAR TEXTO -- ##
        page.insert_textbox(rectPrdctTerm,"TERMINADO", fontsize=self.text_size, fontname="helv", color=self.text_color, align=1)       # EN POSICIÓN [1] SE ENCIENTRA EL NUM. FIGURA
              
##########################################################################################

        # Guarda el documento modificado
        self.temp_filename = "Template/Template_temp.pdf"
        self.doc.save(self.temp_filename)
        self.doc.close()

# Ejecuta la prueba
crpdf = prInrs()
crpdf.pruebas()
