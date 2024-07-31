class TuClase:
    def __init__(self):
        self.bnd = None
        self.tpl = []
        self.tpl2 = []

    def tplInptsLam(self):
        return [
            "23",
            "23",
            "24",
            "24",
            [
                "40",
                "40",
                "40",
            ]
        ]
    
    def pr(self):
        tpl = self.tplInptsLam()
        for i in tpl:
            if isinstance(i, list):
                for k in i:
                    return print(k)
    
cl = TuClase()
cl.pr()

