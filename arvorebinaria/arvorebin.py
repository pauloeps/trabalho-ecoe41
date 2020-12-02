import tkinter as tk
import math as m
from functools import partial
from tkinter import messagebox
class No:
    def __init__(self,val,circ,text,x,y,colocado=None):
        self.valor = val
        self.circulo = circ
        self.texto = text
        self.direita = None
        self.esquerda = None
        self.linha = None
        self.esqDir = colocado
        self.posicoes(x,y)
    def __str__(self):
        return "{0}".format(self.valor)
    def posicoes(self,x,y):
        aux = m.sin(m.radians(45))*10
        self.x = x
        self.y = y
        self.y1 = self.y-10
        self.x2 = self.x + aux
        self.y2 = self.y + aux
        self.x3 = self.x - aux
        
class Linha:
    def __init__(self,canvas,noStart,noEnd,esqDir):
        self.canvas = canvas
        self.noInicio = noStart
        self.noFim = noEnd
        self.direct = esqDir
        if(esqDir == "esquerda"):
            self.linha = canvas.create_line(self.noInicio.x3,self.noInicio.y2,self.noFim.x,self.noFim.y1,fill="black")
        else:
            self.linha = canvas.create_line(self.noInicio.x2,self.noInicio.y2,self.noFim.x,self.noFim.y1,fill="black")
        self.atualiza()
    def atualiza(self):
        if self.linha:
            if(self.direct == "esquerda"):
                self.canvas.coords(self.linha,self.noInicio.x3,self.noInicio.y2,self.noFim.x,self.noFim.y1)
            else:
                self.canvas.coords(self.linha,self.noInicio.x2,self.noInicio.y2,self.noFim.x,self.noFim.y1)
            self.canvas.after(10,self.atualiza)
        
class ArvoreBin:
    def __init__(self):
        self.root = None
    def emOrdem(self,noAux,canvas):
        print("Cheguei")
        if noAux is None:
            return
        if noAux.esquerda is None:
            self.mudaCor(canvas,noAux,True)
            canvas.after(2000,self.mudaCor,canvas,noAux,False)
        canvas.after(2000,self.emOrdem,noAux.esquerda,canvas)
        print (noAux.valor, end = " ")
        canvas.after(4000,self.emOrdem,noAux.direita,canvas)
        
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
    def findNo(self,noAux,aux):
        if noAux is None:
            return
        if noAux.circulo is aux or noAux.texto is aux:
            self.find = noAux
        self.findNo(noAux.esquerda,aux)
        self.findNo(noAux.direita,aux)
        return self.find
    def mudaCor(self,canvas,no,vF):
        if vF:
            canvas.itemconfig(no.circulo,outline="blue")
        else:
            canvas.itemconfig(no.circulo,outline="black")

class Menu(tk.LabelFrame):
    def __init__(self,master):
        super().__init__(master,text = "Binary Tree Manger")
        self.lf = tk.LabelFrame(self,text = "Infos")
        self.info = tk.Label(self.lf, text = "Left Button Mouse = Select Node\Insert Node\nRight Button Mouse = Remove Node\nIf Node Selected you can move with arrows")
        self.valno = tk.LabelFrame(self,text = "Node Value")
        self.caminhamento = tk.LabelFrame(self,text = "Walk")
        self.entrada = tk.Entry(self.valno,width = 10,relief = "groove",justify = tk.RIGHT)
        self.emOrdem = tk.Button(self.caminhamento,text = "In Order")
        self.preOrdem = tk.Button(self.caminhamento,text = "Pre Order")
        self.posOrdem = tk.Button(self.caminhamento,text = "Pos Order")
        self.lf.grid(sticky = tk.N, row = 0, column = 0)
        self.valno.grid(sticky = tk.EW,row = 1,column = 0)
        self.caminhamento.grid(sticky = tk.EW,row = 2, column = 0)
        self.entrada.pack(fill=tk.BOTH)
        self.emOrdem.pack(fill=tk.BOTH)
        self.preOrdem.pack(fill=tk.BOTH)
        self.posOrdem.pack(fill=tk.BOTH)
        self.info.pack()
