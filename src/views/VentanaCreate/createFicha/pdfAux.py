class MtdsAuxPdf():
    def __init__(self):
        pass
    # tpl : Lista de Entradas
    # i : Indice de la tabla
    # j : indice el elemento en la tabla
    # arg : character a utilizar, ejemplo : +,- etc..
    # txt : Algun Texto adicional
    def pru(self,tpl,i,j,*arg): # Ayuda a Colocar las Tolerancias o inputs secundarios al PDF
        if tpl[i][j].items[1].content.controls[1].value != '0':
            return f"{tpl[i][j].items[0].content.controls[1].value.upper()} {arg[0]} {tpl[2][14].items[1].content.controls[1].value.upper()} {arg[1]}"
        else:
            return tpl[i][j].items[0].content.controls[1].value.upper(),