def uno():
    return ["Hola1","ejemplo1","rgb1"]
def dos():
    return ["Hola2","ejemplo2",""]
def tres():
    return ["Hola3","ejemplo3","rgb3"]

def jer(uno,dos,tres):
    dic = []
    dic = (uno,dos,tres)
    for i,j in dic:
        for j in i:
            if j !="":
                print(j)
            else:
                print(f"Vacio en : {i}")
                break

jer(uno(),dos(),tres())

