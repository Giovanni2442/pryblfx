from flet import *
import mysql.connector
from src.conectDataBase.testConectDb import db
from src.app.filExcel.filtroExcel import filter
from src.Controllers.appFichVent import appFichVent
from src.Controllers.appExtr import appExtr
from src.Controllers.appImpr import appImpr
from src.Controllers.appLam import appLam
from src.Controllers.appRef import appRef
from src.Controllers.appConvrs import appConvrs

class appUpdate():
    def __init__(self):

        self.dataTbl = appFichVent()
        self.dtaExtr = appExtr()
        self.dtaImpr = appImpr()
        self.dtaLam = appLam()
        self.dtaRef = appRef()
        self.dtaConvrs = appConvrs()

        self.auxList = []
        self.connect = db()

        

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

        print(self.auxList[10:26],self.auxList[0])


        conectionPool = mysql.connector.pooling.MySQLConnectionPool(
            pool_name="poolUpdate",
            pool_size=5,
            **dbconfig
        )

        cnex = conectionPool.get_connection()
        cursor = cnex.cursor()

          # --- FICHA ---
        try:
            self.dataTbl.putFichaTec(*self.auxList[1:5], self.auxList[0])
            cnex.commit()  # Confirmar la transacción
        except Error as e:
            print(f"Error en putFichaTec: {e}")
            self.cnex.rollback()  # Deshacer la transacción en caso de error

        # --- VENTAS ---
        try:
            self.dataTbl.putVentas(*self.auxList[5:10], self.auxList[0])
            cnex.commit()  # Confirmar la transacción
        except Error as e:
            print(f"Error en putVentas: {e}")
            cnex.rollback()  # Deshacer la transacción en caso de error

        # --- EXTRUSION ---
        try:
            self.dtaExtr.transctInsertExtrs(self.auxList[0], *self.auxList[10:38])
            cnex.commit()  # Confirmar la transacción
        except Error as e:
            print(f"Error en transctInsertExtrs: {e}")
            cnex.rollback()  # Deshacer la transacción en caso de error

        try:
            self.dtaExtr.transctUpdateExtrs(*self.auxList[10:38], self.auxList[0])
            cnex.commit()  # Confirmar la transacción
        except Error as e:
            print(f"Error en transctUpdateExtrs: {e}")
            cnex.rollback()  # Deshacer la transacción en caso de error

        # --- IMPRESION ---
        try:
            self.dtaImpr.transctUpdateImprs(*self.auxList[38:73], self.auxList[0])
            cnex.commit()  # Confirmar la transacción
        except Error as e:
            print(f"Error en transctUpdateImprs: {e}")
            cnex.rollback()  # Deshacer la transacción en caso de error

    finally:
    # Devolver la conexión al pool en lugar de cerrarla
    if finally:
    # Devolver la conexión al pool en lugar de cerrarla
    if cnex.is_connected():
        cursor.close()
        connection.close()
        print("Conexión devuelta al pool.")

except Error as e:
    print(f"Error al crear el pool de conexiones: {e}").is_connected():
        cursor.close()
        connection.close()
        print("Conexión devuelta al pool.")

    except Error as e:
        print(f"Error al crear el pool de conexiones: {e}")