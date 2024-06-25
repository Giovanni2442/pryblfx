import tkinter as tk

#ventana para inicio de seción 
ventana = tk.Tk()

ventana.title("BIOFLEX")


# Obtener las dimensiones de la pantalla
ancho_pantalla = ventana.winfo_screenwidth() #método para obtener Ancho
alto_pantalla = ventana.winfo_screenheight() #método para obtener Alto

# Calcular las coordenadas para centrar la ventana
ancho_ventana = 900
alto_ventana = 750
posicion_x = (ancho_pantalla - ancho_ventana) // 2 
posicion_y = (alto_pantalla - alto_ventana) // 2

#Fondode de la ventana
ventana.configure(bg="red")

# Establecer el tamaño y la posición de la ventana
ventana.geometry(f"{ancho_ventana}x{alto_ventana}+{posicion_x}+{posicion_y}")

#Colocacion de nombre BIOFLEX
etiqueta = tk.Label(ventana, text="BIOFLEX", fg="red", bg="white", font=("Lexend", 35), width=31, height=4, anchor="center")
etiqueta.pack(pady=20)  # Ajusta el valor de `pady` según sea necesario
etiqueta = tk.Label(ventana, text = "INGRESA USUARIO", fg="black", bg="white", font=("Arial", 20))
etiqueta.pack()




ventana.mainloop()
