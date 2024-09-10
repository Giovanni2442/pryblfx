class prInrs:
    def __init__(self):
        template = "Template/Template.pdf"
        self.doc = fitz.open(template)  # Asegúrate de abrir el PDF correcto
    
    def pruebas(self):
        color = (0, 1, 0)  # Color gris claro, con valores RGB entre 0 y 1

        # Asegúrate de acceder a la página correcta del PDF
        page = self.doc[0]  # Cambia el índice a la página que necesites

        ########### PRUEBAS #################

         # Otro rectángulo para una imagen
        # X = Representa el ancho de la figura
        # Y = Altura de la figura
        # X1 , Y1 , X2 , Y2

 ############################EXTRUSION PROCESO############################################
                ## -- PROCESO rectangulo EXTRS -- ##
        rectExtrs = fitz.Rect(880, 810, 1045, 865)  # Img. Extrusión
        page.draw_rect(rectExtrs, color=color)
                ## -- FLECHA EXTRUSION -- ##
        arrwExtrs = [
            # X , Y
            fitz.Point(955,870),  # punta Izq de la Base SUPERIOR    P1
            fitz.Point(975,870),  # punta derch de la Base SUPERIOR  P2
            fitz.Point(975,880),  # Base derecha   INFERIOR          P3
            fitz.Point(985,880),  # Punta derecha de la flecha       P4
            fitz.Point(965,890),  # Punta de la flecha (INFERIOR)    P5
            fitz.Point(945,880),  # Punta izquierda de la flecha     P6   
            fitz.Point(955,880),  # Base izquierda INFERIOR          P7
        ]

        # Dibuja el polígono con los puntos especificados
        page.draw_polyline(arrwExtrs, color=color, fill=color) 
##########################################################################################


 ############################IMPRESION PROCESO############################################
                ## -- PROCESO rectangulo -- ##
        rectImprs = fitz.Rect(880, 895, 1045, 950)  # Img. Extrusión
        page.draw_rect(rectImprs, color=color)
                ## -- FLECHA EXTRUSION -- ##
        arrwImprs = [
            # X , Y
            fitz.Point(955,955),  # punta Izq de la Base SUPERIOR    P1
            fitz.Point(975,955),  # punta derch de la Base SUPERIOR  P2
            fitz.Point(975,965),  # Base derecha   INFERIOR          P3
            fitz.Point(985,965),  # Punta derecha de la flecha       P4
            fitz.Point(965,975),  # Punta de la flecha (INFERIOR)    P5
            fitz.Point(945, 965),  # Punta izquierda de la flecha     P6   
            fitz.Point(955,965),  # Base izquierda INFERIOR          P7
        ]

        # Dibuja el polígono con los puntos especificados
        page.draw_polyline(arrwImprs, color=color, fill=color) 
##########################################################################################

 ############################LAMINADO PROCESO############################################
                ## -- PROCESO rectangulo -- ##
        rectImprs = fitz.Rect(880, 975, 1045, 1030)  # Img. Extrusión
        page.draw_rect(rectImprs, color=color)
                ## -- FLECHA EXTRUSION -- ##
        arrwImprs = [
            # X , Y
            fitz.Point(955,1035),  # punta Izq de la Base SUPERIOR    P1
            fitz.Point(975,1035),  # punta derch de la Base SUPERIOR  P2
            fitz.Point(975,1045),  # Base derecha   INFERIOR          P3
            fitz.Point(985,1045),  # Punta derecha de la flecha       P4
            fitz.Point(965,1055),  # Punta de la flecha (INFERIOR)    P5
            fitz.Point(945, 1045),  # Punta izquierda de la flecha     P6   
            fitz.Point(955,1045),  # Base izquierda INFERIOR          P7
        ]

        # Dibuja el polígono con los puntos especificados
        page.draw_polyline(arrwImprs, color=color, fill=color) 
##########################################################################################

 ############################REFILADO PROCESO############################################
                ## -- PROCESO rectangulo -- ##
        rectImprs = fitz.Rect(880, 1055, 1045, 1110)  # Img. Extrusión
        page.draw_rect(rectImprs, color=color)
                ## -- FLECHA EXTRUSION -- ##
        arrwImprs = [
            # X , Y
            fitz.Point(955,1115),  # punta Izq de la Base SUPERIOR    P1
            fitz.Point(975,1115),  # punta derch de la Base SUPERIOR  P2
            fitz.Point(975,1125),  # Base derecha   INFERIOR          P3
            fitz.Point(985,1125),  # Punta derecha de la flecha       P4
            fitz.Point(965,1135),  # Punta de la flecha (INFERIOR)    P5
            fitz.Point(945, 1125),  # Punta izquierda de la flecha     P6   
            fitz.Point(955,1125),  # Base izquierda INFERIOR          P7
        ]

        # Dibuja el polígono con los puntos especificados
        page.draw_polyline(arrwImprs, color=color, fill=color) 
##########################################################################################

 ############################CONVERSION PROCESO############################################
                ## -- PROCESO rectangulo -- ##
        rectImprs = fitz.Rect(880, 1135, 1045, 1190)  # Img. Extrusión
        page.draw_rect(rectImprs, color=color)
                ## -- FLECHA EXTRUSION -- ##
        arrwImprs = [
            # X , Y
            fitz.Point(955,1195),  # punta Izq de la Base SUPERIOR    P1
            fitz.Point(975,1195),  # punta derch de la Base SUPERIOR  P2
            fitz.Point(975,1205),  # Base derecha   INFERIOR          P3
            fitz.Point(985,1205),  # Punta derecha de la flecha       P4
            fitz.Point(965,1215),  # Punta de la flecha (INFERIOR)    P5
            fitz.Point(945, 1205),  # Punta izquierda de la flecha     P6   
            fitz.Point(955,1205),  # Base izquierda INFERIOR          P7
        ]

        # Dibuja el polígono con los puntos especificados
        page.draw_polyline(arrwImprs, color=color, fill=color) 
##########################################################################################

 ############################PROCESO TERMINADO############################################
                ## -- PROCESO rectangulo -- ##
        rectImprs = fitz.Rect(880, 1215, 1045, 1260)  # Img. Extrusión
        page.draw_rect(rectImprs, color=color)
        
##########################################################################################

        # Guarda el documento modificado
        self.temp_filename = "Template/Template_temp.pdf"
        self.doc.save(self.temp_filename)
        self.doc.close()

# Ejecuta la prueba
crpdf = prInrs()
crpdf.pruebas()