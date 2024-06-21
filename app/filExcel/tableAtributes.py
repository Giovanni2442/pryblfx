class atributes():
    def __init__(self):
        self.codPrintCrd = None
        self.cliente = None
        self.fchaElav = None
        self.product = None
        self.fecha = None

    def atrFichTec(this,fila):
        this.codPrintCrd = fila['CODIGO PRINT CARD'],
        this.cliente = fila['CLIENTE'],
        this.fchaElav = fila['FECHA'],
        this.product = fila['PRODUCTO']
       # this.fecha = str(this.fecha.strftime('%d/%m/%y'))   #NOTA: Se tiene que hacer un cast a las fechas
        return this.codPrintCrd,this.cliente,this.fchaElav,this.product
    
pr = atributes()
#print(pr.atrFichTec()[0][0])
