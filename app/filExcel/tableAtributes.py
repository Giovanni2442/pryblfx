class atrFichTec:
    def __init__(self,fila):
        self.codPrintCrd = fila['CODIGO PRINT CARD']
        self.cliente = fila['CLIENTE']
        self.fechaElav = fila['FECHA']
        self.product = fila['PRODUCTO']
        self.fecha = str(self.fechaElav.strftime('%d/%m/%y'))
        self.mensajes = "campo vacio!","El codigo es Incorrecto!","La fecha es Incorrecta!","Error en Cliente!"

    def getAllAtr(this):
        return this.codPrintCrd,this.cliente,this.fecha,this.product

class atrVentas:
    def __init__(self,fila):
        #NOTA : Para esta tabla faltaria el atributo "PRODUCTO LAMINADO"
        #self.product_Laminado = None
        self.asesor = fila['ASESOR COMERCIAL DE LA CUENTA']
        self.tipoEmpq = fila['TIPO DE EMPAQUE']
        self.estruct = fila['ESTRUCTURA']
        self.empaca = fila['PRODUCTO QUE SE EMPACA']
        self.mensajes = "campo vacio!","Los caracteres son Incorrectos!","Error en la Estructura!"

    def getAllAtr(this):
        return this.asesor,this.tipoEmpq,this.estruct,this.empaca

 # --- TABLA PRINCIPAL DE EXTRUCCIÓN ---   
class atrExtruccion:
    def __init__(self,fila):
        # Atributos Atomicos
        self.tipoMtrl = fila['TIPO DE MATERIAL A EXTRUIR']
        self.dinaje = fila['DINAJE REQUERIDO']
        self.formula = fila['FÓRMULA DEL LDPE']
        self.pigmento = None                        #Hace falta el pigmento del producto, no se encuentra en las capturas
        self.tipoBob = fila['TIPO DE BOBINA']       #
        self.tipoTrat = fila['TIPO DE TRATADO']
        self.maxEmplm = None                        #Averiguar como sacar este campo : IMPRESIÓN
        self.orntBobTrm = None                      #Averiguar como sacar este campo : IMPRESIÓN     
        self.tipoEmpqBob = None                     #Averiguar como sacar este campo : IMPRESIÓN
        self.pesarProduct = None                    #Averiguar como sacar este campo : IMPRESIÓN
        self.etiquetado = None                      #Averiguar como sacar este campo : IMPRESIÓN
        self.numBobTarima = None                    #Averiguar como sacar este campo : REFILADO
        self.tarimaEmplaya = None                   #Averiguar como sacar este campo : REFILADO
        self.tarimaFlejada = None                   #Averiguar como sacar este campo : REFILADO

        # --- CalibrePel_Tolr ---
        self.calibre = fila['CALIBRE GAUGES']       #
        self.calTol = fila['TOLERANCIA']            # NOTA : Aqui hay varias tablas que se llaman tolerancia, arreglar eso

        # --- Ancho de Bobina y Tolerancia ---
        self.anchBob = ['ANCHO DE BOBINA (CM)']     #Esto se tomo de la tabla de IMPRECIÓN
        self.anchBobTol = ['TOLERANCIA (CM)']       #Esto se tomo de la tabla de IMPRECIÓN

        # --- Ancho de Core y Tolerancia ---
        self.anchCore = ['ANCHO DE CORE (CM)']      # Se toma de la Tabla de Laminado 
        self.anchCoreTol = ['TOLERANCIA']           # Se toma de la tabla de Laminado

        # --- Diametro de Bobina y Tolerancia ---
        self.diamBob = ['DIÁMETRO DE BOBINA (CM)']  # se toma de la tabla de Impresión
        self.diamBobTol = ['TOLERANCIA CM']            

        # --- Peso promedio por bobina ---
        self.pesoBob = ['PESO NETO PROMEDIO DE BOBINA (KG)']                         # Existe en Impresión y Laminado, se tomo la de Laminado
        self.pesoBobTol = ['TOLERANCIA']  

        # --- Numero de bobinas por cama y camas por tarima ---
        self.numBobCama = ['NUMERO DE BOBINAS POR CAMA (PZ)']  # se toma de la tabla de Impresión
        self.cmsTarima = ['CAMAS POR TARIMA (PZ)']  

        # --- peso neto promedio por tarima --- 
        self.pesoNetoTam = ['PESO NETO PROMEDIO POR TARIMA (KG)']       # se toma de la tabla de Impresión
        self.pesoPromTamTol = ['TOLERANCIA']                            # se toma de la tabla de Impresión
    
    def getAllAtr(this):
        return this.asesor,this.tipoEmpq,this.estruct,this.empaca

