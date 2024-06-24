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

        # --- 
    
    def getAllAtr(this):
        return this.asesor,this.tipoEmpq,this.estruct,this.empaca



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