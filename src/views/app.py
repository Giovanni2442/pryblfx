from flet import *
from src.views.viewNavigate.views import getViews

from flet import *
from src.views.viewNavigate.views import getViews

#  --- Comienza desde el main --- 
def main(page: Page):
    def route_change(route):    # Función para el cambio de pestañas
        print(page.route)       # Imprime la ruta donde se va a acceder
        page.views.clear()      # Limpia la pagina actual 
        page.views.append(      # Agrega en Pagina la Ruta de la pagina
            getViews(page)[page.route]
        )
        page.update()  # Necesario para actualizar la página

    page.on_route_change = route_change  # Cambiado a on_route_change
    page.go('/')  # Inicia la navegación a la página raíz

    page.window_min_height = 102
    page.window_min_width = 102
    page.theme_mode = ThemeMode.DARK
    page.padding = 5

app(target=main)

