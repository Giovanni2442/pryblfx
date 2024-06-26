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
        self.mensajes = "campo vacio!",
        "Los caracteres son Incorrectos!",
        "Error en la Estructura!"

    def getAllAtr(this):
        return this.asesor,this.tipoEmpq,this.estruct,this.empaca

 # --- TABLA PRINCIPAL DE EXTRUCCIÓN ---   
class atrExtruccion:
    def __init__(self,fila):
        # Atributos Atomicos
        self.tipoMtrl = fila['TIPO DE MATERIAL A EXTRUIR']      # O        
        self.dinaje = fila['DINAJE REQUERIDO']                  # P
        self.formula = fila['FÓRMULA DEL LDPE']                 # Q
        self.pigmento = None                                    # No se encuentra en capturas pigmento
        self.tipoBob = fila['TIPO DE BOBINA']                   # V
        self.tipoTrat = fila['TIPO DE TRATADO']                 # W
        self.maxEmplm = ['MÁXIMO DE EMPALMES POR BOBINA']       # IMPRESIÓN en BE "VERIFICAR ESTO"
        self.orntBobTrm = ['ORIENTACIÓN DE BOBINA EN TARIMA']   # IMPRESIÓN en BG "VERIFICAR ESTO"     
        self.tipoEmpqBob = ['TIPO DE EMPAQUE PARA BOBINA']      # IMPRESIÓN en BF "VERIFICAR ESTO" 
        self.pesarProduct = ['PESAR PRODUCTO POR']              # IMPRESIÓN en BH "VERIFICAR ESTO"
        self.etiquetado = None                                  # Averiguar como sacar este campo : IMPRESIÓN "BM" o REFILADO "DQ" 
        self.numBobTarima = ['NUMERO DE BOBINAS EN TARIMA (PZ)']  # REFILADO en DT
        self.tarimaEmplaya = None                               #Averiguar como sacar este campo : REFILADO
        self.tarimaFlejada = None                               #Averiguar como sacar este campo : REFILADO

        # --- CalibrePel_Tolr ---
        self.calibre = fila['CALIBRE GAUGES']       # T
        self.calTol = fila['TOLERANCIA']            # U

        # --- Ancho de Bobina y Tolerancia ---
        self.anchBob = ['ANCHO DE BOBINA (CM)']     # Y
        self.anchBobTol = ['TOLERANCIA (CM)']       # Z

        # --- Ancho de Core y Tolerancia ---
        self.anchCore = ['ANCHO DE CORE (CM)']      # Laminado en CS
        self.anchCoreTol = ['TOLERANCIA']           # Laminado en CT

        # --- Diametro de Bobina y Tolerancia ---
        self.diamBob = ['DIÁMETRO DE BOBINA (CM)']  # Impresión en BI
        self.diamBobTol = ['TOLERANCIA CM']         # Impreción en BJ           

        # --- Peso promedio por bobina ---
        self.pesoBob = ['PESO NETO PROMEDIO DE BOBINA (KG)']    # Existe en Impresión y Laminado, se tomo la de Laminado en CX
        self.pesoBobTol = ['TOLERANCIA']                        # NO COINCIDE -- Laminado en CY

        # --- Numero de bobinas por cama y camas por tarima ---
        self.numBobCama = ['NUMERO DE BOBINAS POR CAMA (PZ)']   # Impresión en BN
        self.cmsTarima = ['CAMAS POR TARIMA (PZ)']              # Impresión en BO

        # --- peso neto promedio por tarima --- 
        self.pesoNetoTam = ['PESO NETO PROMEDIO POR TARIMA (KG)']       # Impresión VERIFICARLO 
        self.pesoPromTamTol = ['TOLERANCIA']                            # Impresión VERIFICARLO
    
    def getAllAtr(this):
        return this.asesor,this.tipoEmpq,this.estruct,this.empaca

