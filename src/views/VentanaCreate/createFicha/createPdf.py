import fitz  # PyMuPDF
from flet import *  
import os

from src.views.VentanaCreate.createFicha.Insrt_FichaVentas import Insrt_FichaVentas
from src.views.VentanaCreate.createFicha.Insrt_Extr import Insrt_Extr
from src.views.VentanaCreate.createFicha.Insrt_Impr import Insrt_Impr
from src.views.VentanaCreate.createFicha.Insrt_Laminado import Insrt_Laminado
from src.views.VentanaCreate.createFicha.Insrt_Refilado import Instr_Refilado
from src.views.VentanaCreate.createFicha.Insrt_Convrs import Insrt_Convrs
from src.Controllers.appPrindCard import appPrindCard

#### TAREAS ###
# * Obtener los datos de la bd
# * Configurar las Coordenadas para cada elemento de las tablas (Minimo llegar a Extrusión)
# * crear tabla para almacenar los PDF y asi obtenerlos
# * Agregar un boton desde el conjunto de Herramientas para visualizar el PrindCard creado 

# src\views\VentanaCreate\createFicha\Template

#print(doc)
tmpl = "Template/Template.pdf"
doc = fitz.open(tmpl)


class CreatePdf():
    def __init__(self):
        self.pdfFichVent = Insrt_FichaVentas()
        self.pdfExtr = Insrt_Extr()
        self.pdfImpr = Insrt_Impr()
        self.pdfLam = Insrt_Laminado()
        self.pdfRef = Instr_Refilado()
        self.pdfCnvrs = Insrt_Convrs()

        # ADD TO DATABASE
        self.postpdf = appPrindCard()

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

    # agregar tpl
    def Insert(self,tpl):
        # Ejemplo: añadir texto en la primera página
        #txtFld = tpl[2][15].items[0].content.controls[1].value
        page = doc[0]
        vl = 9

        #### -- TABLA EXTRUSIÓN -- #####       
        self.pdfFichVent.pdfFichVent(page,tpl)
        #### -- TABLA EXTRUSIÓN -- #####       
        self.pdfExtr.pdfExtru(page,tpl)
        #### -- TABLA IMPRESION -- #####       
        self.pdfImpr.pdfImpr(page,tpl)
        #### -- TABLA LAMINADO -- #####
        self.pdfLam.pdfLam(page,tpl)
        #self.pdfLam.pru(tpl)
        #### -- TABLA REFILADO -- #####
        self.pdfRef.pdfRefil(page,tpl)
        #### -- TABLA CONVERSIÓN -- #####
        self.pdfCnvrs.pdfConvrs(page,tpl)

        ################################

        
        #### INSERTAR EN BD #####
        #pdfBytes = doc.write()
        #namePdf = f"{tpl[0][0].value}.pdf"
        #self.postpdf.postPridCardPdf(tpl[0][0].value,namePdf)
        #########################

        ####### ACTUALIZA SIN SOBRE ESCRIBIRLO ######
        temp_filename = "Template/Template_temp.pdf"
        doc.save(temp_filename)
        doc.close()

        # Leer el archivo PDF en modo binario
        with open(temp_filename, "rb") as file:
            pdf_binary = file.read()

        self.postpdf.postPridCardPdf(tpl[0][0].value,pdf_binary)
        #############################################

        # Guarda el nuevo PDF en un archivo temporal
        #temp_filename = "temp_editado.pdf"
    
        #doc.save(f"Template/{tpl[0][0].value}.pdf")

#crpdf = CreatePdf()
#crpdf.Insert()
