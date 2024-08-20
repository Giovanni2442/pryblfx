from src.Controllers.appFichVent import appFichVent

class InptsAux():
    def __init__(self):
        self.appFicha = appFichVent()

    def changeBtn(self,id):
        if id == "Insert":
            return "Ingresar"
        else:
            return "Update"

    def pruUpdate(self,id,default_value):
        if id != "Insert":
            return self.appFicha.get_row_Id(id)[0]
        else:
            return default_value

