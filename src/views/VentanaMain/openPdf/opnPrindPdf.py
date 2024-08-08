import flet as ft
import webbrowser
import os
from src.Controllers.appPrindCard import appPrindCard

class opnPrindPdf():
    def __init__(self):
        super().__init__()

        self.qryPrndCrd = appPrindCard()

    def open_pdf(self,e):
        idPrind = e.control.data[0]
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
                print("El archivo no existe.")
            