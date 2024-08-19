import fitz  # PyMuPDF
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
    def __init__(self):
        self.pdfFichVent = Insrt_FichaVentas()
        self.pdfExtr = Insrt_Extr()
        self.pdfImpr = Insrt_Impr()
        self.pdfLam = Insrt_Laminado()
        self.pdfRef = Instr_Refilado()
        self.pdfCnvrs = Insrt_Convrs()
        self.pdfImg = InstrImgs()

        tmpl = "Template/Template.pdf"
        self.doc = fitz.open(tmpl)

        # -- ELEMENTOS DE PRUEBA --
        self.tplImg={} 
        self.Btnid = None
        ########################### 

        # ADD TO DATABASE
        self.postpdf = appPrindCard()
        # PAGINA "0" DEL PDF
        self.page = self.doc[0]
        
    def jer(self,tpl):
        '''     
        for inx,i in enumerate(tpl):
            if isinstance(i, list):
                print(f"{inx} : {i}")
            else:
                continue'''
        #txtFld = tpl[4][11].items[0].content.controls[1].label
        txtFld = tpl[4][11][0].label                                # TextField Navegar por las sub listas
        txtFld2 = tpl[4][13][2]                               # Dropdown
        #txtFld3 = tpl[4][13][2].items[0].content.controls[1].label  # popoptions
        #print("--->",txtFld)
        #print("--->",txtFld2)
        print("-->",txtFld2)      

    def jir(self,**key):
        print()
        pass

    # agregar tpl
    def InsertImg(self,id,dicImg):
        #### -- PREUBAS PARA IMAGEN -- #####
        self.pdfImg.main(self.page,id,dicImg)
        self.Btnid = dicImg
        print(self.Btnid)
        temp_filename = "Template/Template_temp.pdf"
        self.doc.save(temp_filename)
        #self.doc.save()
        ####### ACTUALIZA SIN SOBRE ESCRIBIRLO ######
        #temp_filename = "Template/Template_temp.pdf"
        #self.doc.save(temp_filename)
        #doc.close()

    def InsertTxt(self,tpl):
    #def Insert(self):
        # Ejemplo: añadir texto en la primera página
        #txtFld = tpl[2][15]items[0].content.controls[1].value

        #print(self.Btnid)

        #'''
        #### -- TABLA EXTRUSIÓN -- #####       
        self.pdfFichVent.pdfFichVent(self.page,tpl)
        #### -- TABLA EXTRUSIÓN -- #####       
        self.pdfExtr.pdfExtru(self.page,tpl)
        #### -- TABLA IMPRESION -- #####       
        self.pdfImpr.pdfImpr(self.page,tpl)
        #### -- TABLA LAMINADO -- #####
        self.pdfLam.pdfLam(self.page,tpl)
        #self.pdfLam.pru(tpl)
        #### -- TABLA REFILADO -- #####
        self.pdfRef.pdfRefil(self.page,tpl)
        #### -- TABLA CONVERSIÓN -- #####
        self.pdfCnvrs.pdfConvrs(self.page,tpl)#'''

        temp_filename = "Template/Template_temp.pdf"
        self.doc.save(temp_filename)
        #### INSERTAR EN BD #####
        #pdfBytes = doc.write()
        #namePdf = f"{tpl[0][0].value}.pdf"
        #self.postpdf.postPridCardPdf(tpl[0][0].value,namePdf)
        #########################
        #print("--",self.Btnid)
        #self.save()
        
        #self.doc.close()

        '''
        ####Prueba sin archivos Temporales####
        pdf_buffer = io.BytesIO()               # Transforma el archivo en Bytes
        self.doc.save(pdf_buffer)
        pdf_binary = pdf_buffer.getvalue()      # Archivo Binario
        self.postpdf.postPridCardPdf(tpl[0][0].value,pdf_binary)
        self.doc.close()'''

    def save(self,*tpl):
        print(len(tpl))
        print(tpl)
    

#crpdf = CreatePdf()
#crpdf.Insert()
