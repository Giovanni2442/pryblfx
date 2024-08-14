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

class InstrImgs():
    def __init__(self):
        self.vl = 7
        self.clr = (0, 0, 0)
        self.fnt = "Helvetica-Bold"

        self.text_color = (0,0,0)        # Color del Recuadro(ELIMINAR)
        self.text_size = 12    

    def pdfImageExtr(self,page,id,dic):
        # Ruta de la imagen que deseas insertar
        image_path = "Imagenes/img1.png" 
     
        # Figuras
        numFig = fitz.Rect(186, 587, 400, 609)      # Num. Fig. Bobina
        Img_rect = fitz.Rect(70, 587, 180, 659)     # Img. Extrusión
        text_rect = fitz.Rect(186, 610, 400, 660)   # Txt. Extrusión

        # --- DIBUJA EL RECTANGULO ---      
        #page.draw_rect(numFig,color=color) 
        #page.draw_rect(Img_rect,color=color)
        #page.draw_rect(text_rect,color=color)
 
        # --- AGREGAR TEXTO/IMAGEN AL RECT ---
        self.chekKey(page=page,fig=Img_rect,id=id,numFig=numFig,obsr=text_rect,dicImgs=dic)

    def pdfImageImpr(self,page,id,dic):
        # Figuras
        numFig = fitz.Rect(208, 1095, 400, 1120)      # Num. Fig. Bobina
        Img_rect = fitz.Rect(70, 1093, 200, 1265)     # Img. Extrusión
        text_rect = fitz.Rect(208, 1120, 400, 1265)   # Txt. Extrusión
 
        #page.insert_image(Img_rect, filename= image_path)        # Insetar la figura PRUEBAS
        self.chekKey(page=page,fig=Img_rect,id=id,numFig=numFig,obsr=text_rect,dicImgs=dic)

    def pdfImageLam(self,page,id,dic):
        # Figuras
        numFig = fitz.Rect(560, 701, 765, 730)      # Num. Fig. Bobina
        Img_rect = fitz.Rect(438, 701, 550, 795)     # Img. Extrusión
        text_rect = fitz.Rect(560, 730, 765, 795)   # Txt. Extrusión
 
        self.chekKey(page=page,fig=Img_rect,id=id,numFig=numFig,obsr=text_rect,dicImgs=dic)

    def pdfImageRef(self,page,id,dic):
        # Figuras
        numFig = fitz.Rect(560, 1155, 765, 1177)      # Num. Fig. Bobina
        Img_rect = fitz.Rect(438, 1155, 550, 1267)     # Img. Extrusión
        text_rect = fitz.Rect(560, 1177, 765, 1267)   # Txt. Extrusión
 
        self.chekKey(page=page,fig=Img_rect,id=id,numFig=numFig,obsr=text_rect,dicImgs=dic)

    def pdfImageCnvrs(self,page,id,dic):
        # Figuras
        numFig = fitz.Rect(950, 540, 1125, 564)      # Num. Fig. Bobina
        Img_rect = fitz.Rect(800, 540, 940, 776)     # Img. Extrusión
        text_rect = fitz.Rect(950, 564, 1125, 776)   # Txt. Extrusión
 
        self.chekKey(page=page,fig=Img_rect,id=id,numFig=numFig,obsr=text_rect,dicImgs=dic)
  
    def pdfSecuen(self,page):
        image_path = "Imagenes/img1.png" 

        # Crear el nuevo rectángulo en las coordenadas especificadas
         #                   x0  y0   x1   y1 
        txt = "Hommmmmmmmmmmmmmmmmmmmmmmmmmmmmmmla xd"
        text_color = color = (0,1,0)
        text_size = 12
        color = (0,1,0)  # Color gris claro, con valores RGB entre 0 y 1

        # Figuras
        Img_rect = fitz.Rect(800, 810, 1125, 1265)     # Img. Extrusión
 
        page.draw_rect(Img_rect,color=color)
 
        # Sirve para Ingresar Textos dentro del Rectangulo
        page.insert_image(Img_rect, filename=image_path)
    
    # Función para agregar Imagenes y Observaciónes
    # Ayuda a agregar Imagenes vacias y Observaciónes
    def chekKey(self,page,fig,id,numFig,obsr,dicImgs):
        if dicImgs[id][0] != None:          # Accede al indice de la imagen
            #pass
            page.insert_image(fig,filename=dicImgs[id][0]) 
            page.insert_textbox(numFig, dicImgs[id][1].upper(), fontsize=self.text_size, fontname="helv", color=self.text_color, align=1)
            page.insert_textbox(obsr, dicImgs[id][2].upper(), fontsize=self.text_size, fontname="helv", color=self.text_color, align=0)
        elif dicImgs[id][1] and dicImgs[id][2] != "N/A":        # Si no hay imagen, agrega los demas textos
            page.insert_textbox(numFig, dicImgs[id][1].upper(), fontsize=self.text_size, fontname="helv", color=self.text_color, align=1)
            page.insert_textbox(obsr, dicImgs[id][2].upper(), fontsize=self.text_size, fontname="helv", color=self.text_color, align=0)
        else:
            return None
        #'''

        '''nota : reposiciónar los cuadros de texto y el de imagen.
        * Si falta imagen, reposiciónar el recuadro de Obsrv, avarcando
        el espacio de la imagen faltante'
        print("--: ",dicImgs[key][0])'''

    # DICCIONARIO DONDE TOMA LA FUNCIÓN DEPENDIENDO DEL BTN PRECIONADO
    def main(self,page,id,dicImg):
        print(id)
        #'''
        select = {
            'EXTRC' : self.pdfImageExtr,
            'IMPRC' : self.pdfImageImpr,
            'LMNSN' : self.pdfImageLam,
            'RFLD'  : self.pdfImageRef,
            'CNVRSN' : self.pdfImageCnvrs
        }

        # Busca la función en el diccionario
        funcion_seleccionada = select.get(id)
        
        if funcion_seleccionada:
            # Ejecuta la función, pasándole los argumentos necesarios
            funcion_seleccionada(page,id, dicImg)
        else:
            print(f"Opción {id} no encontrada.")