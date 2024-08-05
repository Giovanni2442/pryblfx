import fitz  # PyMuPDF
from flet import *  
import os

from src.views.VentanaCreate.createFicha.Insrt_FichaVentas import Insrt_FichaVentas
from src.views.VentanaCreate.createFicha.Insrt_Extr import Insrt_Extr
from src.views.VentanaCreate.createFicha.Insrt_Laminado import Insrt_Laminado
from src.views.VentanaCreate.createFicha.Insrt_Refilado import Instr_Refilado
from src.views.VentanaCreate.createFicha.Insrt_Convrs import Insrt_Convrs


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
        self.pdfExtr = Insrt_Extr()
        self.pdfLam = Insrt_Laminado()
        self.pdfRef = Instr_Refilado()
        self.pdfCnvrs = Insrt_Convrs()

        
    def jer(self,tpl):
        '''     
        for inx,i in enumerate(tpl):
            if isinstance(i, list):
                print(f"{inx} : {i}")
            else:
                continue'''
        #txtFld = tpl[4][11].items[0].content.controls[1].label
        txtFld = tpl[4][11][0].label                                # TextField Navegar por las sub listas
        txtFld2 = tpl[4][11][1].label                               # Dropdown
        txtFld3 = tpl[4][11][2].items[0].content.controls[1].label  # popoptions
        #print("--->",txtFld)
        #print("--->",txtFld2)
        print("-->",tpl[0][0])      
            
    def saludo(self,id):
        print(id)

    # agregar tpl
    def Insert(self,tpl):
        # Ejemplo: añadir texto en la primera página
        #txtFld = tpl[2][15].items[0].content.controls[1].value
        page = doc[0]
        vl = 9

        #text = "PRUEBA"
        '''
        #### TABLA FichaTecnica ####
            # id_producto
        page.insert_text(   
            (930, 135),
            text= tpl[0].value.upper(),  #Id_PrindCard
            color=(0, 0, 0),
            fontsize=19,
            fontname="Helvetica-Bold"
        )

            # cliente
        page.insert_text(   
            (930, 79),
            text= tpl[1].value.upper(),
            color=(0, 0, 0),
            fontsize=19,
            fontname="Helvetica-Bold"
        )

            # fecha_elav
        page.insert_text(   
            (930, 56),
            text = tpl[2].value.upper(),
            color=(0, 0, 0),
            fontsize=19,
            fontname="Helvetica-Bold"
        )

            # fecha_Rev
        page.insert_text(   
            (653, 82),
            text = tpl[3].value.upper(),
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

        #### -- TABLA VENTAS -- #####

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
        ##################################
        #'''

        # PRUEBA #
        #print(tpl[0])
        #self.pdfFichVent.ji(tpl)

        ji = tpl
        print(tpl[0][0])

        #### -- TABLA EXTRUSIÓN -- #####       
        self.pdfFichVent.pdfFichVent(page,tpl)
        #### -- TABLA EXTRUSIÓN -- #####       
        #self.pdfExtr.pdfExtru(page)
        #### -- TABLA LAMINADO -- #####
        #self.pdfLam.pdfLam(page)
        #### -- TABLA REFILADO -- #####
        #self.pdfRef.pdfRefil(page)
        #### -- TABLA CONVERSIÓN -- #####
        #self.pdfCnvrs.pdfConvrs(page)

        ################################

        # Guarda el nuevo PDF en un archivo temporal
        temp_filename = "temp_editado.pdf"
        
        #doc.save(f"Template/{tpl[0][0].value}.pdf")
        temp_filename = "Template/Template.pdf"
        doc.save(temp_filename)

        # Renombra el archivo temporal al nombre original
        os.replace(temp_filename,tmpl)
    
    #def getData(self,tpl):
    #    for i in tpl:
    #        for j in i:
    #            print(j.value.upper())
        
#crpdf = CreatePdf()
#crpdf.Insert()
