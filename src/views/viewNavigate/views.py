from flet import *
from src.views.VentanaMain.crudPrintCard import crudPrintCard
from src.views.VentanaCreate.createPrindCard import createPrind
from src.views.VentanaCreate.WindowPru import windowPru
from src.views.VentanaMain.crudMsvUptd import crudMsv


def getViews(page):
    id = page.client_storage.get("id") or "id"
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

         '/editMsv': View(
            route='/crudMsvUptd',
            controls=[
                crudMsv(page)
            ]
        ),

        '/prueba': View(
            route='/windowPru',
            controls=[
                windowPru(page)
            ]
        )
    }


    