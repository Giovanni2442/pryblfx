class TuClase:
    def __init__(self):
        self.bnd = None
        self.tpl = []
        self.tpl2 = []

    def vlMnuPop(self, inx, j):
        if self.bnd == inx:
            print(f"id : {self.bnd}  :  {j}")
            self.tpl2.append(self.bnd)
        else:
            # Añade el último conjunto antes de vaciar self.tpl2
            if self.tpl2:
                self.tpl.append(self.tpl2)
            self.tpl2 = []
            self.bnd = inx
            
        # Asegúrate de agregar el último conjunto al final
        if inx == len(funciones) - 1:  # Aquí asumimos que 'inx' es el índice final esperado
            if self.tpl2:
                self.tpl.append(self.tpl2)

    def dic(self, inx, j):
        # NOTA : El post solo acepta arreglos NO iteraci+ón
        funciones = {
            0: self.vlMnuPop,
            1: self.vlMnuPop,
            2: self.vlMnuPop,
           # 3: self.vlMnuPop, # Elemento NO funcional por bug
        }
        funcion = funciones.get(inx)
        if funcion:
            funcion(inx, j)
        else:
            print(f"No hay función definida para el índice {inx}")

    def upd(self, e):
        #pr2
        #tplInpts
        self.vrf.pru(
            self.Inpts.tplInptsFichTec(),
            self.Inpts.tplInptsVentas(),
            #self.InptsExtrc.tplInptsExtr(),
            #self.Inpts.tplInptsFichTec(), # Arreglar el bug, ya que no acepta el ultimo conjunto
        )

# Ejemplo de uso
clase = TuClase()
clase.dic(0, 'dato')
clase.dic(1, 'dato')
clase.dic(2, 'dato')
print(clase.tpl)
