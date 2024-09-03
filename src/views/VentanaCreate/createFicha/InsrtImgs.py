'''
*********** TAREAS ******************

* Establecer la función auxiliar para cada tabla que lo requiera
* Desarrollar vista para agregar Imágenes al pdf y descipciónes para el footer de cada tabla
* Hacer las conexiones pertinentes para que todo funcione bien
* Averiguar como arreglar el bug de los PDF
* Averiguar como hacer el UPDATE
* Si no, empezar con el diseño (PRIORIDAD)

'''

import fitz  # PyMuPDF
import os
import shutil
from PIL import Image
from src.Controllers.appPrindCard import appPrindCard

class InstrImgs():
    def __init__(self,page):
        self.page = page
        self.vl = 7
        self.clr = (0, 0, 0)
        self.fnt = "Helvetica-Bold"

        self.text_color = (0,0,0)               # Color del Recuadro(ELIMINAR)
        self.text_size = 12     
        self.lst = []                            # Lista de urls que retorna la función para almacenar en BD            
        #self.dicImgs = {}                           #  Dicciónario de Imagenes, donde guarda las url dependiendo del proceso 
        self.appPrind = appPrindCard
       
        # INSERTAR / ACTUALIZAR
        self.id = self.page.client_storage.get("id")
        # METHOD GET 
        #self.dta = self.dtaFich().getFicha(self.id)
        #self.urlImg = self.appPrind().getPridCardImagesLOCAL(self.id)

    def pdfImageExtr(self,page,dic):
        # Figuras
        numFig = fitz.Rect(186, 587, 400, 609)      # Num. Fig. Bobina
        Img_rect = fitz.Rect(70, 587, 180, 659)     # Img. Extrusión
        text_rect = fitz.Rect(186, 610, 400, 660)   # Txt. Extrusión

        # --- DIBUJA EL RECTANGULO ---      
        #page.draw_rect(numFig,color=color) 
        #page.draw_rect(Img_rect,color=color)
        #page.draw_rect(text_rect,color=color)
 
        # --- AGREGAR TEXTO/IMAGEN AL RECT ---
        self.chekKey(page=page,fig=Img_rect,numFig=numFig,obsr=text_rect,dicImgs=dic)#'''


    #'''
    def pdfImageImpr(self,page,dic):
        # Figuras
        numFig = fitz.Rect(208, 1095, 400, 1120)      # Num. Fig. Bobina
        Img_rect = fitz.Rect(70, 1093, 200, 1265)     # Img. Extrusión
        text_rect = fitz.Rect(208, 1120, 400, 1265)   # Txt. Extrusión
 
        #page.insert_image(Img_rect, filename= image_path)        # Insetar la figura PRUEBAS
        self.chekKey(page=page,fig=Img_rect,numFig=numFig,obsr=text_rect,dicImgs=dic)#'''
    

    def pdfImageLam(self,page,dic):
        # Figuras
        numFig = fitz.Rect(560, 701, 765, 730)      # Num. Fig. Bobina
        Img_rect = fitz.Rect(438, 701, 550, 795)     # Img. Extrusión
        text_rect = fitz.Rect(560, 730, 765, 795)   # Txt. Extrusión
 
        self.chekKey(page=page,fig=Img_rect,numFig=numFig,obsr=text_rect,dicImgs=dic)#'''

    def pdfImageRef(self,page,dic):
        # Figuras
        numFig = fitz.Rect(560, 1155, 765, 1177)      # Num. Fig. Bobina
        Img_rect = fitz.Rect(438, 1155, 550, 1267)     # Img. Extrusión
        text_rect = fitz.Rect(560, 1177, 765, 1267)   # Txt. Extrusión
 
        self.chekKey(page=page,fig=Img_rect,numFig=numFig,obsr=text_rect,dicImgs=dic)#'''

    def pdfImageCnvrs(self,page,dic):
        # Figuras
        numFig = fitz.Rect(950, 540, 1125, 564)      # Num. Fig. Bobina
        Img_rect = fitz.Rect(800, 540, 940, 776)     # Img. Extrusión
        text_rect = fitz.Rect(950, 564, 1125, 776)   # Txt. Extrusión
 
        self.chekKey(page=page,fig=Img_rect,numFig=numFig,obsr=text_rect,dicImgs=dic)#'''
    
    # PROXIMAMENTE HACER ESTO AUTOMATICO
    def pdfSecuen(self,page):
        image_path = "Imagenes/img1.png" 
        color = (0,1,0)  # Color gris claro, con valores RGB entre 0 y 1
        # Figuras
        Img_rect = fitz.Rect(800, 810, 1125, 1265)     # Img. Extrusión
        # CONTENEDOR GUIA DE IMAGEN
        page.draw_rect(Img_rect,color=color)
 
        # Sirve para Ingresar Textos dentro del Rectangulo
        page.insert_image(Img_rect, filename=image_path)
    
    # Función para agregar Imagenes y Observaciónes
    # Ayuda a agregar Imagenes vacias y Observaciónes
    def chekKey(self,page,fig,numFig,obsr,dicImgs):
        try:
            if dicImgs[0] != None:          # Accede al indice de la imagen
                #pass
                page.insert_image(fig,filename=dicImgs[0])  # EN POSICIÓN [0] SE ENCIENTRA LA IMAGEN
                page.insert_textbox(numFig, dicImgs[1].upper(), fontsize=self.text_size, fontname="helv", color=self.text_color, align=1)       # EN POSICIÓN [1] SE ENCIENTRA EL NUM. FIGURA
                page.insert_textbox(obsr, dicImgs[2].upper(), fontsize=self.text_size, fontname="helv", color=self.text_color, align=0)         # EN POSICIÓN [2] SE ENCIENTRA LA DESCR.
            elif dicImgs[1] and dicImgs[2] != "N/A":        # Si no hay imagen, agrega los demas textos NUM. FIG Y DESCRIP
                page.insert_textbox(numFig, dicImgs[1].upper(), fontsize=self.text_size, fontname="helv", color=self.text_color, align=1)
                page.insert_textbox(obsr, dicImgs[2].upper(), fontsize=self.text_size, fontname="helv", color=self.text_color, align=0)
            else :
                return None
        except Exception  as e:
            print("ERROR EN INSERTAR LA IMAGEN",e)
  
            
        #'''

        '''nota : reposiciónar los cuadros de texto y el de imagen.
        * Si falta imagen, reposiciónar el recuadro de Obsrv, avarcando
        el espacio de la imagen faltante'
        print("--: ",dicImgs[key][0])'''
    

    #'''

    #EL PROBLEMA ESTA PORQUE REQUIERE DE UNA LISTA CON 3 ELEMENTOS [IMAGEN,FIGURA,DESCRIPCIÓN]
    # HACER UNA PRUEBA DONDE SOLO TOME LA IMAGEN O HACER QUE TOME LAS OTRAS 2 QUE FALTA, TOMANDO LOS VALORES
    # DE LOS TEXFIELD#
    def chekKeyPRU(self,page,fig,numFig,obsr,dicImgs):
        #print("--",lst[1])       # IMAGEN
        if dicImgs[0] != None:          # Accede al indice de la imagen
            #pass
            page.insert_image(fig,filename=dicImgs[0])  # EN POSICIÓN [0] SE ENCIENTRA LA IMAGEN
            page.insert_textbox(numFig, dicImgs[id][1].upper(), fontsize=self.text_size, fontname="helv", color=self.text_color, align=1)       # EN POSICIÓN [1] SE ENCIENTRA EL NUM. FIGURA
            page.insert_textbox(obsr, dicImgs[id][2].upper(), fontsize=self.text_size, fontname="helv", color=self.text_color, align=0)         # EN POSICIÓN [2] SE ENCIENTRA LA DESCR.
        elif dicImgs[id][1] and dicImgs[id][2] != "N/A":        # Si no hay imagen, agrega los demas textos NUM. FIG Y DESCRIP
            page.insert_textbox(numFig, dicImgs[id][1].upper(), fontsize=self.text_size, fontname="helv", color=self.text_color, align=1)
            page.insert_textbox(obsr, dicImgs[id][2].upper(), fontsize=self.text_size, fontname="helv", color=self.text_color, align=0)
        else:
            return None#'''
    
    def main2(self,page,idPrint):
        
        # INSERTAR / ANTUALIZAR IMAGENES EN EL PDF#
        if self.id != 'Insert':  # ACTUALIZAR
            dicImgs = self.page.client_storage.get("id_Img")
            # TRAE LAS URL DE LA BASE DE DATOS
            dta = self.appPrind().getPridCardImagesLOCAL(self.id)
            print("--",dta)
            
            # RECOLECTA DE LA BASE DE DATOS# 
            selectImg = {
                'EXTRC' : dta[1],
                'IMPRC' : dta[2],
                'LMNSN' : dta[3],
                'RFLD'  : dta[4],
                'CNVRSN' : dta[5]
            }
            ##################################

            # RECOLECTA DEL DICCIONARIO STORAGE # 
            select = {
                'EXTRC' : self.pdfImageExtr,
                'IMPRC' : self.pdfImageImpr,
                'LMNSN' : self.pdfImageLam,
                'RFLD'  : self.pdfImageRef,
                'CNVRSN' : self.pdfImageCnvrs
            }
            #####################################
         
            for key in selectImg:
                value = selectImg[key]
                if value != "N/A":           # VERIFICAR CONTENIDO
                    
                    fun = select.get(key)
                    print(value)
                    fun(page,value) 

                    #POST IMAGENES
                    # LLAMADA PARA CREAR LA LISTA
                    r = self.PostImgs(idPrint,key,value)
                # Limpiar el diccionario id_Img
            self.page.client_storage.set("id_Img", {})
            print("Mieda -",r)
            return r 


                    # SE INSERTAN IMAGENES VACIAS SI NO HAY IMAGENES
                    #print("NEL PASTEL XD")
                    #return ["N/A","N/A","N/A","N/A","N/A"]
                    #print("ERROR")
        
        else :      # INSERTAR
            dicImgs = self.page.client_storage.get("id_Img")

            #print("-AQUI LIMPIAR-",dicImgs)
            #'''
            select = {
                'EXTRC' : self.pdfImageExtr,
                'IMPRC' : self.pdfImageImpr,
                'LMNSN' : self.pdfImageLam,
                'RFLD'  : self.pdfImageRef,
                'CNVRSN' : self.pdfImageCnvrs
            }

            if dicImgs:
                for key in dicImgs:
                    value = dicImgs[key]
                    print("--d-- : ",value)
                    fun = select.get(key)
                    fun(page,value)

                    #POST IMAGENES
                    # LLAMADA PARA CREAR LA LISTA
                    r = self.PostImgs(idPrint,key,value[0])
                
                # Limpiar el diccionario id_Img
                self.page.client_storage.set("id_Img", {})
                print(r)
                return r 
            else:
                # SE INSERTAN IMAGENES VACIAS SI NO HAY IMAGENES
                return ["N/A","N/A","N/A","N/A","N/A"]
                #print("ERROR")

    # idPrint : Id del Prindcard
    # idSec     : Id de la secuencia (EXTRUSION,IMPRESION,LAMINADO,REFILADO,CONVERSION)
    # url_Img   : url de la Imagen
    # 
    def PostImgs(self,idPrint,idSec,url_Img):
        dicImgs = {
            'EXTRC' : 'N/A',
            'IMPRC' : 'N/A',
            'LMNSN' : 'N/A',
            'RFLD'  : 'N/A',
            'CNVRSN' : 'N/A'
        }
    #def PostImgs(id):
        lstImgs = []
        #'''#url = 
        print(idSec,url_Img)
        if url_Img:     # si no es None
            try:
                # Abrir la imagen con Pillow para detectar el formato original
                with Image.open(url_Img) as img:
                    extencion = img.format.lower()  # 'jpeg', 'png', 'gif', etc.

                #nuevo_nombre = f"{idPrint}_{idSec}.{extencion}"             # Nombre nueva de la Imagen ejemplo : 'E34EE_344_IMPRS.png'
                nuevo_nombre = f"{idPrint}.{extencion}" 
                nuevo_directorio = os.path.join(os.getcwd(), "Imagenes",f'{idSec}')     # NOTA : HACER QUE SE GUARDEN POR SUBCARPETAS
                # Crear la ruta completa para la nueva ubicación
                nueva_ruta = os.path.join(nuevo_directorio, nuevo_nombre)
                
                # RUTA DEL DIRECTORIO DEL PROYECTO
                ruta_relativa = os.path.relpath(nueva_ruta, os.getcwd())
                print("CARPETA NUEVA --- ",ruta_relativa)
                # Mover y renombrar el archivo
                shutil.move(url_Img, nueva_ruta)
                #shutil.move(url_Img, ruta_relativa)

                # Almacena la url en el dicciónario dependiendo de la Key
                #dicImgs[idSec] = f'Imagenes/{nuevo_nombre}'
                dicImgs[idSec] = f'{ruta_relativa}'

                # Recorrer el Dicciónario y agregar sus value en una lista
                for key in dicImgs: 
                    lstImgs.append(dicImgs[key])
                    #print("-- ",dicImgs[key])  # Imprimir el diccionario para verificar
                print("lista ---",lstImgs)
                return lstImgs

            except Exception as e:
                print(f"Error al mover y renombrar la imagen: {e}")
        else:
            print("ERROR HACER RESTRICCIÓN HASTA AGREGAR ALGO!")
    
