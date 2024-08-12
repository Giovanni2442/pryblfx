import flet as ft

def main(page: ft.Page):
    def on_file_picked(e: ft.FilePickerResultEvent):
        if e.files:
            for file in e.files:
                page.add(ft.Text(f"Archivo seleccionado: {file.name}"))
                # Aquí puedes manejar el archivo, por ejemplo, subirlo a un servidor

    file_picker = ft.FilePicker(on_result=on_file_picked)

    page.overlay.append(file_picker)

    page.add(
        ft.Text("Subir archivo usando Flet"),
        ft.ElevatedButton(
            "Seleccionar archivo",
            on_click=lambda _: file_picker.pick_files(allow_multiple=True),
        ),
    )

ft.app(target=main)