class atrImpresion:
    def __init__(self):
        self.matImpr = ['MATERIAL A IMPRIMIR']                      # AA                           
        self.dinaje = ['DINAJE']                                    # AC
        self.grosorCore = None                                      # Averiguar como sacar este atributo
        self.dsrrllImpr = ['DESARROLLO A IMPRIMIR mm (MANGA)']      # AL
        self.repEje = ['REPETICIONES AL EJE']                       # AM
        self.repDesrr = ['REPETICIONES AL DESARROLLO']              # AN    
        self.cantTinImpr = ['CANTIDAD DE TINTAS A IMPRIMIR']        # AO
        self.tipImpr = ['TIPO DE EMPRESION']                        # AD
        self.tipoTintasUtilizar = ['TIPO DE TINTAS A UTILIZAR']     # AR 
        self.tipoBarniz = ['TIPO DE BARNIZ']                        # BA 
        self.figEmbobImpr = ['sentido de embobinado(Figura de Embobinado)'] # BB
        self.maxEmpalmes = ['MÁXIMO DE EMPALMES POR BOBINA']        # BE
        self.tipoEmpaqBob = ['TIPO DE EMPAQUE PARA BOBINA']         # BF
        self.orientBobTarima = ['ORIENTACIÓN DE BOBINA EN TARIMA']  # BG
        self.pesarProduct = ['PESAR PRODUCTO POR']                  # BH            
        self.etiquetado = ['ETIQUETADO']                            # BM
        self.NumbobTarima = ['NUMERO DE BOBINAS POR CAMA']          # Refilado en DT
        self.validClr = ['VALIDACIÓN DE COLOR']                     # BC                  
        self.tarimaEmplaye = None                                   # Averiguar como sacar este atributo
        self.tarimaFlejada = None                                   # Averiguar como sacar este atributo

        # --- Calibre del material y Tolerancia ---
        self.calibre = ['CALIBRE Micras']                           # Se encuantra en "AE"
        self.calibreTol = ['TOLERANCIA']                            # Se encuentra en "AF"

        # --- Ancho de bobina a imprimir y tolerancia ---
        self.anchBob = ['ANCHO DE BOBINA (CM)']                     # AI
        self.anchBobTol = ['TOLERANCIA (CM)']                       # AJ

        # --- Ancho de core y tolerancia
        self.anchCore = ['ANCHO DE CORE (CM)']                      # "Laminado" en "CS"
        self.anchCoreTol = ['TOLERANCIA']                           # CT

        # --- Diametro de bobina y Tolerancia ---
        self.diamBob = ['DIÁMETRO DE BOBINA (CM)']                  # BI
        self.diamBobTol = ['TOLERANCIA CM']                         # BJ

        # --- Peso neto promedio de bobina ---
        self.pesoPromBob = ['PESO NETO PROMEDIO DE BOBINA (KG)']    # BK
        self.pesoPromBobTol = ['TOLERANCIA']                        # BL

        # --- Numero de bobinas por cama y camas por tarima ---
        self.numBobCama = ['NUMERO DE BOBINAS POR CAMA']            # BN
        self.camaTam = ['CAMAS POR TARIMA (PZ)']                    # B0

        # --- Peso neto por tarima ---
        self.pesoNto = ['PESO NETO PROMEDIO POR TARIMA (KG)']       # BP                 
        self.pesoNtoTol = ['TOLERANCIA']                            # BQ

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
            self.calPelTol = ['TOLERANCIA']                     # POSICIÓN "CK"
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
        self.proceso = ['PROCESO A REALIZAR']                   # CZ
        self.acabadoBob = None                                  # No se espesifica
        self.grosorCore = None                                  # No se espesifica
        self.figEmbobImpr = ['FIGURA DE EMBOBINADO']            # DE
        self.bobinaRefilar = ['LA BOBINA SE REFILARA/DOBLARA POR METROS, DIAMETRO O PESO']  # DF
        self.maximoEmpal = ['MÁXIMO DE EMPALMES POR BOBINA']    # DK 
        self.señalEmpl = None
        self.orientBobTarima = ['ORIENTACIÓN DE BOBINA EN TARIMA']  # DL
        self.tipoEmpaque = ['TIPO DE EMPAQUE PARA BOBINA']          # BM
        self.pesarPrdct = ['PESAR PRODUCTO POR']                    # DN
        self.etiquetado = ['ETIQUETADO']                            # DQ
        self.tarimaEmplaye = None
        self.tarimaFlejada = None
        # --- Ancho final de bobina al refilarse/Doblarse y Tolerancia ---
        self.anchoFinalBob = ['ANCHO FINAL DE BOBINA (CM)']         # DA
        self.anchoFinalBobTol = ['TOLERANCIA (CM)']                 # DB
        # --- Ancho de core y Tolerancia ---
        self.anchoCore = ['ANCHO DE CORE (LONGITUD DE BOBINA)']     # DC   
        self.anchoCoreTol = ['TOLERANCIA']                          # DD
        # --- Metros por bobina al refilarse/doblarse y tolerancia ---
        self.metrosBob = ['METROS POR BOBINA AL REFILARSE/DOBLARSE']    # DG
        self.metrosBobTol = ['TOLERANCIA MTS']                          # DH
        # --- Diametro de bobina al refilarse/doblarse y tolerancia ---
        self.diametroRef = ['DIAMETRO DE BOBINA AL REFILARSE/DOBLARSE (CM)']    # DI
        self.diametroRefTol = ['TOLERANCIA (CM)']                               # DJ
        # --- Peso neto promedio por bobina ---
        self.pesoNetPromBob = ['PESO NETO PROMEDIO DE BOBINA (KG)']             # DP
        self.pesoNetPromBobTol = ['TOLERANCIA']                                 # DQ
        # --- Numero de bobinas por cama y camas por tarima ---
        self.numBobCama = ['NUMERO DE BOBINAS POR CAMA (PZ)']                   # DR
        self.camasTam = ['CAMAS POR TARIMA']                                    # DT
        # --- Peso neto promedio por tarima --- 
        self.pesoNtoTam = ['PESO NETO PROMEDIO POR TARIMA']                     # DU
        self.pesoNtoTamTol = ['TOLERANCIA']                                     # DV

class atrConversion:
    def __init__(self):
        pass
    
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