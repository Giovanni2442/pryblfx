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

slicesLst()
    