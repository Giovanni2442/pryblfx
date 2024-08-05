import fitz  # PyMuPDF
from flet import *  
import os

# Insertar Valores del formulario EXTRUSION al pdf 
class Insrt_Extr():
    def __init__(self):
        self.vl = 15


    def pdfExtru(self,page):
        # Tip material a extruir
        page.insert_text(   
            (320, 1075),
            text= "PANCH000000",
            color=(0, 1, 0),
            fontsize=self.vl,
            fontname="Helvetica-Bold"
        )