class atrImpresion:
    def __init__(self):
        self.matImpr = ['MATERIAL A IMPRIMIR']
        self.dinaje = ['DINAJE']
        self.grosorCore = None                          # Averiguar como sacar este atributo
        self.dsrrllImpr = ['DESARROLLO A IMPRIMIR mm (MANGA)']
        self.repEje = ['REPETICIONES AL EJE']
        self.repDesrr = ['REPETICIONES AL DESARROLLO']
        self.cantTinImpr = ['CANTIDAD DE TINTAS A IMPRIMIR']
        self.tipImpr = ['TIPO DE IMPRESION']
        self.tipoTintasUtilizar = ['TIPO DE TINTAS A UTILIZAR']
        self.tipoBarniz = ['TIPO DE BARNIZ']
        self.figEmbobImpr = ['sentido de embobinado(Figura de Embobinado)']
        self.maxEmpalmes = ['MÁXIMO DE EMPALMES POR BOBINA']
        self.tipoEmpaqBob = ['TIPO DE EMPAQUE PARA BOBINA']
        self.orientBobTarima = ['ORIENTACIÓN DE BOBINA EN TARIMA']
        self.pesarProduct = ['PESAR PRODUCTO POR']
        self.etiquetado = ['ETIQUETADO']
        self.NumbobTarima = ['NUMERO DE BOBINAS POR CAMA']
        self.tarimaEmplaye = None                      # Averiguar como sacar este atributo
        self.tarimaFlejada = None                      # Averiguar como sacar este atributo

        # --- Calibre del material y Tolerancia ---
        self.calibre = ['']
        self.calibreTol = ['']

        # --- Ancho de bobina a imprimir y tolerancia ---
        self.anchBob = ['']
        self.anchBobTol = ['']

        # --- Ancho de core y tolerancia
        self.anchCore = ['']
        self.anchCoreTol = ['']

        # --- Validación de color ---
        self.validClr = ['VALIDACIÓN DE COLOR']        
        self.combinacion = ['']     #Varifica esto

        # --- Diametro de bobina y Tolerancia ---
        self.diamBob = ['DIÁMETRO DE BOBINA (CM)']
        self.diamBobTol = ['TOLERANCIA CM']

        # --- Peso neto promedio de bobina ---
        self.pesoPromBob = ['PESO NETO PROMEDIO DE BOBINA (KG)']
        self.pesoPromBobTol = ['TOLERANCIA']

        # --- Numero de bobinas por cama y camas por tarima ---
        self.psoBobCama = ['NUMERO DE BOBINAS POR CAMA']
        self.psoBobCamaTol = ['CAMAS POR TARIMA (PZ)']

