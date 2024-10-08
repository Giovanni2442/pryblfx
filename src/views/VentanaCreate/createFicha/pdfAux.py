class MtdsAuxPdf():
    def __init__(self,estd):
        self.estd = estd
    # tpl : Lista de Entradas
    # i : Indice de la tabla
    # j : indice el elemento en la tabla
    # arg : character a utilizar, ejemplo : +,- etc..
    # txt : Algun Texto adicional
    #'''

    # --- SOLO SIRVE PARA INSERCIÓNES ----# 
    def toleranciasInsert(self,tpl,i,j,arg): # Ayuda a Colocar las Tolerancias o inputs secundarios al PDF
        if str(tpl[i][j].items[1].content.controls[1].value) != '0.0':
            #print(tpl[i][j].items[1].content.controls[1].value)
            return f"{tpl[i][j].items[0].content.controls[1].value} {arg[0]} {tpl[i][j].items[1].content.controls[1].value} {arg[1]}"
        else:
            return str(tpl[i][j].items[0].content.controls[1].value),

    def tolLamInsert(self,tpl,i,j,k,arg): # Ayuda a Colocar las Tolerancias o inputs secundarios al PDF
        if str(tpl[i][j][k].items[1].content.controls[1].value) != '0.0':
            return f"{tpl[i][j][k].items[0].content.controls[1].value} {arg[0]} {tpl[i][j][k].items[1].content.controls[1].value} {arg[1]}"
        else:
            return str(tpl[i][j][k].items[0].content.controls[1].value),
    # ------------------------------------------------------------------------------------- # 



    # --- SOLO SIRVE PARA AVTUALIZACIÓNES MASIVAS ---- # 

    # Ayuda a Colocar las Tolerancias o inputs secundarios al PDF
    def toleranciasMsv(self,tpl,tbl1,indx1,tbl2,indx2,arg): 
        if str(tpl[tbl2][indx2]) != '0.0' :
            #print(tpl[tbl2][indx2])
            #return "NULL"
            return f"{tpl[tbl1][indx1]} {arg[0]} {tpl[tbl2][indx2]} {arg[1]}"
        else: 
            return str(tpl[tbl1][indx1])
        
   
    def tolLamMsv(self,tpl,tbl1,subTbl1,indx1,tbl2,subTbl2,indx2,arg): # Ayuda a Colocar las Tolerancias o inputs secundarios al PDF
        if str(tpl[tbl2][subTbl2][indx2]) != '0.0':
            return f"{tpl[tbl1][subTbl1][indx1]} {arg[0]} {tpl[tbl2][subTbl2][indx2]} {arg[1]}"
        else:
            return str(tpl[tbl2][subTbl2][indx2]),
    # ------------------------------------------------------------------------------------- # 

        # --- INTERFACES DE METODOS --- #

    # TOLERANCIAS DE LOS FORMULARIOS
    def frmlTol(self,tpl,tbl0,indx0,tbl1,indx1,tbl2,indx2,*arg):
        if self.estd != "Insert" and self.estd != "Update":
            return self.toleranciasMsv(tpl,tbl1,indx1,tbl2,indx2,arg)
        else:
            return self.toleranciasInsert(tpl,tbl0,indx0,arg)

    def frmlTolLaminas(self,tpl,tbl0,subTbl0,Indx0,tbl1,subTbl1,indx1,tbl2,subTbl2,indx2,*arg):
        if self.estd != "Insert" and self.estd != "Update":
            return self.tolLamMsv(tpl,tbl1,subTbl1,indx1,tbl2,subTbl2,indx2,arg)
        else:
            return self.tolLamInsert(tpl,tbl0,subTbl0,Indx0,arg)   # <--- ARREGLAR AQUI


    # -- MODO DE USO --
    # tbl0,Indx0 = ATRIBUTO_1           : DATOS QUE TOMA DIRECTAMENTE DEL FORMULARIO
    # tbl1,subTbl1,indx1 = ATRIBUTO_2   : DATOS DE LA BASE DE DATOS 
    # tbl2,subTbl2,indx2 = ATRIBUTO_3   : TOLERANCIA
    def frmlTolLamGen(self,tpl,tbl0,Indx0,tbl1,subTbl1,indx1,tbl2,subTbl2,indx2,*arg):
        if self.estd != "Insert" and self.estd != "Update":
            return self.tolLamMsv(tpl,tbl1,subTbl1,indx1,tbl2,subTbl2,indx2,arg)
        else:
            return self.toleranciasInsert(tpl,tbl0,Indx0,arg)   # <--- ARREGLAR AQUI    

        #'''

    # tupla     :   tupal con conjunto de listas
    # tbl       :   Tabla
    # indx      :   Indice del elemento en la tabla
    def txtAux(self,tupla,tbl,indx):
        tplUpdtMav = tupla
        tplInsert = tupla

        #print("eyy aqui -",self.estd)
        if self.estd != "Insert" and self.estd != "Update":
            #print("-->-",tupla[indx2])
            #print(".i.",1)
            return tplUpdtMav[tbl][indx]
        else:
            #print(".i.",2)
            return tplInsert[tbl][indx].value.upper()
        
    def txtAux2(self,tupla,tbl1,indx1,tbl2,indx2):
        tplUpdtMav = tupla
        tplInsert = tupla

        #print("eyy aqui -",self.estd)
        if self.estd != "Insert" and self.estd != "Update":
            #print("-->-",tupla[indx2])
            #print(".i.",1)
            return tplUpdtMav[tbl2][indx2]
        else:
            #print(".i.",2)
            return tplInsert[tbl1][indx1].value

    def txtAuxLamGen(self,tupla,tbl1,indx1,tbl2,indx2,indx3):
        tplUpdtMav = tupla
        tplInsert = tupla

        #print("eyy aqui -",self.estd)
        if self.estd != "Insert" and self.estd != "Update":
            #print("-->-",tupla[indx2])
            #print(".i.",1)
            return tplUpdtMav[tbl2][indx2][indx3]
        else:
            #print(".i.",2)
            return tplInsert[tbl1][indx1].value
        
    def txtAuxLamins(self,tupla,tbl0,subTbl0,indx0,tbl1,subTbl1,indx1):
        tplUpdtMav = tupla
        tplInsert = tupla

        #print("eyy aqui -",self.estd)
        if self.estd != "Insert" and self.estd != "Update":
            #print("-->-",tupla[indx2])
            #print(".i.",1)
            return tplUpdtMav[tbl1][subTbl1][indx1]
        else:
            #print(".i.",2)
            return tplInsert[tbl0][subTbl0][indx0].value



class frmtDtaUpdate:
    def __init__(self):
        pass       

    # TRANSFORMA LOS DATOS TRAIDOS DE LA BD EN SUBLISTAS
    def formatData(self,tplData): 
        # Lista que contendrá las sublistas
        resultado = []
        # Variable temporal para almacenar cada grupo de elementos entre los '1111'
        grupo_actual = []

        id = tplData[0]

        # Iterar sobre la tupla
        for elemento in tplData:
            if elemento == id:
                # Si ya hay un grupo en curso, se añade a la lista de resultado
                if grupo_actual:
                    resultado.append(grupo_actual)
                # Iniciar un nuevo grupo
                grupo_actual = [elemento]
            else:
                # Añadir elementos al grupo actual
                grupo_actual.append(elemento)

        # Añadir el último grupo al resultado si existe
        if grupo_actual:
            resultado.append(grupo_actual)

        # Eliminar el primer elemento '1111' de cada sublista excepto la primera
        for i in range(1, len(resultado)):
            resultado[i] = resultado[i][1:]

        # Mostrar el resultado
        #print(resultado)
        return resultado
