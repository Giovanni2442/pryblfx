from tkinter import *
from tkinter import Misc, ttk

# Clase vtnMain que hereda de un Frama()
class vtnMain(Frame):
    def __init__(self, master=None):
        super().__init__(master,width=900, height=700)
        self.master = master
        self.pack()
        self.widgetsMain()

    def widgetsMain(self):
        # --- Frame de busqueda y filtrados ---
        frameFilter = Frame(self,bg="#768E90")
        frameFilter.place(x=5,y=5,width=670,height=200)

        # --- Frame para las tablas ---
        frameTable = Frame(self,bg="#17C497")
        frameTable.place(x=5,y=210,width=670,height=285)

        # --- Labels ---
        lblIndex = Label(frameFilter,text="Busqueda de Fichas!",font=("Arial",15))
        lblIndex.place(x=260,y=7)

        lblFiltr = Label(frameFilter,text="FILTRAR BUSQUEDA : ",font=("Calibri",10))
        lblFiltr.place(x=470,y=70)
        
        # --- Inputs ---
        self.InptName=Entry(frameTable)
        self.InptName.place(x=3,y=75,width=120, height=20)  

        self.InptFltrPrintCard=Entry(frameFilter)
        self.InptFltrPrintCard.place(x=470,y=100,width=120, height=20) 

                # Crear un estilo para ttk.Entry
        style = ttk.Style()
        style.configure("TEntry",
                        fieldbackground="red",  # Color de fondo del campo
                        background="red",  # Color del borde
                        borderwidth=5,  # Ancho del borde
                        relief="solid")  # Estilo del borde (solid, groove, ridge, etc.)

        # Crear un ttk.Entry con el estilo personalizado
        self.InptFltrPrintCard = ttk.Entry(frameFilter, style="TEntry")
        self.InptFltrPrintCard.place(x=470, y=140, width=120, height=20)
        