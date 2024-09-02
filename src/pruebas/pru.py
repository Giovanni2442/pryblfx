def uno(id):
    print(id)
def dos(id):
    print(id)
def tres(id):
    print(id)
def cuatro(id):
    print(id)
    
def diccionarios(id):

    dic = {
        "uno" : uno,
        "dos": dos, 
        "tres": tres,
        "cuatro": cuatro
    }

    return dic.get("uno")

print(diccionarios("uno"))
    