import base64
import io
import flet as ft
import fitz
import webbrowser
import os
#from src.Controllers.appPrindCard import appPrindCard
from src.views.VentanaCreate.createFicha.createPdf import CreatePdf

class opnPrindPdf():
    def __init__(self,page):
        super().__init__()

        pass
    '''
        # Instancia hacia los qury's para el PDF
        self.qryPrndCrd = appPrindCard()
        self.page = page

        self.crtPdf = CreatePdf()'''

    def opnPdfBffer(self,e):
        pass
        '''
        idPrind = e.control.data[0]
        getPdf = self.qryPrndCrd.getPridCardPdf(idPrind)[0]
     
        # Recuperar el archivo PDF de la base de datos
        if getPdf:
            # Crear un buffer en memoria para el PDF
            pdf_buffer = io.BytesIO(getPdf)

            # Abrir el PDF desde el buffer
            pdf_document = fitz.open("pdf", pdf_buffer)

            temp_pdf_path = "Template/archivo_temporal.pdf"
            pdf_document.save(temp_pdf_path)

            #self.crtPdf.close()
            #pdf_document.close()
            
            if os.path.exists(temp_pdf_path):
                webbrowser.open(f'file://{os.path.abspath(temp_pdf_path)}')
            else:
                print("El archivo no existe.")

        self.page.update()'''
        
    def open_pdf(self,e):
        pass
        '''
        idPrind = e.control.data[0] # Obtiene el id del formulario
        getPdf = self.qryPrndCrd.getPridCardPdf(idPrind)[0]
        # Recuperar el archivo PDF de la base de datos
        if getPdf:
            # Guardar temporalmente el PDF en el disco
            with open("Template/archivo_temporal.pdf", "wb") as file:
                file.write(getPdf)

            ruta = "Template/archivo_temporal.pdf"

            if os.path.exists(ruta):
                webbrowser.open(f'file://{os.path.abspath(ruta)}')
            else:
                print("El archivo no existe.")'''
            