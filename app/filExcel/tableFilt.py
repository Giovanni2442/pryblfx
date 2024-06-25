# --- SE FILTRAN LAS TABLAS POR EXPRECIÓNES REGULARES ---
#from filtroExcel import filter
from filExcel.filtroExcel import filter
from filExcel.tableAtributes import *      #Acceder a los tributos de cada Tabla

class tableFilt():
    errArr = ""                 # tupla de errores que retorna la función
    elmnts = ""                 # tupla de valores que retorna la función
    msg = ""                    # tupla de mensajes de error
    atr = ""                    # Instancia a la clase de Atributos

    #Replazar if en esta fucnión
    # *func     : El numero de "n" funciónes
    # clmn      : Columna del archivo excel
    # msg       : mensaje de error
    # elmnts    : tupla de elementos extraidos del excel
    def condiFilts(*func,c,msg,elmnts):
        filNan = (c)+3 # NOTA : El indice se suma a +3 ya que empieza en 0 desde la fila de datos 
        
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
    def tblFichTec(fila,cl):
        atr = atrFichTec(fila)
        #NOTA: Se tiene que hacer un cast a las fechas
        return tableFilt.condiFilts(
            #NOTA : Importa el orden de los filtros con los mensajes, arreglar eso
            filter.vrfNan(atr.codPrintCrd,atr.cliente,atr.fecha,atr.product),
            filter.vrfPrintCard(atr.codPrintCrd),
            filter.vrfFechas(atr.fecha),
            filter.vrfCliente(atr.cliente),
            c=cl,
            msg=atr.mensajes,
            elmnts=atr.getAllAtr()
        )
            
    # Color : Azul
    def tblVentas(fila,cl):
        atr = atrVentas(fila)
        
        return tableFilt.condiFilts(
            filter.vrfNan(atr.asesor,atr.tipoEmpq,atr.estruct,atr.empaca),
            filter.vrfIsletter(atr.asesor,atr.tipoEmpq,atr.empaca),# atr.empaca, atr.tipoEmpq
            filter.prEsctr(atr.estruct),
            c=cl,
            msg=atr.mensajes,
            elmnts=atr.getAllAtr()
        )
    
    def tblExtruccion(fila,cl):
        print(filter.vrfIsletter("Hoala Mundo 45"))
       

# ---- FUNCIONES DE PRUEBAS ---- 
    def pr1():
        je = atrLaminado.je()
        print(je.prueba)
    
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
clase.pr1()

