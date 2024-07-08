from flet import *
from src.views.viewNavigate.views import getViews

from flet import *
from src.views.viewNavigate.views import getViews

# Comienza desde el main
def main(page: Page):
    def route_change(route):
        print(page.route)  # Prueba para ver la ruta de acceso
        page.views.clear()
        page.views.append(
            getViews(page)[page.route]
        )
        page.update()  # Necesario para actualizar la página

    page.on_route_change = route_change  # Cambiado a on_route_change
    page.go('/')  # Inicia la navegación a la página raíz

app(target=main)

