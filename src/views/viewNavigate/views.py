from flet import *
from src.views.VentanaMain.crudPrintCard import crudPrintCard
from src.views.VentanaCreate.createPrindCard import createPrind
from src.views.VentanaMain.vtnMain import pr
from src.views.VentanaCreate.createFicha.createPdf import CreatePdf

# retorna mi conjunto de rutas para el manejo de vistas 
def pru(page,id):
    return View(
            route='/cratePrindCard',
            controls=[
                createPrind(page,id)
            ]
    )


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
                createPrind(page)
            ]
        ),
        '/prueba':pru,
    }


    