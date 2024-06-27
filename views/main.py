from tkinter import *
from tkinter import Misc, ttk
#from ttkthemes import ThemedStyle # type: ignore
from VentanaMain.vtnMain import *

class appMain:
    root = Tk()     # raiz : Objeto de tipo Frame de la clase Tk()
    root.wm_title("ventana de pruebas")
    app = vtnMain(root)     # Pasando el frame a la clase ventana, que en este caso es la instancia root
    app.mainloop()


if __name__ == "__main__":
    re = appMain()
    re()
