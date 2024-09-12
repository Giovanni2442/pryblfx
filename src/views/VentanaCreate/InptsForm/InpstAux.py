#'''

from src.Controllers.appFichVent import appFichVent
from src.Controllers.appExtr import appExtr
from src.Controllers.appImpr import appImpr
from src.Controllers.appLam import appLam
from src.Controllers.appRef import appRef
from src.Controllers.appConvrs import appConvrs 
#'''
class InptsAux():
    def __init__(self):

        #'''
        self.dtaFichVent = appFichVent
        self.dtaExtr = appExtr
        self.dtaImpr = appImpr
        self.dtaLam = appLam
        self.dtaRef = appRef
        self.dtaConvrs = appConvrs #'''
        #pass

    # CAMBIA EL VALOR DEL LABEL EN EL BTN
    def changeBtn(self,id):
        print("--,",id)
        if id == "Insert":
            return "Ingresar"
        elif id == "UpdateMsv":
            return "Update Masivo"
        else:
            return "Update"
        
    # RETORNA EL VALOR DE LA TUPLA :
    # id : DEVUELVE EL ESTADO SI ES INSERT O UPDATE
    # default_value : Valor por defecto de la entrada de Texto
    # value : Indice de la tupla que se trae de la BD
    # NOTA : MEJORAR ESTA FUNCIÓN PARA QUE SEA GENERICA, UTILIZA UN DICCIÓNARIO
    def pruUpdate(self,id,default_value,value):
        #pass
        '''
        if id != "Insert":
            #return  self.appFicha.get_row_Id(id)
            return self.appFicha.getFicha(id)[0][value]
        else:
            return default_value
            #return None'''

    #def getData(self,id,tabla,Indice,default_value):
    def getData(self,id,tabla):
        #pass
        #'''
        if id != "Insert":           
            dic =  {                  
                'FICHA':self.dtaFichVent().getFicha(id),
                'VENTAS':self.dtaFichVent().get_Ventas(id),
                'EXTRS': self.dtaExtr().transactGetExtrs(id),
                'IMPR' : self.dtaImpr().transGetImprs(id)
            }

            return "SI"
            #return dic[tabla][Indice]
        else:
            return None
            #return None'''

    def getData2(self,id):
        if id != "Insert":           
           
            #return "SI"
            return self.dtaExtr().transactGetExtrs(id)
        else:
            return None

