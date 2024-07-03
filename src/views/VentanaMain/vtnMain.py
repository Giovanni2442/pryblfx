import flet as ft

class ejmpl(ft.UserControl):
    def __init__(self):
        super().__init__()

    def build(self):
        title = "AlertDialog examples"
        horizontal_alignment = ft.CrossAxisAlignment.CENTER

        self.dlg = ft.AlertDialog(
            title=ft.Text("Hi, this is a non-modal dialog!"),
            on_dismiss=lambda e: self.page.add(ft.Text("Non-modal dialog dismissed")),
        )

        self.dlg_modal = ft.AlertDialog(
            modal=True,
            title=ft.Text("Please confirm"),
            content=ft.Text("Do you really want to delete all those files?"),
            actions=[
                ft.TextButton("Yes", on_click=self.handle_close),
                ft.TextButton("No", on_click=self.handle_close),
            ],
            actions_alignment=ft.MainAxisAlignment.END,
            on_dismiss=lambda e: self.page.add(
                ft.Text("Modal dialog dismissed"),
            ),
        )

        # Botones que abren el modal
        self.cntIni = ft.Container(
            content=ft.Column(
                controls=[
                    ft.ElevatedButton("Open dialog", on_click=self.open_non_modal_dialog),
                    ft.ElevatedButton("Open modal dialog", on_click=self.open_modal_dialog),
                ]
            ),
            alignment=ft.alignment.center
        )

        self.ejemplo = ft.Container(
            border_radius=10,
            width=100,
            height=100,
            shadow=ft.BoxShadow(
                spread_radius=0,
                blur_radius=50,
                color=ft.colors.AMBER_700,
                offset=ft.Offset(50, 110),
                blur_style=ft.ShadowBlurStyle.OUTER,
            )
        )

        # Frame Principal
        self.frameMain = ft.Container(
            content=ft.Column(
                controls=[
                    self.cntIni,
                    self.ejemplo
                ]
            )
        )

        return self.frameMain
    def pruebas(self):
        self.pr = "Messasge!"

    def open_non_modal_dialog(self, e):
        self.page.overlay.append(self.dlg)
        self.dlg.open = True
        self.page.update()

    def open_modal_dialog(self, e):
        self.page.overlay.append(self.dlg_modal)
        self.dlg_modal.open = True
        self.page.update()

    def handle_close(self, e):
        self.dlg_modal.open = False
        self.page.update()
        self.page.add(ft.Text(f"Modal dialog closed with action: {e.control.text}"))

def main(page: ft.Page):
    page.padding = 5
    page.add(ejmpl())

ft.app(target=main)

