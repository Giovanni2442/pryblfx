import fitz  # PyMuPDF
import os

from src.Controllers.appTable import Controllers

#### TAREAS ###
# * Obtener los datos de la bd
# * Configurar las Coordenadas para cada elemento de las tablas (Minimo llegar a Extrusión)
# * crear tabla para almacenar los PDF y asi obtenerlos
# * Agregar un boton desde el conjunto de Herramientas para visualizar el PrindCard creado 

class createPdf():
    def __init__(self):

        self.tmpl = "editado.pdf"
        doc = fitz.open(self.tmpl)

        # Ejemplo: añadir texto en la primera página
        page = doc[0]
        text = "PRODUCTO"

        #### TABLA FichaTecnica ####
        '''    # id_producto
        page.insert_text(   
            (930, 130),
            text,
            color=(1, 0, 0),
            fontsize=9,
            fontname="Times-Bold"
        )

            # cliente
        page.insert_text(   
            (930, 79),
            text,
            color=(1, 0, 0),
            fontsize=9,
            fontname="Times-Bold"
        )

            # fecha_elav
        page.insert_text(   
            (930, 54),
            text,
            color=(1, 0, 0),
            fontsize=9,
            fontname="Times-Bold"
        )

            # fecha_Rev
        page.insert_text(   
            (653, 82),
            text,
            color=(1, 0, 0),
            fontsize=9,
            fontname="Times-Bold"
        )'''

            # Producto
        page.insert_text(   
            (300, 135),
            text,
            color=(1, 0, 0),
            fontsize=19,
            fontname="helvb"
        )


        # Guarda el nuevo PDF en un archivo temporal
        temp_filename = "temp_editado.pdf"
        doc.save(temp_filename)
        #doc.save("editado.pdf")
        doc.close()

        # Renombra el archivo temporal al nombre original
        os.replace(temp_filename, tmpl)
