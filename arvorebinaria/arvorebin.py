import tkinter as tk
from tkinter import messagebox
class No:
    def __init__(self,val,circ,text):
        self.valor = val
        self.circulo = circ
        self.texto = text
        self.direita = None
        self.esquerda = None
    def insertDir(self,valor,circ,text):
        self.direita = No(valor,circ,text)
    def insertEsq(self,valor,circ,text):
        self.esquerda = No(valor,circ,text)

class ArvoreBin:
    def __init__(self):
        self.root = None
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

class Menu(tk.LabelFrame):
    def __init__(self,master,canvas,arvore):
        super().__init__(master,text = "Binary Tree Manger")
        self.canvas = canvas
        self.arvore = arvore
        self.lf = tk.LabelFrame(self,text = "Infos")
        self.info = tk.Label(self.lf, text = "Left Button Mouse = Select Node\Insert Node\nRight Button Mouse = Remove Node\nIf Node Selected you can move with arrows")
        self.valno = tk.LabelFrame(self,text = "Valor do No")
        self.caminhamento = tk.LabelFrame(self,text = "Caminhamento")
        self.entrada = tk.Entry(self.valno,width = 10,relief = "groove",justify = tk.RIGHT)
        self.emOrdem = tk.Button(self.caminhamento,text = "Em Ordem")
        self.preOrdem = tk.Button(self.caminhamento,text = "Pre Ordem")
        self.posOrdem = tk.Button(self.caminhamento,text = "Pos Ordem")
        self.lf.grid(sticky = tk.N, row = 0, column = 0)
        self.valno.grid(sticky = tk.EW,row = 1,column = 0)
        self.caminhamento.grid(sticky = tk.EW,row = 2, column = 0)
        self.entrada.pack(fill=tk.BOTH)
        self.emOrdem.pack(fill=tk.BOTH)
        self.preOrdem.pack(fill=tk.BOTH)
        self.posOrdem.pack(fill=tk.BOTH)
        self.info.pack()
class FrameTree(tk.Frame):
    def __init__(self,master):
        super().__init__(master)
        self.menu = Menu(self,None,None)
        self.menu.grid(sticky=tk.W,row = 0,column = 0)
class Pilha(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Stack")
        self.geometry("800x800")
        self.frmPilha = FrameTree(self)
        self.frmPilha.pack()
            
pilha=Pilha()
pilha.mainloop()
