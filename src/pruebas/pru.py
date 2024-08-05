
class ejemplo():
    def __init__(self):
        pass

    def pr(self):

        for indx,i in enumerate(tpl):       # Recorre las listas de Inputs
            for j in i:                     # Recorre los valores de cada lista
                if isinstance(j, list):     # Verifica si el valor de la lista hay listas, para colocar los valores en la lista padre
                    for f in j:             # Recorre la sub lista desde el indice
                        if isinstance( f, PopupMenuButton):
                            for m in f.items:
                                txtFld = m.content.controls[1]
                                if txtFld.value != "":
                                    if txtfld.error_text !="":
                                        print(txtfld.label)
                                        vlErr.append(txtfld.label)       # Captura los campos vacios
                                    continue
                                else:
                                    txtfld.error_text = "Ingrese los valores"
                                    print(txtfld.label)
                                    vlVoid.append(txtfld.label)
                                    m.content.update()
                    continue
                else:
                    if isinstance(j, PopupMenuButton):
                        for k in j.items:
                            txtfld =  k.content.controls[1]
                            if txtfld.value != "":
                                if txtfld.error_text !="":
                                    print(txtfld.label)
                                    vlErr.append(txtfld.label)       # Captura los campos vacios
                                continue
                            else:
                                txtfld.error_text = "Ingrese los valores"
                                print(txtfld.label)
                                vlVoid.append(txtfld.label)
                                k.content.update()
        
                            #print(k.content.controls[1].value)
                    else:
                        if j.value != "":
                            #if j.border_color != "red":
                            if j.error_text != "":
                                vlErr.append(j.label)       # Captura los campos vacios
                            continue
                        else:
                            j.error_text = "Ingrese los valores"
                            vlVoid.append(j.label)
                            j.update()
    