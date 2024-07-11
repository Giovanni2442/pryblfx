from flet import *
from src.views.VentanaMain.pruebasFlet import crudPrintCard

# retorna mi conjunto de rutas para el manejo de vistas 
def getViews(page):
    return {
        # CRUD de Productos
        '/':View(
            route='/',  # Se define la ruta principal el Login
            controls=[
                crudPrintCard(page)
            ],
        ),
        '/cratePrindCard':View(
            route='/cratePrindCard',
            controls=[
                #UI(page)
            ]
        ),
    }

    