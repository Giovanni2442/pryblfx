# Esta clase sirve como un Modulo Auxiliar para abrir y cerrar Modales
class Mdls():
    def __init__(self,page):
        self.page = page
    
        # Función para abrir el diálogo
    def open_dialog(self,dialog):
        self.page.overlay.append(dialog)
        dialog.open = True
        self.page.update()
    # Función para cerrar el diálogo
    def close_dialog(self,dialog):
        dialog.open = False
        self.page.update()
        