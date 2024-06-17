# --- SE FILTRAN LAS TABLAS POR EXPRECIÓNES REGULARES ---
from filExcel.filtroExcel import filter
from datetime import datetime


class tableFilt():

    errArr = ""                 # tupla de retorno a la función
    msg = ""

    #Replazar if en esta fucnión
    def collectFilter(self,*any):
        cnt = 0
        cnt = len(any)
        dir = {}

        ''' for i,j in enumerate(any):
            dir[i] = lambd
            i +=1
            print(i,j)'''
        

    def tblFichTec(fila,clmn,c):
        # --- Atributos de la Tabla ---
        codPrintCrd = fila[8] 
        cliente = fila[6]
        fchaElav = fila[2]
        product = fila[7]   
        # ------------------------- 

        filNan = (c-clmn)+1         #Formula para calcular la posisión de la fila
        fecha = str(fchaElav.strftime('%d/%m/%y'))   #NOTA: Se tiene que hacer un cast a las fechas
        #print(fh)
        #print("--",filter.fechas(fecha))

        if filter.vrfNan(codPrintCrd,cliente,fchaElav,product):
            msg = "campo vacio!"
            errArr = False,filNan,msg           #tupla de elementos
            #print(f'{errArr[0]}  :  {errArr[1]}') 
            return errArr
        elif filter.vrfPrintCard(codPrintCrd,cliente) != True:
            msg = "El codigo es Incorrecto!"
            errArr = False,filNan,msg           #tupla de elementos
            return errArr
        elif filter.vrfFechas(fecha) != True:
            msg = "La fecha es Incorrecta!"
            errArr = False,filNan,msg
            return errArr
        else:
            errArr = codPrintCrd,cliente,fecha,product        #tupla de elementos si todo es correcto
            return errArr
        
    def tblVentas(fila,clmn,c):
        # --- Atributos de la Tabla ---
        asesor = fila[11] 
        tipo_Empaque = fila[12]
        product_Laminado = fila[2]  #No esta en las tablas de captura, averiguar como Aplica o N/A
        estruct_Product = fila[13]
        empaca = fila[14]
        # ------------------------- 
        filNan = (c-clmn)+1         #Formula para calcular la posisión de la fila

        if filter.vrfNan(asesor):
            msg = "campo vacio!"
            errArr = False,filNan,msg           #tupla de elementos
            #print(f'{errArr[0]}  :  {errArr[1]}') 
            return errArr
        elif filter.vrfIsletter(asesor) != True:
            msg = "El campo no es una cadena!"
            errArr = False,filNan,msg           #tupla de elementos
            return errArr
            
    def test():
        #cadena = "LDPE NAT 125 +/- 10% / LDPE NAT 125 +/- 10%"
        #print(filter.vrfEstrcProd(cadena))
        pass

    def saludo():
        print("Hola")

#clase = tableFilt()
#clase.saludo()


#clase.collectFilter("Hola","l","l")
