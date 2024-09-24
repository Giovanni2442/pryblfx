import time
import threading

from flet import * 
from src.views.VentanaCreate.Mdls import Mdls

class MdlProgress(UserControl):
    def __init__(self, page):
        super().__init__(expand=True)
        self.page = page

    def pruProgress(self,*fun):
        self.mdlpRUE = AlertDialog(
            modal=True,
            content=Column(
                [
                    Text("CARGANDO ELEMENTOS..."),
                    ProgressRing()
                ],
                height=20,
                width=10,
                horizontal_alignment=CrossAxisAlignment.CENTER,
            ),
            actions_alignment=MainAxisAlignment.END
        )
        self.page.overlay.append(self.mdlpRUE)
        self.mdlpRUE.open = True
        self.page.update()

        # Ejecutar el proceso en un hilo separado
        threading.Thread(target=lambda : self.simulate_long_process(fun)).start()


    def simulate_long_process(self, fun):
        #EJECUTA MULTIPLES FUNCIÓNES
        #time.sleep(0.5)
        for funcs in fun:
            funcs()  # Ejecuta cada función

        # Cerrar el diálogo al finalizar el proceso
        self.mdlpRUE.open = False
        self.page.update()
