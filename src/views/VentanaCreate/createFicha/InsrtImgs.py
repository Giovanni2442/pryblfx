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

    def pdfImage(self,page):
        # Ruta de la imagen que deseas insertar
        image_path = "Imagenes/img1.png" 
        #                x0 : Altura y0 : Ancho x1 : Ancho Figura y1 : Altura Figura
        rect = fitz.Rect(50, 50, 100, 100)

        width = rect.width
        height = rect.height

        # Define la nueva posición para el rectángulo
        new_x0, new_y0 = 150, 150  # Nuevas coordenadas de la esquina superior izquierda

        # Calcula las nuevas coordenadas de la esquina inferior derecha
        new_x1 = new_x0 + width
        new_y1 = new_y0 + height

        print("-->",new_x1," ","-->",new_y1)

        # Crear el nuevo rectángulo en las coordenadas especificadas
         #                   x0  y0   x1   y1 
        
        ###### ESTE ES EL CHID0 #######
        new_rect = fitz.Rect(70, 590, 170, 660) # Figura
        text_rect = fitz.Rect(170, 590, 270, 660) # Cuadro de Texto
        ################################
        # Dibuja un rectángulo con color de fondo
        color = (0,1,0)  # Color gris claro, con valores RGB entre 0 y 1
        
        #page.draw_rect(rect, color=color, fill_opacity=1)
        page.draw_rect(new_rect,color=color)
        page.draw_rect(text_rect,color=color)

        # Sirve para Ingresar Textos dentro del Rectangulo
        text_rect = page.insert_textbox(rect, text, fontsize=text_size, fontname="helv", color=text_color, align=1)


        # Inserta la imagen en la página
        #page.insert_image(rect, filename=image_path)
        page.insert_image(new_rect, filename=image_path)        # Insetar la figura
        page.insert_image(text_rect)