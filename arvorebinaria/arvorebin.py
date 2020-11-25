class No:
    def __init__(self,val,circ,text):
        self.valor = val
        self.circulo = circ
        self.text
        self.direita = None
        self.esquerda = None
    def insertDir(self,valor):
        self.direita = No(valor)
    def insertEsq(self,valor):
        self.esquerda = No(valor)

class ArvoreBin:
    def __init__(self,raiz):
        self.root = raiz
    def emOrdem(self,noAux):
        if noAux is None:
            return
        self.emOrdem(noAux.esquerda)
        print (noAux.valor, end = " ")
        self.emOrdem(noAux.direita)
        
    def preOrdem(self,noAux):
        if noAux is None:
            return
        print (noAux.valor,end = " ")
        self.preOrdem(noAux.esquerda)
        self.preOrdem(noAux.direita)
        
    def posOrdem(self,noAux):
        if noAux is None:
            return
        self.posOrdem(noAux.esquerda)
        self.posOrdem(noAux.direita)
        print (noAux.valor, end = " ")

class DrawCircle():
    
