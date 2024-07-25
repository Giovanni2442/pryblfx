import fitz  # PyMuPDF
import os

from src.Controllers.appTable import Controllers

#### TAREAS ###
# * Obtener los datos de la bd
# * Configurar las Coordenadas para cada elemento de las tablas (Minimo llegar a Extrusión)
# * crear tabla para almacenar los PDF y asi obtenerlos
# * Agregar un boton desde el conjunto de Herramientas para visualizar el PrindCard creado 

# src\views\VentanaCreate\createFicha\Template

#print(doc)
tmpl = "Template/Template2.pdf"
doc = fitz.open(tmpl)

class CreatePdf():
    def __init__(self):
        self.data = Controllers()

    def Inser(self,tpl):
        # Ejemplo: añadir texto en la primera página
        page = doc[0]
        
        #text = "PRUEBA"

        #### TABLA FichaTecnica ####
            # id_producto
        page.insert_text(   
            (930, 135),
            text= tpl[0][0].value.upper(),  #Id_PrindCard
            color=(0, 0, 0),
            fontsize=19,
            fontname="Helvetica-Bold"
        )

            # cliente
        page.insert_text(   
            (930, 79),
            text= tpl[0][1].value.upper(),
            color=(0, 0, 0),
            fontsize=19,
            fontname="Helvetica-Bold"
        )

            # fecha_elav
        page.insert_text(   
            (930, 56),
            text = tpl[0][2].value.upper(),
            color=(0, 0, 0),
            fontsize=19,
            fontname="Helvetica-Bold"
        )

            # fecha_Rev
        page.insert_text(   
            (653, 82),
            text = tpl[0][3].value.upper(),
            color=(0, 0, 0),
            fontsize=19,
            fontname="Helvetica-Bold"
        )

            # Producto
        page.insert_text(   
            (304, 135),
            text = tpl[0][4].value.upper(),
            color=(0, 0, 0),
            fontsize=19,
            fontname="Helvetica-Bold"
        )
        ################################

        #### TABLA VENTAS #####

            # Asesor Comercial
        page.insert_text(   
            (320, 176),
            text = tpl[1][0].value.upper(),
            color=(0, 0, 0),
            fontsize=10,
            fontname="Helvetica-Bold"
        )

            # Tipo de empaque
        page.insert_text(   
            (320, 192),
            text = tpl[1][1].value.upper(),
            color=(0, 0, 0),
            fontsize=10,
            fontname="Helvetica-Bold"
        )


            # Producto laminado
        page.insert_text(   
            (320, 206),
            text = tpl[1][2].value.upper(),
            color=(0, 0, 0),
            fontsize=10,
            fontname="Helvetica-Bold"
        )

        # Estructura del producto
        page.insert_text(   
            (233, 219),
            text = tpl[1][3].value.upper(),
            color=(0, 0, 0),
            fontsize=10,
            fontname="Helvetica-Bold"
        )

        # producto que se empaca
        page.insert_text(   
            (320, 234),
            text = tpl[1][4].value.upper(),
            color=(0, 0, 0),
            fontsize=10,
            fontname="Helvetica-Bold"
        )

        page.insert_text(   
            (320, 264),
            text= "prueba",
            color=(0, 0, 0),
            fontsize=10,
            fontname="Helvetica-Bold"
        )

        # Guarda el nuevo PDF en un archivo temporal
        #temp_filename = "temp_editado.pdf"
        #doc.save(temp_filename)
        doc.save(f"Template/{tpl[0][0].value}.pdf")
        doc.close()

        # Renombra el archivo temporal al nombre original
        #os.replace(temp_filename,tmpl)
    
    def getData(self,tpl):
        for i in tpl:
            for j in i:
                print(j.value.upper())
        
#crpdf = CreatePdf()
#crpdf.Inser()
