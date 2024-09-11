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
from src.views.VentanaCreate.createFicha.InsertSec import prInrs
from src.Controllers.appSec import appSec
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
        self.secProc = prInrs(self.page)
        self.pdfImg = InstrImgs(self.page)

        self.tmpl = "Template/Template.pdf"

        #self.tmpl = "C:/Users/csanchez/Desktop/pryblfx/venv/src/views/VentanaCreate/createFicha/Template/Template.pdf"
        self.doc = fitz.open(self.tmpl)

        # ESTADO IDENTIFICADOR DE INSERT Y UPDATE
        self.estd = self.page.client_storage.get("estado")
        # ID DEL PRODUCTO HA EDITAR
        self.id = self.page.client_storage.get("id")


        # -- ELEMENTOS DE PRUEBA --
        self.dta = []       # ALMACENA LOS DATOS QUE SE VAN A INGRESAR EN LA BD

        ########################### 

        # ADD TO DATABASE
        self.postpdf = appPrindCard
        self.postSecuencias = appSec
        # PAGINA "0" DEL PDF
        self.pagPdf = self.doc[0]
        

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


        # -- LISTA DE PROCESOS -- 
        lstProc = self.secProc.pruSec(self.pagPdf) 
  
        # -- LISTA DE  IMAGENES --# 
        lstImg = self.pdfImg.main2(self.pagPdf,idpdf)
        print("IMG --",lstImg)      # <- EYY! Q CHECA LA LISTA
        #self.pdfImg.main(self.page,tpl)

        for pros in lstImg:                 # KEY Recorre el proceso
            for lst in pros:                # VALUE DE CADA PROCESO
                #print("--.i.- ",lst)
                self.dta.append(lst)        # ADD VALUE EN LISTA

        # Guarda el nuevo pdf
        self.pdf = f"FilePdf/{idpdf}.pdf"
        self.doc.save(self.pdf)


        ############################ INSRCIÓNES A LA BD #######################
            # PROCESOS
        self.postSecuenciaPdf(idpdf,lstProc)

            # OBSERVACIÓNES
        # pdf : Url y nombre donde se guarda el pdf
        # idpdf : Id del Prindcard
        # 
        #print("--INSERTA AQUI -- : ",self.dta)
        self.postPdfLOCAL(idpdf,self.pdf,self.dta) # ----- MOVERLE A ESTE PEDO

        self.doc.close()
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
            #self.doc.close()
            #print("PROXIMAMENTE!")
        else:
                    # INSERT
            # IMAGENES  =   [:15:3]
           # DESCRIPCIÓNES = [2:15:3]
             # FIGURAS   =   [1:15:3]
            self.postpdf().transctInsertPrindCardLOCAL(id_pdf,url_pef,*dta[:15:3],*dta[1:15:3],*dta[2:15:3])
            #self.doc.close()#'''

    def postSecuenciaPdf(self,id_pdf,dta):
        print("PEDAZOS.-.-.",dta[:])
        print(id_pdf)
        #'''
        if self.estd != "Insert":
                    # UPDATE
            # IMAGENES  =       [:15:3]
            # FIGURAS   =       [1:15:3]
            # DESCRIPCIÓNES =   [2:15:3]
            self.postSecuencias().transUpdateProceso(*dta[:],id_pdf)
            #self.doc.close()
            #print("PROXIMAMENTE!")
        else:
                    # INSERT
            # IMAGENES  =   [:15:3]
           # DESCRIPCIÓNES = [2:15:3]
             # FIGURAS   =   [1:15:3]
            self.postSecuencias().transInsertProceso(id_pdf,*dta[:])
            #self.doc.close()#'''


        ### -- ADVERTENCIA - ESTA FUNCIÓN ES DE PRUEBAS Y ALIMENTA LA BD CON PDF --
    def InsertBd(self):  
            pass   
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
            self.doc.close()'''
            
            ###########################################################################################


# Ejecuta la prueba
#crpdf = prInrs()
#crpdf.pruebas()