class CanvasTree(tk.Canvas):
    def __init__(self,master,tree,menu):
        super().__init__(master, bg = "white", width = 600, height = 700)
        self.menu = menu
        self.arvore = tree
        self.selecionado = None
        self.bind("<Button-1>",self.draw_No)
        self.bind("<Button-3>",self.removeNo)
    def draw_No(self,event):
        x,y = event.x,event.y
        valor = self.menu.entrada.get()
        if(self.arvore.root is None):
            try:
                valor = int(valor)
                circ = self.create_oval(x-10,y-10,x+10,y+10,width = 2,fill="white")
                text = self.create_text(x,y,text = valor)
                self.menu.entrada.delete(0,"end")
                no = No(valor,circ,text,x,y)
                self.arvore.root = no
                partialEmOrdem = partial(self.arvore.emOrdem,self.arvore.root,self)
                self.menu.emOrdem.configure(command = partialEmOrdem)
            except:
                messagebox.showerror("ERROR","Invalid input")
        else:
            if(self.selecionado is None):
                item = self.find_withtag(tk.CURRENT)
                if(item):
                    no = self.arvore.findNo(self.arvore.root,item[0])
                    if(no):
                        self.selecionado = no
                        self.itemconfig(no.circulo, outline = "red")
            else:
                self.itemconfig(self.selecionado.circulo, outline = "black")
                item = self.find_withtag(tk.CURRENT)
                if (valor==""):
                    if not item or item[0] is self.selecionado.circulo or item[0] is self.selecionado.texto:
                        self.coords(self.selecionado.circulo,x-10,y-10,x+10,y+10)
                        self.coords(self.selecionado.texto,x,y)
                        self.selecionado.posicoes(x,y)
                    else:
                        messagebox.showerror("ERROR","Can't draw over a node!")
                else:
                    try:
                        valor = int(valor)
                        if(not item):
                            self.menu.entrada.delete(0,"end")
                            findNoSel = self.arvore.findNo(self.arvore.root,self.selecionado.circulo)
                            if(x > findNoSel.x):
                                if(findNoSel.direita is None):
                                    circ = self.create_oval(x-10,y-10,x+10,y+10,width = 2,fill="white")
                                    text = self.create_text(x,y,text = valor)
                                    no = No(valor,circ,text,x,y,"direita")
                                    linha = Linha(self,findNoSel,no,"direita")
                                    no.linha = linha
                                    findNoSel.direita = no
                                else:
                                    messagebox.showerror("ERROR","Right node already exist!")
                            else:
                                if(findNoSel.esquerda is None):
                                    circ = self.create_oval(x-10,y-10,x+10,y+10,width = 2,fill="white")
                                    text = self.create_text(x,y,text = valor)
                                    no = No(valor,circ,text,x,y,"esquerda")
                                    linha = Linha(self,findNoSel,no,"esquerda")
                                    no.linha = linha
                                    findNoSel.esquerda = no
                                else:
                                    messagebox.showerror("ERROR","Left node already exist!")
                    except:
                        messagebox.showerror("ERROR","Invalid input")
                self.selecionado = None

    def removeNo(self,event):
        x,y = event.x,event.y
        item = self.find_withtag(tk.CURRENT)
        if(item):
            no = self.arvore.findNo(self.arvore.root,item[0])
            if no.direita is None and no.esquerda is None:
                if no is self.arvore.root:
                    self.delete(no.circulo,no.texto)
                    self.arvore.root = None
                else:
                    preNo = no.linha.noInicio
                    self.delete(no.circulo,no.texto,no.linha.linha)
                    if(preNo.direita is no):
                        preNo.direita = None
                    else:
                        preNo.esquerda = None
            elif no.direita is None or no.esquerda is None:
                if no is self.arvore.root:
                    self.delete(no.circulo,no.texto)
                    if no.direita:
                        self.arvore.root = no.direita
                        self.delete(no.direita.linha.linha)
                        no.direita.linha=None
                        no.direita = None
                    else:
                        self.arvore.root = no.esquerda
                        self.delete(no.esquerda.linha.linha)
                        no.esquerda.linha=None
                        no.esquerda = None
                else:
                    preNo = no.linha.noInicio
                    self.delete(no.circulo,no.texto,no.linha.linha)
                    if preNo.direita is no:
                        if no.direita:
                            no.direita.linha.noInicio = preNo
                            no.direita.linha.direct = "direita"
                            preNo.direita = no.direita
                            no.direita = None
                        else:
                            no.esquerda.linha.noInicio = preNo
                            no.esquerda.linha.direct = "direita"
                            preNo.direita = no.esquerda
                            no.esquerda = None
                    else:
                        if no.direita:
                            no.direita.linha.noInicio = preNo
                            no.direita.linha.direct = "esquerda"
                            preNo.esquerda = no.direita
                            no.direita = None
                        else:
                            no.esquerda.linha.noInicio = preNo
                            no.esquerda.linha.direct = "esquerda"
                            preNo.esquerda = no.esquerda
                            no.esquerda = None
                        
            else:
                messagebox.showerror("ERROR","Can't remove a node with 2 children!")
        
class FrameTree(tk.Frame):
    def __init__(self,master):
        super().__init__(master)
        self.arvore = ArvoreBin()
        self.menu = Menu(self)
        self.menu.grid(sticky=tk.W,row = 0,column = 0)
        self.canvas = CanvasTree(self,self.arvore,self.menu)
        self.canvas.grid(sticky=tk.W,row=0,column=1)
class Tela(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("BinaryTree")
        self.geometry("800x800")
        self.frmPilha = FrameTree(self)
        self.frmPilha.pack()
            
pilha=Tela()
pilha.mainloop()
