import time
import threading

from flet import * 
from src.views.VentanaCreate.Mdls import Mdls

class pru3(UserControl):
    def __init__(self,page):
        super().__init__(expand=True)

        self.page = page

        # ABRIR Y CERRAR MODAL
        self.mdl = Mdls(page)

        self.BtnCreate = FilledButton(
            text="CLICK ME!",
            adaptive=True,
            style=ButtonStyle(
                bgcolor=colors.BLACK,
                color={
                    ControlState.DEFAULT: colors.WHITE,
                    ControlState.HOVERED: colors.WHITE,
                }, 
                overlay_color="#405d44",
                elevation={"pressed": 0, "": 1},
                animation_duration=200,
                shape={
                    ControlState.HOVERED: RoundedRectangleBorder(radius=15),
                    ControlState.DEFAULT: RoundedRectangleBorder(radius=3),
                },
            ),
            on_click= lambda e: self.pruProgress 
             
            #                
            #on_click= self.inptTable.jer
        )

        self.frameMain = Container(
            bgcolor=colors.WHITE,
            border_radius=10,
            content=Column(
                controls=[
                    self.BtnCreate
                ]
            )
        )

        # Contenerdor para hacer resposiva la app
        self.container = ResponsiveRow(
            controls=[
                self.frameMain
            ]
        )

    def pruProgress(self,e):
        self.mdlDlt = AlertDialog(
            modal=True,
            
            content= Column([
                Text("CARGANDO ELEMENTOS..."),
                ProgressRing()
                ],
                height=20,
                width=10,
                horizontal_alignment=CrossAxisAlignment.CENTER,
            ),
            actions=[
                #TextButton("Eliminar",on_click= lambda _: self.btnSlct(bnd=True,id=idPrind)),   # lambda _ : "_" el guión sirve para tomar ignorar los parametros, ya que no se usan en la función  
                #TextButton("CERRAR", on_click= lambda e: self.mdl.close_dialog(self.mdlDlt))
            ],
            actions_alignment= MainAxisAlignment.END
        )
        self.page.overlay.append(self.mdlDlt)
        self.mdlDlt.open = True
        self.page.update()

        # Ejecutar el proceso en un hilo separado
        threading.Thread(target=self.simulate_long_process).start()

    def simulate_long_process(self):
        # Redirigir a la página deseada
        #self.page.go('/cratePrindCard')
        time.sleep(3)
        # Cerrar el diálogo al finalizar el proceso
        self.mdlDlt.open = False
        self.page.update()

    def build(self):
        return self.container

def main(page: Page):
    page.window_min_height = 200
    page.window_min_width = 200

    #page.theme_mode = ThemeMode.DARK
    page.padding = 0
    #page.adaptive = True
    page.add(pru3(page))

app(main)