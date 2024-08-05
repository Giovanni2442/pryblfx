import fitz  # PyMuPDF
from flet import *  
import os

from src.views.VentanaCreate.createFicha.Insrt_Extr import Insrt_Extr

#### TAREAS ###
# * Obtener los datos de la bd
# * Configurar las Coordenadas para cada elemento de las tablas (Minimo llegar a Extrusión)
# * crear tabla para almacenar los PDF y asi obtenerlos
# * Agregar un boton desde el conjunto de Herramientas para visualizar el PrindCard creado 

# src\views\VentanaCreate\createFicha\Template

#print(doc)
tmpl = "Template/1212.pdf"
doc = fitz.open(tmpl)


class CreatePdf():
    def __init__(self):
        self.pdfExtr = Insrt_Extr()
        
    
    def jer(self,*tpl):
        
        for inx,i in enumerate(tpl):
            if isinstance(i, list):
                print(f"{inx} : {i}")
            else:
                continue
        #txtFld = tpl[5][11].items[0].content.controls[1].label

       #print("--->",txtFld)     
        #print(tpl[108])
        '''
        #vle = tpl[2][0].items[0].content.controls[1].value
        def jer(self, *tpl):
            for in1, i in enumerate(tpl):  # Recorre las listas de Inputs
                if isinstance(i, list):
                    for in2, j in enumerate(i):  # Recorre los valores de cada lista
                        if isinstance(j, list):  # Verifica si el valor de la lista hay listas, para colocar los valores en la lista padre
                            for sub_index, f in enumerate(j):  # Recorre la sub lista desde el indice
                                if isinstance(f, PopupMenuButton):
                                    for m_index, m in enumerate(f.items):
                                        txtFld = m.content.controls[1]
                                        print(f"[{in1}][{in2}][{sub_index}][{m_index}]", txtFld.label)
                                else:
                                    print(f"[{in1}][{in2}][{sub_index}]", f.label)
                        elif isinstance(j, PopupMenuButton):
                            for k_index, k in enumerate(j.items):
                                txtFld = k.content.controls[1]
                                print(f"[{in1}][{in2}][{k_index}]", txtFld.label)
                        else:
                            print(f"[{in1}][{in2}]", j.label)
                else:
                    # Maneja el caso donde `i` no es una lista
                    if isinstance(i, PopupMenuButton):
                        for m_index, m in enumerate(i.items):
                            txtFld = m.content.controls[1]
                            print(f"[{in1}][{m_index}]", txtFld.label)
                    else:
                        print(f"[{in1}]", i.label)
                '''
            
    # agregar tpl
    def Inser(self):
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
        #### -- TABLA EXTRUSIÓN -- #####
        # Tip material a extruir
        page.insert_text(   
            (320, 271),
            text= "MATERIAL",
            color=(0, 0, 0),
            fontsize=vl,
            fontname="Helvetica-Bold"
        )

        # Dinaje Requerido
        page.insert_text(   
            (320, 285),
            text= "DINAJE",
            color=(0, 0, 0),
            fontsize=vl,
            fontname="Helvetica-Bold"
        )

        # FÓRMULA CON LA QUE SE EXTRUIRÁ LA BOBINA
        page.insert_text(   
            (320, 299),
            text= "FÓRMULA",
            color=(0, 0, 0),
            fontsize=vl,
            fontname="Helvetica-Bold"
        )

        # PIGMENTO DE PELÍCULA: (SI (especificar color), N/A)
        page.insert_text(   
            (320, 313),
            text= "PIGMENTO",
            color=(0, 0, 0),
            fontsize=vl,
            fontname="Helvetica-Bold"
        )

        # CALIBRE DE LA PELÍCULA Y TOLERANCIA
        page.insert_text(   
            (320, 328),
            text= "CALIBRE",
            color=(0, 0, 0),
            fontsize=vl,
            fontname="Helvetica-Bold"
        )

        # TIPO DE BOBINA: 
        page.insert_text(   
            (320, 341),
            text= "TRATADO",
            color=(0, 0, 0),
            fontsize=vl,
            fontname="Helvetica-Bold"
        )

        # TIPO DE TRATADO: 
        page.insert_text(   
            (320, 355),
            text= "BOBINA",
            color=(0, 0, 0),
            fontsize=vl,
            fontname="Helvetica-Bold"
        )

        # ANCHO DE BOBINA Y TOLERANCIA 
        page.insert_text(   
            (320, 369),
            text= "ANCHO",
            color=(0, 0, 0),
            fontsize=vl,
            fontname="Helvetica-Bold"
        )

        # ANCHO DE CORE Y TOLERANCIA 
        page.insert_text(   
            (320, 384),
            text= "CORE",
            color=(0, 0, 0),
            fontsize=vl,
            fontname="Helvetica-Bold"
        )

        # DIÁMETRO DE BOBINA Y TOLERANCIA
        page.insert_text(   
            (320, 398),
            text= "DIÁMETRO",
            color=(0, 0, 0),
            fontsize=vl,
            fontname="Helvetica-Bold"
        )

        # MÁXIMO DE EMPALMES POR BOBINA
        page.insert_text(   
            (320, 412),
            text= "EMPLAMES",
            color=(0, 0, 0),
            fontsize=vl,
            fontname="Helvetica-Bold"
        )

        # ORIENTACIÓN DE BOBINA EN TARIMA: (HORIZONTAL/ VERTICAL)
        page.insert_text(   
            (320, 426),
            text= "ORIENTACIÓN",
            color=(0, 0, 0),
            fontsize=vl,
            fontname="Helvetica-Bold"
        )

        # TIPO DE EMPAQUE PARA BOBINA: (EMPLAYE / BOLSA / N/A)
        page.insert_text(   
            (320, 440),
            text= "EMPQ",
            color=(0, 0, 0),
            fontsize=vl,
            fontname="Helvetica-Bold"
        )

        # PESAR PRODUCTO POR: (TARIMA / BOBINA / AMBOS)
        page.insert_text(   
            (320, 454),
            text= "PESAR PRDCT",
            color=(0, 0, 0),
            fontsize=vl,
            fontname="Helvetica-Bold"
        )

        # PESO NETO PROMEDIO DE BOBINA
        page.insert_text(   
            (320, 468),
            text= "PSNTO",
            color=(0, 0, 0),
            fontsize=vl,
            fontname="Helvetica-Bold"
        )

        # ETIQUETADO
        page.insert_text(   
            (320, 482),
            text= "ETIQUETADO",
            color=(0, 0, 0),
            fontsize=vl,
            fontname="Helvetica-Bold"
        )

        # NUMERO DE BOBINAS POR CAMA Y CAMAS POR TARIMA
        page.insert_text(   
            (320, 496),
            text= "NUMERO",
            color=(0, 0, 0),
            fontsize=vl,
            fontname="Helvetica-Bold"
        )

        # NUMERO DE BOBINAS EN TARIMA
        page.insert_text(   
            (320, 511),
            text= "TARIMA",
            color=(0, 0, 0),
            fontsize=vl,
            fontname="Helvetica-Bold"
        )

        # PESO NETO PROMEDIO POR TARIMA
        page.insert_text(   
            (320, 525),
            text= "PROMEDIO",
            color=(0, 0, 0),
            fontsize=vl,
            fontname="Helvetica-Bold"
        )

        # LA TARIMA LLEVARA EMPLAYE: (APLICA / N/A)
        page.insert_text(   
            (320, 539),
            text= "EMPLAYE",
            color=(0, 0, 0),
            fontsize=vl,
            fontname="Helvetica-Bold"
        )

        # LA TARIMA SERA FLEJADA: (APLICA / N/A)
        page.insert_text(   
            (320, 553),
            text= "FLEJADA",
            color=(0, 0, 0),
            fontsize=vl,
            fontname="Helvetica-Bold"
        )

        #############################

        #### -- TABLA IMPRESIÓN -- #####
        
        # MATERIAL A IMPRIMIR
        page.insert_text(   
            (320, 693),
            text= "EXTRUCIÓN",
            color=(0, 0, 0),
            fontsize=vl,
            fontname="Helvetica-Bold"
        )

        # DINAJE REQUERIDO PARA SU IMPRESIÓN
        page.insert_text(   
            (320, 707),
            text= "DINAJE",
            color=(0, 0, 0),
            fontsize=vl,
            fontname="Helvetica-Bold"
        )

        # CALIBRE DEL MATERIAL A IMPRIMIR Y TOLERANCIA
        page.insert_text(   
            (320, 721),
            text= "CALIBRE",
            color=(0, 0, 0),
            fontsize=vl,
            fontname="Helvetica-Bold"
        )

        # ANCHO DE BOBINA A IMPRIMIR Y TOLERANCIA 
        page.insert_text(   
            (320, 735),
            text= "ANCHO",
            color=(0, 0, 0),
            fontsize=vl,
            fontname="Helvetica-Bold"
        )

        # GROSOR DE CORE:  (10 MM / OTRO) 
        page.insert_text(   
            (320, 748),
            text= "GROSOR",
            color=(0, 0, 0),
            fontsize=vl,
            fontname="Helvetica-Bold"
        )

        # ANCHO DE CORE Y TOLERANCIA  
        page.insert_text(   
            (320, 763),
            text= "GROSOR",
            color=(0, 0, 0),
            fontsize=vl,
            fontname="Helvetica-Bold"
        )
        
        # DESARROLLO A IMPRIMIR (MANGA)  
        page.insert_text(   
            (320, 777),
            text= "DESARROLLO",
            color=(0, 0, 0),
            fontsize=vl,
            fontname="Helvetica-Bold"
        )

        # REPETICIONES AL EJE  
        page.insert_text(   
            (320, 792),
            text= "EJE",
            color=(0, 0, 0),
            fontsize=vl,
            fontname="Helvetica-Bold"
        )

        # REPETICIONES AL DESARROLLO 
        page.insert_text(   
            (320, 806),
            text= "DESARROLLO",
            color=(0, 0, 0),
            fontsize=vl,
            fontname="Helvetica-Bold"
        )

        # CANTIDAD DE TINTAS A IMPRIMIR 
        page.insert_text(   
            (320, 820),
            text= "TINTAS",
            color=(0, 0, 0),
            fontsize=vl,
            fontname="Helvetica-Bold"
        )

        # TIPO DE IMPRESIÓN: (INTERNA/EXTERNA) 
        page.insert_text(   
            (320, 834),
            text= "IMPRESIÓN",
            color=(0, 0, 0),
            fontsize=vl,
            fontname="Helvetica-Bold"
        )

        # TIPO DE TINTAS A UTILIZAR 
        page.insert_text(   
            (320, 848),
            text= "UTILIZAR",
            color=(0, 0, 0),
            fontsize=vl,
            fontname="Helvetica-Bold"
        )

        # TIPO DE BARNIZ SOBRE LA IMPRESIÓN 
        page.insert_text(   
            (320, 862),
            text= "BARNIZ",
            color=(0, 0, 0),
            fontsize=vl,
            fontname="Helvetica-Bold"
        )

        # FIGURA DE EMBOBINADO AL SALIR DE IMPRESIÓN (1,2,3,4,5,6,7,8)
        page.insert_text(   
            (320, 876),
            text= "EMBOBINADO",
            color=(0, 0, 0),
            fontsize=vl,
            fontname="Helvetica-Bold"
        )

        # VALIDACIÓN DE COLOR POR
        page.insert_text(   
            (320, 891),
            text= "VALIDACIÓN",
            color=(0, 0, 0),
            fontsize=vl,
            fontname="Helvetica-Bold"
        )

        # MÁXIMO DE EMPALMES POR BOBINA
        page.insert_text(   
            (320, 906),
            text= "MÁXIMO",
            color=(0, 0, 0),
            fontsize=vl,
            fontname="Helvetica-Bold"
        )

        # TIPO DE EMPAQUE PARA BOBINA
        page.insert_text(   
            (320, 920),
            text= "EMPAQUE",
            color=(0, 0, 0),
            fontsize=vl,
            fontname="Helvetica-Bold"
        )

        # ORIENTACIÓN DE BOBINA EN TARIMA: 
        page.insert_text(   
            (320, 934),
            text= "ORIENTACIÓN",
            color=(0, 0, 0),
            fontsize=vl,
            fontname="Helvetica-Bold"
        )

        # PESAR PRODUCTO POR:
        page.insert_text(   
            (320, 948),
            text= "PESAR",
            color=(0, 0, 0),
            fontsize=vl,
            fontname="Helvetica-Bold"
        )

        # DIÁMETRO DE BOBINA Y TOLERANCIA 
        page.insert_text(   
            (320, 962),
            text= "DIÁMETRO",
            color=(0, 0, 0),
            fontsize=vl,
            fontname="Helvetica-Bold"
        )

         # PESO NETO PROMEDIO DE BOBINA  
        page.insert_text(   
            (320, 976),
            text= "PESO",
            color=(0, 0, 0),
            fontsize=vl,
            fontname="Helvetica-Bold"
        )

        # ETIQUETADO  
        page.insert_text(   
            (320, 991),
            text= "ETIQUETADO",
            color=(0, 0, 0),
            fontsize=vl,
            fontname="Helvetica-Bold"
        )

        # NUMERO DE BOBINAS POR CAMA Y CAMAS POR TARIMA   
        page.insert_text(   
            (320, 1005),
            text= "CAMAS",
            color=(0, 0, 0),
            fontsize=vl,
            fontname="Helvetica-Bold"
        )

        # NUMERO DE BOBINAS EN TARIMA    
        page.insert_text(   
            (320, 1019),
            text= "TARIMA",
            color=(0, 0, 0),
            fontsize=vl,
            fontname="Helvetica-Bold"
        )

         # PESO NETO PROMEDIO POR TARIMA   
        page.insert_text(   
            (320, 1032),
            text= "PROMEDIO",
            color=(0, 0, 0),
            fontsize=vl,
            fontname="Helvetica-Bold"
        )

         # LA TARIMA LLEVARA EMPLAYE: (APLICA / N/A)  
        page.insert_text(   
            (320, 1047),
            text= "EMPLAYE",
            color=(0, 0, 0),
            fontsize=vl,
            fontname="Helvetica-Bold"
        )


        # LA TARIMA SERA FLEJADA: (APLICA / N/A)
        page.insert_text(   
            (320, 1061),
            text= "FLEJADA",
            color=(0, 0, 0),
            fontsize=vl,
            fontname="Helvetica-Bold"
        )

        self.pdfExtr.pdfExtru(page)




        ################################


        # Guarda el nuevo PDF en un archivo temporal
        #temp_filename = "temp_editado.pdf"
        
        #doc.save(f"Template/{tpl[0][0].value}.pdf")
        temp_filename = "Template/1215_temp.pdf"
        doc.save(temp_filename)
        

        # Renombra el archivo temporal al nombre original
        #os.replace(temp_filename,tmpl)
    
    #def getData(self,tpl):
    #    for i in tpl:
    #        for j in i:
    #            print(j.value.upper())
        
crpdf = CreatePdf()
crpdf.Inser()
