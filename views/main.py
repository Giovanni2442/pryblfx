from tkinter import *
from tkinter import ttk
from ttkthemes import ThemedStyle

class appMain:
    raiz = Tk()
    raiz.title("ventana de pruebas")
    raiz.mainloop()



def main():
    root = tk.Tk()
    root.title("Ejemplo de TTKThemes")

    # Crear un estilo temático
    style = ThemedStyle(root)
    style.set_theme("plastik")  # Elegir un tema, por ejemplo "plastik"

    # Crear un botón con el estilo del tema elegido
    button = ttk.Button(root, text="Botón Temático")
    button.pack(padx=20, pady=20)

    root.mainloop()

if __name__ == "__main__":
    re = appMain()
    re()
