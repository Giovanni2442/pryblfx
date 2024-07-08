from flet import *
from src.views.VentanaMain.vtnMain import ejemplo
from src.views.VentanaMain.eje2 import ejemplo2
#from src.views.VentanaMain.pruebasFlet import UI

# retorna mi conjunto de rutas para el manejo de vistas 
def getViews(page):
    return {
        '/':View(
            route='/',  # Se define la ruta principal el Login
            controls=[
                ejemplo(page)
            ]
        ),
        '/frame2':View(
            route='/frame2',
            controls=[
                ejemplo2(page)
            ]
        )
    }

    