class No:
    def __init__(self,val,canvas,x0,y0,x1,y1):
        self.valor = val
        self.direita = None
        self.esquerda = None
        self.oval = canvas.create_oval(x0, y0, x1, y1, width = 2)
        self.text = canvas.create_text((x1-x0)/2, (y1-y0)/2, text = val)
    def insertDir(self,valor):
        self.direita = No(valor)
    def insertEsq(self,valor):
        self.esquerda = No(valor)

class ArvoreBin:
    def __init__(self,raiz):
        self.root = raiz
