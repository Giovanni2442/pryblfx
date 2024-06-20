class atributes():
    def __init__(self):
        self.codPrintCrd = ['CODIGO PRINT CARD']
        self.cliente = ['CLIENTE']
        self.fchaElav = ['FECHA']
        self.product = ['PRODUCTO']


    def atrFichTec(fila):
        codPrintCrd = fila['CODIGO PRINT CARD'] 
        cliente = fila['CLIENTE']
        fchaElav = fila['FECHA']
        product = fila['PRODUCTO']

        fecha = str(fchaElav.strftime('%d/%m/%y'))   #NOTA: Se tiene que hacer un cast a las fechas

        return codPrintCrd,cliente,fecha,fchaElav,product
    
pru = atributes()
print(pru.cliente)
