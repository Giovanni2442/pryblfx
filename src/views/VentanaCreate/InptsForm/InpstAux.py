from src.Controllers.appFichVent import appFichVent
from src.Controllers.appExtr import appExtr
from src.Controllers.appImpr import appImpr
from src.Controllers.appLam import appLam
from src.Controllers.appRef import appRef
from src.Controllers.appConvrs import appConvrs
from src.conectDataBase.testConectDb import db

class InptsAux():
    def __init__(self):

        self.dtaFichVent = appFichVent()
        self.dtaExtr = appExtr()
        self.dtaImpr = appImpr()
        self.dtaLam = appLam()
        self.dtaRef = appRef()
        self.dtaConvrs = appConvrs()

    # CAMBIA EL VALOR DEL LABEL EN EL BTN
    def changeBtn(self,id):
        if id == "Insert":
            return "Ingresar"
        else:
            return "Update"
        
    # RETORNA EL VALOR DE LA TUPLA :
    # id : DEVUELVE EL ESTADO SI ES INSERT O UPDATE
    # default_value : Valor por defecto de la entrada de Texto
    # value : Indice de la tupla que se trae de la BD
    # NOTA : MEJORAR ESTA FUNCIÓN PARA QUE SEA GENERICA, UTILIZA UN DICCIÓNARIO
    def pruUpdate(self,id,default_value,value):
        if id != "Insert":
            #return  self.appFicha.get_row_Id(id)
            return self.appFicha.getFicha(id)[0][value]
        else:
            return default_value
            #return None

    def getData(self,id,tabla,Indice,default_value):
        if id != "Insert":           
            dic =  {                  
                'FICHA':self.dtaFichVent.getFicha(id)[0],
                'VENTAS':self.dtaFichVent.get_Ventas(id)[0],
                'EXTRS': self.dtaExtr.getExtr(id)[0],
            }

            #cursor = self.connect.cursor()
            #cursor.close()
            #self.connect.close()
            return dic[tabla][Indice]

        else:
            return default_value
            #return None

    def getData2(self,id,default_value):
        if id != "Insert":           
            dic =  {                  
                'FICHA':self.dtaFichVent.getFicha(id)[0],
                'VENTAS':self.dtaFichVent.get_Ventas(id)[0],
                'EXTRS': self.dtaExtr.getExtr(id)[0],
            }

            return dic
            #return dic[tabla][Indice]

        else:
            return default_value

