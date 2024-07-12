from flet import *
from src.app.filExcel.filtroExcel import filter

class InptsTable(UserControl):
    def __init__(self):
        super().__init__()

        self.filter = filter().vrfPrintCard

    ### INPUTS DE TABLA FichaTecnica ###
        self.id_product = TextField(
            label="Ingresar el PrindCard",
            border= InputBorder.OUTLINE,
            border_color="Black",
            label_style=TextStyle(color="Black",italic=True),
            on_change= self.verInpts,
        )

        self.cliente = TextField(
            label="Ingresar el Cliente",
            border= InputBorder.OUTLINE,
            border_color="Black",
            label_style=TextStyle(color="Black",italic=True),
            #on_change= lambda e: self.shwAllInpts(e.control.label)
        )

        self.fecha_Elav = TextField(
            label="dd/MM/YYYY",
            border= InputBorder.OUTLINE,
            border_color="Black",
            label_style=TextStyle(color="Black",italic=True),
        )

        self.fecha_Rev = TextField(
            label="dd/MM/YYYY",
            #label_style=,
            border= InputBorder.OUTLINE,
            border_color="Black",
            label_style=TextStyle(color="Black",italic=True),
        )

        self.producto = TextField(
            label="Ingrese el Nombre",
            border= InputBorder.OUTLINE,       
            border_color="Black",
            label_style=TextStyle(color="Black",italic=True),
        )

    def pruData(self,e):
        id_codProduct = self.id_product.value
        cliente = self.cliente.value
        producto = self.producto.value
        fecha_Elav = self.fecha_Elav.value
        fecha_Rev = self.fecha_Rev.value

        dic = [
            id_codProduct,
            cliente,
            producto,
            fecha_Elav,
            fecha_Rev
        ]
        print(dic)


###### PRUEBAS PARA FILTRADO ###########
    def verInpts(self,e):
        rejex = filter.vrfPrintCard
        jer = len(e.control.value)
        trimmed_value = e.control.value.strip()
        #print(jer)
        if jer != 0 and trimmed_value:
            if filter.vrfPrintCard(e.control.value):
                print(f"{e.control.label}  : {e.control.value}")
                e.control.border_color="green"
            else:
                e.control.border_color="red"
                print("Incorrecto")
        else:
            e.control.border_color="red"
            print("Campo Vacio")

        e.control.update()  # Actualiza el control para reflejar los cambios

    '''def add_data(self, e):
        name = self.name.value
        age = str(self.age.value)
        email = self.email.value
        phone = str(self.phone.value)

        if len(name) and len(age) and len(email) and len(phone) > 0:
            contact_exists = False
            for row in self.data.get_contacts():
                if row[1] == name:
                    contact_exists = True
                    break

            if not contact_exists:
                self.clean_fields()
                self.data.add_contact(name, age, email, phone)
                self.show_data()
            else:
                print("El contacto ya existe en la base de datos.")
        print("Escriba sus datos")'''