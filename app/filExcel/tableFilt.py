# --- SE FILTRAN LAS TABLAS POR EXPRECIÓNES REGULARES ---
#from filtroExcel import filter
from filExcel.filtroExcel import filter

class tableFilt():
    errArr = ""                 # tupla de errores que retorna la función
    elmnts = ""                 # tupla de valores que retorna la función
    msg = ""
    #Replazar if en esta fucnión
    # *func     : El numero de "n" funciónes
    # clmn      : Columna del archivo excel
    # msg       : mensaje de error
    # elmnts    : tupla de elementos extraidos del excel
    def condiFilts(*func,cln,c,msg,elmnts):
        #filNan = (c-cln)+1         #Formula para calcular la posisión de la fila
        filNan = (c)+1
        #print(filNan)
        if not all(func):       #Busca el las tuplas si existe un false
            for i,j in enumerate(func):  #En el ciclo busca el indice el false para obtener el mensaje de error 
                if j !=True: 
                    inx = i
                    break
            errArr = False,filNan,msg[inx] 
            return errArr
        else:
            return elmnts
             
    #Color Amarillo     
    def tblFichTec(fila,clmn,cl):
        # --- Atributos de la Tabla ---
        codPrintCrd = fila[8] 
        cliente = fila[6]
        fchaElav = fila[2]
        product = fila[7]   
        # ------------------------- 
        
        fecha = str(fchaElav.strftime('%d/%m/%y'))   #NOTA: Se tiene que hacer un cast a las fechas
        atributos = codPrintCrd,cliente,fecha,product 

        mensajes = "campo vacio!","El codigo es Incorrecto!","La fecha es Incorrecta!"
        return tableFilt.condiFilts(
            filter.vrfNan(codPrintCrd,cliente,fchaElav,product),
            filter.vrfPrintCard(codPrintCrd,cliente),
            filter.vrfFechas(fecha),
            cln=clmn,
            c=cl,
            msg=mensajes,
            elmnts=atributos
        )
            
    # Color : Azul
    def tblVentas(fila,clmn,c):
        # --- Atributos de la Tabla ---
        asesor = fila[9] 
        tipo_Empaque = fila[10]
        product_Laminado = fila[2]  #No esta en las tablas de captura, averiguar como Aplica o N/A
        estruct_Product = fila[11]
        empaca = fila[12]
        # ------------------------- 
        filNan = (c-clmn)+1         #Formula para calcular la posisión de la fila

        if filter.vrfNan(asesor,tipo_Empaque,estruct_Product,empaca):
            msg = "campo vacio!"
            errArr = False,filNan,msg           #tupla de elementos
            #print(f'{errArr[0]}  :  {errArr[1]}') 
            return errArr
        elif filter.vrfIsletter(asesor,tipo_Empaque,empaca) != True:
            msg = "No es una cadena!"
            errArr = False,filNan,msg           #tupla de elementos
            return errArr
        elif filter.vrfEstrcProd(estruct_Product) != True:
            msg = "Error en la estructura!"
            errArr = False,filNan,msg           #tupla de elementos
            return errArr
        else:
            errArr = asesor,tipo_Empaque,estruct_Product,empaca       #tupla de elementos si todo es correcto
            return errArr

# ---- FUNCIONES DE PRUEBAS ---- 
    def pr1():

        tupla1 = True,True,True
        tupla2 = True,False,True
        tupla3 = True,True,True

        mensajes = "1","2","3"

        tableFilt.pru(
            tupla1,
            tupla2,
            tupla3,
            msg=mensajes
        )
    def pru(*func,cln,c,msg,elmnts):
        filNan = (c-cln)+1         #Formula para calcular la posisión de la fila
        
        if not all(func):       #Busca el las tuplas si existe un false
            for i,j in enumerate(func):  #En el ciclo busca el indice el false para obtener el mensaje de error 
                if j !=True: 
                    inx = i
                    break
            errArr = False,filNan,msg[inx] 
            return errArr
        else:
            return elmnts
        
        #return func
            #if not encontrado:
            #    print("No se encontró ningún False en la tupla.")
#-----------------------------------------

clase = tableFilt
#clase.pr1()
