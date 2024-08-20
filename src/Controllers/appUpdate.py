from flet import *
from src.conectDataBase.testConectDb import db
from src.Controllers.appFichVent import appFichVent

class appUpdate():
    def __init__(self):
        self.dataTbl = appFichVent()
        self.auxList = []

        # RECOLECTOR DE DATOS PARA CADA ENTRADA
    def qryUpdate(self,tpl):                     # Recorre las listas de Inputs para colocarlas en una lista
        #vle = tpl[2][0].items[0].content.controls[1].value
        for indx,i in enumerate(tpl):       # Recorre las listas de Inputs
            for j in i:                     # Recorre los valores de cada lista
                if isinstance(j, list):     # Verifica si el valor de la lista hay listas, para colocar los valores en la lista padre
                    for f in j:             # Recorre la sub lista desde el indice
                        if isinstance( f, PopupMenuButton):
                            for m in f.items:
                                txtFld = m.content.controls[1]
                                #print("--- **** ", txtFld.label)
                                self.auxList.append(txtFld.value)
                        else:
                            #print(f" --xx {f.label}")
                            self.auxList.append(f.value)
                        #print("-->" ,f) 
                    continue
                if isinstance(j, PopupMenuButton):
                    for k in j.items:
                        txtFld = k.content.controls[1]
                        #print("--- **** ", txtFld.label)
                        self.auxList.append(txtFld.value)
                else:
                    #print(f" --xx {inx}  : {j.label} : {j.value}")
                    self.auxList.append(j.value)

        print(self.auxList[:5])

        self.dataTbl.putFichaTec()
