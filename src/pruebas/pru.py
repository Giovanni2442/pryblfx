def slicesLst():
    lst = ["IMG","FIG","DSCR",          #EXTRC
           "IMG","FIG","DSCR",          #IMPRS
           "IMG","FIG","DSCR",          #LAM
           "IMG","FIG","DSCR",          #REF
           "IMG","FIG","DSCR"]          #CNVRS         

    #ejemplo[1,4,7]    <- IMAGES
    #ejemplo[2,5,8]    <- FIGURAS
    #ejemplo[3,6,9]

    print(lst[:15:3])       # <- IMAGENES
    print(lst[1:15:3])
    print(lst[2:15:3])

def dicPrbs():
    dicImgs = {
        'EXTRC' :   ['N/A','N/A','N/A'],
        'IMPRC' :   ['N/A','N/A','N/A'],
        'LMNSN' :   ['N/A','N/A','N/A'],
        'RFLD'  :   ['N/A','N/A','N/A'],
        'CNVRSN' :  ['N/A','N/A','N/A']
    }

    dicPrbs = {'EXTRC' : ['N/A','N/A','JI'],
            'LMNSN' : ['N/A','ACTUALIZADO','EJEMPLOS'],}

    print(dicImgs)

    for key in dicPrbs:
        for i,value in enumerate(dicPrbs[key]):  # Acceder a la lista asociada a la clave
            if value != "N/A":
                dicImgs[key][i] = value
                print(i,value)

    print("Avtual -- ",dicImgs)
dicPrbs()








