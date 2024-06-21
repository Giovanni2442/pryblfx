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