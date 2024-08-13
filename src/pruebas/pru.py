from flet import * 

class FileUploaderApp:
    def __init__(self, page: Page):
        self.page = page
        self.file_picker = FilePicker(on_result=self.on_file_picked)
        self.page.overlay.append(self.file_picker)

        # Diccionario para almacenar las rutas de los archivos con el identificador del botón
        self.tplImg = {}

        # Variable Temporal
        self.current_button_id = None

    def on_file_picked(self, e: FilePickerResultEvent):  # Agrega un parámetro para el ID del botón
        if e.files:
            for file in e.files:
                # Almacena el nombre del archivo y su ruta en el diccionario
                #self.tplImg[button_id] = {'name': file.name, 'path': file.path}
                print(self.current_button_id,file.path)

    def select_file(self, e, button_id):
        
        self.current_button_id = button_id
        
        # Pasa el ID del botón a la función que maneja el resultado del picker
        self.file_picker.pick_files(allow_multiple=False)


    def build(self):
        return Column(
            [
                Text("Subir archivo usando Flet"),
                ElevatedButton(
                    "Seleccionar archivo",
                    on_click=lambda e: self.select_file(e,"HOLA XD"),
                ),
            ]
        )

def main(page: Page):
    app = FileUploaderApp(page)
    page.add(app.build())

# Ejemplo de uso
app(target=main)
