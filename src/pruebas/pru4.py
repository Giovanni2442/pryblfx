import threading
import flet as ft
import time

class MyApp:
    def __init__(self, page: ft.Page):
        self.page = page
        self.mdlDlt = None

    def pruProgress(self, e):
        # Crear el AlertDialog
        self.mdlDlt = ft.AlertDialog(
            modal=True,
            content=ft.Column(
                [
                    ft.Text("CARGANDO ELEMENTOS..."),
                    ft.ProgressRing()
                ],
                height=20,
                width=10,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            actions_alignment=ft.MainAxisAlignment.END
        )
        
        # Mostrar el diálogo
        self.page.overlay.append(self.mdlDlt)
        self.mdlDlt.open = True
        self.page.update()

        # Ejecutar el proceso en un hilo separado para no bloquear la UI
        threading.Thread(target=self.simulate_long_process).start()

    def simulate_long_process(self):
        # Simular un proceso largo si fuera necesario (descomentar si lo necesitas)
        time.sleep(2)  # Simula un retraso si quieres

        # Redirigir a la página deseada
        #self.page.go('/cratePrindCard')
        #print("Pamch0")

        # Cerrar el diálogo al finalizar el proceso
        self.mdlDlt.open = False
        self.page.update()

def main(page: ft.Page):
    app = MyApp(page)
    
    # Crear el botón y agregarlo a la página
    btn = ft.FilledButton(
        text="CLICK ME!",
        adaptive=True,
        style=ft.ButtonStyle(
            bgcolor=ft.colors.BLACK,
            color={ft.ControlState.DEFAULT: ft.colors.WHITE, ft.ControlState.HOVERED: ft.colors.WHITE},
            overlay_color="#405d44",
            elevation={"pressed": 0, "": 1},
            animation_duration=200,
            shape={
                ft.ControlState.HOVERED: ft.RoundedRectangleBorder(radius=15),
                ft.ControlState.DEFAULT: ft.RoundedRectangleBorder(radius=3),
            },
        ),
        on_click=app.pruProgress  # Llamar a la función pruProgress cuando se haga clic
    )
    
    # Agregar el botón a la página
    page.add(btn)

ft.app(target=main)
