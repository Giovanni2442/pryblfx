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

    def pdfText(self,page):
        rect = fitz.Rect(100,50,110,60)
        borderColor = (0,0,0)

        text = "kiiiiiiiiiiiii"
        text_color = (0, 1, 0)  # Color del texto (negro)
        text_size = 12  # Tamaño de la fuente

        text_rect = fitz.Rect(230, 590, 400, 660) # Cuadro de Texto
        page.draw_rect(text_rect,color=text_color)

        page.insert_textbox(text_rect, text, fontsize=text_size, fontname="helv", color=text_color, align=1)

    def pdfImageExtr(self,page,img):
        # Ruta de la imagen que deseas insertar
        image_path = "Imagenes/img1.png" 
     
        # Crear el nuevo rectángulo en las coordenadas especificadas
         #                   x0  y0   x1   y1 
        txt = "Hola xd"
        text_color = color = (0,1,0)
        text_size = 12
        color = (0,1,0)  # Color gris claro, con valores RGB entre 0 y 1

        # Figuras

        Img_rect = fitz.Rect(70, 587, 180, 660)     # Img. Extrusión
        text_rect = fitz.Rect(190, 587, 400, 660)   # Txt. Extrusión
 
        page.draw_rect(Img_rect,color=color)
        page.draw_rect(text_rect,color=color)
 
        # Sirve para Ingresar Textos dentro del Rectangulo
        page.insert_textbox(text_rect, txt, fontsize=text_size, fontname="helv", color=text_color, align=1)
        page.insert_image(Img_rect, filename=img)        # Insetar la figura

    def pdfImageImpr(self,page,img):
        # Ruta de la imagen que deseas insertar
        image_path = "Imagenes/img1.png" 
     
        # Crear el nuevo rectángulo en las coordenadas especificadas
         #                   x0  y0   x1   y1 
        txt = "Hommmmmmmmmmmmmmmmmmmmmmmmmmmmmmmla xd"
        text_color = color = (0,1,0)
        text_size = 12
        color = (0,1,0)  # Color gris claro, con valores RGB entre 0 y 1

        # Figuras

        Img_rect = fitz.Rect(70, 1095, 200, 1260)     # Img. Extrusión
        text_rect = fitz.Rect(208, 1095, 400, 1260)   # Txt. Extrusión
 
        page.draw_rect(Img_rect,color=color)
        page.draw_rect(text_rect,color=color)
 
        # Sirve para Ingresar Textos dentro del Rectangulo
        page.insert_textbox(text_rect, txt, fontsize=text_size, fontname="helv", color=text_color, align=1)
        page.insert_image(Img_rect, filename=img)   

    def pdfImageLam(self,page):
        # Ruta de la imagen que deseas insertar
        image_path = "Imagenes/img1.png" 
     
        # Crear el nuevo rectángulo en las coordenadas especificadas
         #                   x0  y0   x1   y1 
        txt = "Hommmmmmmmmmmmmmmmmmmmmmmmmmmmmmmla xd"
        text_color = color = (0,1,0)
        text_size = 12
        color = (0,1,0)  # Color gris claro, con valores RGB entre 0 y 1

        # Figuras

        Img_rect = fitz.Rect(438, 701, 550, 795)     # Img. Extrusión
        text_rect = fitz.Rect(560, 701, 765, 795)   # Txt. Extrusión
 
        page.draw_rect(Img_rect,color=color)
        page.draw_rect(text_rect,color=color)
 
        # Sirve para Ingresar Textos dentro del Rectangulo
        page.insert_textbox(text_rect, txt, fontsize=text_size, fontname="helv", color=text_color, align=1)
        page.insert_image(Img_rect, filename=image_path)   

    def pdfImageRef(self,page):
        # Ruta de la imagen que deseas insertar
        image_path = "Imagenes/img1.png" 
     
        # Crear el nuevo rectángulo en las coordenadas especificadas
         #                   x0  y0   x1   y1 
        txt = "Hommmmmmmmmmmmmmmmmmmmmmmmmmmmmmmla xd"
        text_color = color = (0,1,0)
        text_size = 12
        color = (0,1,0)  # Color gris claro, con valores RGB entre 0 y 1

        # Figuras

        Img_rect = fitz.Rect(438, 1155, 550, 1267)     # Img. Extrusión
        text_rect = fitz.Rect(560, 1155, 765, 1267)   # Txt. Extrusión
 
        page.draw_rect(Img_rect,color=color)
        page.draw_rect(text_rect,color=color)
 
        # Sirve para Ingresar Textos dentro del Rectangulo
        page.insert_textbox(text_rect, txt, fontsize=text_size, fontname="helv", color=text_color, align=1)
        page.insert_image(Img_rect, filename=image_path)

    def pdfImageCnvrs(self,page):
        # Ruta de la imagen que deseas insertar
        image_path = "Imagenes/img1.png" 
     
        # Crear el nuevo rectángulo en las coordenadas especificadas
         #                   x0  y0   x1   y1 
        txt = "Hommmmmmmmmmmmmmmmmmmmmmmmmmmmmmmla xd"
        text_color = color = (0,1,0)
        text_size = 12
        color = (0,1,0)  # Color gris claro, con valores RGB entre 0 y 1

        # Figuras

        Img_rect = fitz.Rect(800, 540, 940, 776)     # Img. Extrusión
        text_rect = fitz.Rect(950, 540, 1125, 776)   # Txt. Extrusión
 
        page.draw_rect(Img_rect,color=color)
        page.draw_rect(text_rect,color=color)
 
        # Sirve para Ingresar Textos dentro del Rectangulo
        page.insert_textbox(text_rect, txt, fontsize=text_size, fontname="helv", color=text_color, align=1)
        page.insert_image(Img_rect, filename=image_path)   

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
    
    def main(self,page,img):
        self.pdfImageExtr(page,img),
        self.pdfImageImpr(page,img),
        #self.pdfImageLam(page),
        #self.pdfImageRef(page),
        #self.pdfImageCnvrs(page),
        #self.pdfSecuen(page)