class atrLaminado:
    def __init__(self):
        self.estructProduct = ['ESTRUCTURA']        # Se toma de la tabla de Ventas 
        self.tipoTratado = ['TIPO DE TRATADO']
        self.maxEmpalmesBob = ['MÁXIMO DE EMPALMES POR BOBINA']
        self.orientBobRack = None                   # Averiguar de donde se saca el atributo
        self.tipoEmpaqBob = ['TIPO DE EMPAQUE PARA BOBINA']
        self.etiquetado = ['ETIQUETADO']
        self.pesarProduct = ['PESAR PRODUCTO POR']  # Se toma de la tabla de Impresión

        # --- Medida de la manga para la Transferencia --
        self.medidaManga = ['MEDIDA DE LA MANGA PARA TRANSFERENCIA (CM)']
        self.medidaMangaTol = None                  # Averiguar de donde se saca el atributo 

        # --- Ancho de core y Tolerancia ---
        self.anchoCore = ['ANCHO DE CORE (CM)']
        self.anchoCoreTol = ['TOLERANCIA']

        # --- Diametro y Grosor de core --- 
        self.diametro = None            # Averiguar de donde se saca el atributo
        self.grosorCore = None          # Averiguar de donde se saca el atributo

        # --- Diametro de bobina y Tolerancia ---
        self.diametroBob = ['DIÁMETRO DE BOBINA (CM)']                      
        self.diametroBobTol = ['TOLERANCIA (CM)']

        # --- Peso promedio por bobina y Tolerancia ---
        self.pesoPromBob = ['PESO NETO PROMEDIO DE BOBINA (KG)']
        self.pesoPromBobTol = ['TOLERANCIA']

     # --- Material Impreso ---
    class materialImpreso:
        def __init__(self):
            self.tipoTratado = ['TIPO DE TRATADO']          # NOTA : EXISTEN MAS TRATADOS EN EL EXCEL
            # --- Calibre de pelicula y Tolerancia --
            self.calibre = ['CALIBRE gauges','CALIBRE Micras']              # Existe en GAUGUES Y EN MICRAS. Si  en GAUGUES se coloca en GAUGUES
            self.calTol = ['TOLERANCIA']
            # --- Ancho de Bobina y Tolerancia ---
            self.anchoBob = ['ANCHO DE BOBINA (CM)']
            self.anchoBobTol = ['TOLERANCIA (CM)']

    class Laminacion_1:
        def __init__(self):
            self.material = ['MATERIAL 1 LAM (CLAVE SAP)']
            self.tipoTratado = ['TIPO DE TRATADO']
            self.tipoLamin = None               # Averiguar de donde se saca el atributo    
            # --- Calibre de pelicula y Tolerancia Laminación 1 ---
            self.calPel = ['CALIBRE MICRAS (GAUGES/4)']         # POSICIÓN "CA"
            self.calPelTol = ['TOLERANCIA']                     #  POSICIÓN "CB"
            # --- Ancho de Bobina y Tolerancia Laminación 1 ---
            self.anchoBob = ['ANCHO DE BOBINA (CM)']
            self.anchoBobTol = ['TOLERANCIA (CM)']              # POSICIÓN "CE"

    class Laminacion_2:
        def __init__(self):
            self.material = ['MATERIAL 2 LAM (CLAVE SAP)']
            self.tipoTratado = ['TIPO DE TRATADO']              # POSICIÓN "CO"
            self.tipoLamin = None                                   # Averiguar de donde se saca el atributo    
            # --- Calibre de pelicula y Tolerancia Laminación 1 ---
            self.calPel = ['CALIBRE GAUGES']                    # POSICIÓN "CI" NOTA : SI LLEGA ALAMINACIÓN 2 ESTE ATRIBUTO, TIENE QUE TENER TOLERANCIA
            self.calPelTol = ['TOLERANCIA']                      # POSICIÓN "CK"
            # --- Ancho de Bobina y Tolerancia Laminación 1 ---
            self.anchoBob = ['ANCHO DE BOBINA (CM)']            # POSICIÓN "CL"
            self.anchoBobTol = ['TOLERANCIA (CM)']              # POSICIÓN "CN"

    class Laminacion_3:
        def __init__(self):
            self.tipoTratado = None
            self.tipoLamin =  None
            # --- Calibre de pelicula y Tolerancia Laminación 1 ---
            self.calPel =  None
            self.calPelTol =  None
            # --- Ancho de Bobina y Tolerancia Laminación 1 ---
            self.anchoBob =  None
            self.anchoBobTol =  None

    class Laminacion_4:
        def __init__(self):
            self.tipoTratado =  None
            self.tipoLamin =  None
            # --- Calibre de pelicula y Tolerancia Laminación 1 ---
            self.calPel =  None
            self.calPelTol =  None
            # --- Ancho de Bobina y Tolerancia Laminación 1 ---
            self.anchoBob =  None
            self.anchoBobTol =  None
            
class atrRefilado:
    def __init__(self):
        self.proceso = ['']
        self.acabadoBob = ['']
        self.grosorCore = ['']
        self.figEmbobImpr = ['']
        self.bobinaRefilar = ['']
        self.maximoEmpal = ['']
        self.señalEmpl = ['']
        self.orientBobTarima = ['']
        self.tipoEmpaque = ['']
        self.pesarPrdct = ['']
        self.etiquetado = ['']
        self.tarimaEmplaye = ['']
        self.tarimaFlejada = ['']
        # --- Ancho final de bobina al refilarse/Doblarse y Tolerancia ---
        self.anchoFinalBob = ['']
        self.anchoFinalBobTol = ['']
        # --- Ancho de core y Tolerancia ---
        self.anchoCore = ['']
        self.anchoCoreTol = ['']
        # --- Metros por bobina al refilarse/doblarse y tolerancia ---
        self.metrosBob = ['']
        self.metrosBobTol = ['']
        # --- Diametro de bobina al refilarse/doblarse y tolerancia ---
        self.diametroRef = ['']
        self.diametroRefTol = ['']
        # --- Peso neto promedio por bobina ---
        self.pesoNetPromBob = ['']
        self.pesoNetPromBobTol = ['']
        # --- Numero de bobinas por cama y camas por tarima ---



# --------- FUNCIÓNES DE PRUEBAS -----------------
class pruebas:
    def __init__(self,fila):
        self.codPrintCrd = fila['CODIGO PRINT CARD'],'CODIGO PRINT CARD'
        self.cliente = fila['CLIENTE'],'CLIENTE'
        self.fechaElav = fila['FECHA']
        self.product = fila['PRODUCTO'],'PRODUCTO'
        self.fecha = str(self.fechaElav.strftime('%d/%m/%y')),'FECHA'
    def atrFichTec(this):
        #this.fecha = str(this.fechaElav.strftime('%d/%m/%y'))
        return str(this.codPrintCrd[0]),this.cliente[0],this.fecha[0],this.product[0]
#---------------------------------------------------