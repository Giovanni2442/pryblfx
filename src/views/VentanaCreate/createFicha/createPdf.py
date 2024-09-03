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

        # INSERT / UPDATE
        self.id = self.page.client_storage.get("id")

        # -- ELEMENTOS DE PRUEBA --
        self.tplImg={} 
        self.dta = []       # ALMACENA LOS DATOS QUE SE VAN A INGRESAR EN LA BD

        ########################### 

        # ADD TO DATABASE
        self.postpdf = appPrindCard
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

    def jir1(self,*key):
        self.uno = key
        print(self.uno)
        
    def jir2(self,*arg):
        self.dos = arg
        print(self.uno,self.dos)

    # agregar tpl
    #def InsertImg(self,id,dicImg):
    def InsertImg(self):
        #print(dicImg)
        #### -- PREUBAS PARA IMAGEN -- #####
        #self.pdfImg.main(self.page,id,dicImg)
        self.pdfImg.main2(self.page)
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
        #self.pdfImg.main(self.page,id,dicImg)
        
        # INSERCIÓN DE IMAGENES # 
        lstImg = self.pdfImg.main2(self.page,idpdf)
        print("IMG --",lstImg)      # <- EYY! Q CHECA LA LISTA
        #self.pdfImg.main(self.page,tpl)

        for pros in lstImg:       # Recorre el proceso
            for lst in pros:
                print("--.i.- ",lst)

        imgExtr = lstImg[0][0]   #  
        imgImpr = lstImg[1][0]
        imgLam = lstImg[2][0]
        imgRef = lstImg[3][0]
        imgCnvr = lstImg[4][0]

        figExtrs = lstImg[0][1]
        figImprs = "N/A"
        figLam = "N/A"
        figRef = "N/A"
        figCnvrs = "N/A"

        print(figExtrs)
        #figImprs = lstImg[1][1]

        self.pdf = f"FilePdf/{idpdf}.pdf"
        self.doc.save(self.pdf)

        # pdf : Url y nombre donde se guarda el pdf
        # idpdf : Id del Prindcard
        # 

        #self.postPdfLOCAL(idpdf,self.pdf,imgExtr,imgImpr,imgLam,imgRef,imgCnvr,figExtrs,figImprs,figLam,figRef,figCnvrs)

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
        if self.id != "Insert":
            # UPDATE
            self.postpdf().transctUpdatePrindCard(pdf,id_pdf)
            self.doc.close()
        else:
            # INSERT
            self.postpdf().transctInsertPrindCard(id_pdf,pdf)
            self.doc.close()#'''

    def postPdfLOCAL(self,id_pdf,url_pef,extr,imprs,lam,ref,cnvr,figExtrs,figImprs,figLam,figRef,figCnvrs):
        if self.id != "Insert":
            # UPDATE
            #self.postpdf().transctInsertPrindCardLOCAL(url_pef,id_pdf)
            #self.doc.close()
            print("PROXIMAMENTE!")
        else:
            # INSERT
            self.postpdf().transctInsertPrindCardLOCAL(id_pdf,url_pef,extr,imprs,lam,ref,cnvr,figExtrs,figImprs,figLam,figRef,figCnvrs)
            self.doc.close()#'''

#crpdf = CreatePdf()
#crpdf.Insert()
