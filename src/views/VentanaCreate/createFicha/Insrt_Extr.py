
# Insertar Valores del formulario EXTRUSION al pdf 
class Insrt_Extr():
    def __init__(self):
        self.vl = 7
    
    # Tabla de Extrusion
    def pdfExtru(self,page):
        vl = 9
        page.insert_text(   
            (320, 271),
            text= "MATERIAL",
            color=(0, 0, 0),
            fontsize=self.vl,
            fontname="Helvetica-Bold"
        )

        # Dinaje Requerido
        page.insert_text(   
            (320, 285),
            text= "DINAJE",
            color=(0, 0, 0),
            fontsize=self.vl,
            fontname="Helvetica-Bold"
        )

        # FÓRMULA CON LA QUE SE EXTRUIRÁ LA BOBINA
        page.insert_text(   
            (320, 299),
            text= "FÓRMULA",
            color=(0, 0, 0),
            fontsize=self.vl,
            fontname="Helvetica-Bold"
        )

        # PIGMENTO DE PELÍCULA: (SI (especificar color), N/A)
        page.insert_text(   
            (320, 313),
            text= "PIGMENTO",
            color=(0, 0, 0),
            fontsize=self.vl,
            fontname="Helvetica-Bold"
        )

        # CALIBRE DE LA PELÍCULA Y TOLERANCIA
        page.insert_text(   
            (320, 328),
            text= "CALIBRE",
            color=(0, 0, 0),
            fontsize=self.vl,
            fontname="Helvetica-Bold"
        )

        # TIPO DE BOBINA: 
        page.insert_text(   
            (320, 341),
            text= "TRATADO",
            color=(0, 0, 0),
            fontsize=self.vl,
            fontname="Helvetica-Bold"
        )

        # TIPO DE TRATADO: 
        page.insert_text(   
            (320, 355),
            text= "BOBINA",
            color=(0, 0, 0),
            fontsize=self.vl,
            fontname="Helvetica-Bold"
        )

        # ANCHO DE BOBINA Y TOLERANCIA 
        page.insert_text(   
            (320, 369),
            text= "ANCHO",
            color=(0, 0, 0),
            fontsize=self.vl,
            fontname="Helvetica-Bold"
        )

        # ANCHO DE CORE Y TOLERANCIA 
        page.insert_text(   
            (320, 384),
            text= "CORE",
            color=(0, 0, 0),
            fontsize=self.vl,
            fontname="Helvetica-Bold"
        )

        # DIÁMETRO DE BOBINA Y TOLERANCIA
        page.insert_text(   
            (320, 398),
            text= "DIÁMETRO",
            color=(0, 0, 0),
            fontsize=self.vl,
            fontname="Helvetica-Bold"
        )

        # MÁXIMO DE EMPALMES POR BOBINA
        page.insert_text(   
            (320, 412),
            text= "EMPLAMES",
            color=(0, 0, 0),
            fontsize=self.vl,
            fontname="Helvetica-Bold"
        )

        # ORIENTACIÓN DE BOBINA EN TARIMA: (HORIZONTAL/ VERTICAL)
        page.insert_text(   
            (320, 426),
            text= "ORIENTACIÓN",
            color=(0, 0, 0),
            fontsize=self.vl,
            fontname="Helvetica-Bold"
        )

        # TIPO DE EMPAQUE PARA BOBINA: (EMPLAYE / BOLSA / N/A)
        page.insert_text(   
            (320, 440),
            text= "EMPQ",
            color=(0, 0, 0),
            fontsize=self.vl,
            fontname="Helvetica-Bold"
        )

        # PESAR PRODUCTO POR: (TARIMA / BOBINA / AMBOS)
        page.insert_text(   
            (320, 454),
            text= "PESAR PRDCT",
            color=(0, 0, 0),
            fontsize=self.vl,
            fontname="Helvetica-Bold"
        )

        # PESO NETO PROMEDIO DE BOBINA
        page.insert_text(   
            (320, 468),
            text= "PSNTO",
            color=(0, 0, 0),
            fontsize=self.vl,
            fontname="Helvetica-Bold"
        )

        # ETIQUETADO
        page.insert_text(   
            (320, 482),
            text= "ETIQUETADO",
            color=(0, 0, 0),
            fontsize=self.vl,
            fontname="Helvetica-Bold"
        )

        # NUMERO DE BOBINAS POR CAMA Y CAMAS POR TARIMA
        page.insert_text(   
            (320, 496),
            text= "NUMERO",
            color=(0, 0, 0),
            fontsize=self.vl,
            fontname="Helvetica-Bold"
        )

        # NUMERO DE BOBINAS EN TARIMA
        page.insert_text(   
            (320, 511),
            text= "TARIMA",
            color=(0, 0, 0),
            fontsize=self.vl,
            fontname="Helvetica-Bold"
        )

        # PESO NETO PROMEDIO POR TARIMA
        page.insert_text(   
            (320, 525),
            text= "PROMEDIO",
            color=(0, 0, 0),
            fontsize=self.vl,
            fontname="Helvetica-Bold"
        )

        # LA TARIMA LLEVARA EMPLAYE: (APLICA / N/A)
        page.insert_text(   
            (320, 539),
            text= "EMPLAYE",
            color=(0, 0, 0),
            fontsize=self.vl,
            fontname="Helvetica-Bold"
        )

        # LA TARIMA SERA FLEJADA: (APLICA / N/A)
        page.insert_text(   
            (320, 553),
            text= "FLEJADA",
            color=(0, 0, 0),
            fontsize=self.vl,
            fontname="Helvetica-Bold"
        )

        #############################

        #### -- TABLA IMPRESIÓN -- #####
        
        # MATERIAL A IMPRIMIR
        page.insert_text(   
            (320, 693),
            text= "EXTRUCIÓN",
            color=(0, 0, 0),
            fontsize=self.vl,
            fontname="Helvetica-Bold"
        )

        # DINAJE REQUERIDO PARA SU IMPRESIÓN
        page.insert_text(   
            (320, 707),
            text= "DINAJE",
            color=(0, 0, 0),
            fontsize=self.vl,
            fontname="Helvetica-Bold"
        )

        # CALIBRE DEL MATERIAL A IMPRIMIR Y TOLERANCIA
        page.insert_text(   
            (320, 721),
            text= "CALIBRE",
            color=(0, 0, 0),
            fontsize=self.vl,
            fontname="Helvetica-Bold"
        )

        # ANCHO DE BOBINA A IMPRIMIR Y TOLERANCIA 
        page.insert_text(   
            (320, 735),
            text= "ANCHO",
            color=(0, 0, 0),
            fontsize=self.vl,
            fontname="Helvetica-Bold"
        )

        # GROSOR DE CORE:  (10 MM / OTRO) 
        page.insert_text(   
            (320, 748),
            text= "GROSOR",
            color=(0, 0, 0),
            fontsize=self.vl,
            fontname="Helvetica-Bold"
        )

        # ANCHO DE CORE Y TOLERANCIA  
        page.insert_text(   
            (320, 763),
            text= "GROSOR",
            color=(0, 0, 0),
            fontsize=self.vl,
            fontname="Helvetica-Bold"
        )
        
        # DESARROLLO A IMPRIMIR (MANGA)  
        page.insert_text(   
            (320, 777),
            text= "DESARROLLO",
            color=(0, 0, 0),
            fontsize=self.vl,
            fontname="Helvetica-Bold"
        )

        # REPETICIONES AL EJE  
        page.insert_text(   
            (320, 792),
            text= "EJE",
            color=(0, 0, 0),
            fontsize=self.vl,
            fontname="Helvetica-Bold"
        )

        # REPETICIONES AL DESARROLLO 
        page.insert_text(   
            (320, 806),
            text= "DESARROLLO",
            color=(0, 0, 0),
            fontsize=self.vl,
            fontname="Helvetica-Bold"
        )

        # CANTIDAD DE TINTAS A IMPRIMIR 
        page.insert_text(   
            (320, 820),
            text= "TINTAS",
            color=(0, 0, 0),
            fontsize=self.vl,
            fontname="Helvetica-Bold"
        )

        # TIPO DE IMPRESIÓN: (INTERNA/EXTERNA) 
        page.insert_text(   
            (320, 834),
            text= "IMPRESIÓN",
            color=(0, 0, 0),
            fontsize=self.vl,
            fontname="Helvetica-Bold"
        )

        # TIPO DE TINTAS A UTILIZAR 
        page.insert_text(   
            (320, 848),
            text= "UTILIZAR",
            color=(0, 0, 0),
            fontsize=self.vl,
            fontname="Helvetica-Bold"
        )

        # TIPO DE BARNIZ SOBRE LA IMPRESIÓN 
        page.insert_text(   
            (320, 862),
            text= "BARNIZ",
            color=(0, 0, 0),
            fontsize=self.vl,
            fontname="Helvetica-Bold"
        )

        # FIGURA DE EMBOBINADO AL SALIR DE IMPRESIÓN (1,2,3,4,5,6,7,8)
        page.insert_text(   
            (320, 876),
            text= "EMBOBINADO",
            color=(0, 0, 0),
            fontsize=self.vl,
            fontname="Helvetica-Bold"
        )

        # VALIDACIÓN DE COLOR POR
        page.insert_text(   
            (320, 891),
            text= "VALIDACIÓN",
            color=(0, 0, 0),
            fontsize=self.vl,
            fontname="Helvetica-Bold"
        )

        # MÁXIMO DE EMPALMES POR BOBINA
        page.insert_text(   
            (320, 906),
            text= "MÁXIMO",
            color=(0, 0, 0),
            fontsize=self.vl,
            fontname="Helvetica-Bold"
        )

        # TIPO DE EMPAQUE PARA BOBINA
        page.insert_text(   
            (320, 920),
            text= "EMPAQUE",
            color=(0, 0, 0),
            fontsize=self.vl,
            fontname="Helvetica-Bold"
        )

        # ORIENTACIÓN DE BOBINA EN TARIMA: 
        page.insert_text(   
            (320, 934),
            text= "ORIENTACIÓN",
            color=(0, 0, 0),
            fontsize=self.vl,
            fontname="Helvetica-Bold"
        )

        # PESAR PRODUCTO POR:
        page.insert_text(   
            (320, 948),
            text= "PESAR",
            color=(0, 0, 0),
            fontsize=self.vl,
            fontname="Helvetica-Bold"
        )

        # DIÁMETRO DE BOBINA Y TOLERANCIA 
        page.insert_text(   
            (320, 962),
            text= "DIÁMETRO",
            color=(0, 0, 0),
            fontsize=self.vl,
            fontname="Helvetica-Bold"
        )

         # PESO NETO PROMEDIO DE BOBINA  
        page.insert_text(   
            (320, 976),
            text= "PESO",
            color=(0, 0, 0),
            fontsize=self.vl,
            fontname="Helvetica-Bold"
        )

        # ETIQUETADO  
        page.insert_text(   
            (320, 991),
            text= "ETIQUETADO",
            color=(0, 0, 0),
            fontsize=self.vl,
            fontname="Helvetica-Bold"
        )

        # NUMERO DE BOBINAS POR CAMA Y CAMAS POR TARIMA   
        page.insert_text(   
            (320, 1005),
            text= "CAMAS",
            color=(0, 0, 0),
            fontsize=self.vl,
            fontname="Helvetica-Bold"
        )

        # NUMERO DE BOBINAS EN TARIMA    
        page.insert_text(   
            (320, 1019),
            text= "TARIMA",
            color=(0, 0, 0),
            fontsize=self.vl,
            fontname="Helvetica-Bold"
        )

         # PESO NETO PROMEDIO POR TARIMA   
        page.insert_text(   
            (320, 1032),
            text= "PROMEDIO",
            color=(0, 0, 0),
            fontsize=self.vl,
            fontname="Helvetica-Bold"
        )

         # LA TARIMA LLEVARA EMPLAYE: (APLICA / N/A)  
        page.insert_text(   
            (320, 1047),
            text= "EMPLAYE",
            color=(0, 0, 0),
            fontsize=self.vl,
            fontname="Helvetica-Bold"
        )

        # LA TARIMA SERA FLEJADA: (APLICA / N/A)
        page.insert_text(   
            (320, 1061),
            text= "FLEJADA",
            color=(0, 0, 0),
            fontsize=self.vl,
            fontname="Helvetica-Bold"
        )

        ## -- ELEMENTOS DE PRUEBA --- ###
        # Tip material a extruir
        page.insert_text(   
            (320, 1075),
            text= "PANCH000000",
            color=(0, 1, 0),
            fontsize=self.vl,
            fontname="Helvetica-Bold"
        )

        ##################################
