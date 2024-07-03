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

        self.cntIni = ft.Container(
            content=ft.Column(
                controls=[
                    ft.ElevatedButton("Open dialog", on_click=self.open_non_modal_dialog),
                    ft.ElevatedButton("Open modal dialog", on_click=self.open_modal_dialog),
                ]
            ),
            alignment=ft.alignment.center
        )

        self.frameMain = ft.Container(
            content=ft.Column(
                controls=[
                    self.cntIni
                ]
            )
        )

        return self.frameMain

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

