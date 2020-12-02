import tkinter as tk
import math as m
from functools import partial
from tkinter import messagebox
class No:
    def __init__(self,val,circ,text,x,y):
        self.valor = val
        self.circulo = circ
        self.texto = text
        self.direita = None
        self.esquerda = None
        self.linha = None
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
        self.time = 0
    def emOrdem(self,noAux,canvas,resetTime):
        if resetTime:
            self.time = 0
            print()
            print("Walk In Order!")
        canvas.update()
        if noAux is None:
            return
        self.emOrdem(noAux.esquerda,canvas,False)
        print (noAux.valor, end = " ")
        canvas.after(self.time,self.mudaCor,canvas,noAux,True)
        canvas.after(self.time+1500,self.mudaCor,canvas,noAux,False)
        self.time += 1500
        self.emOrdem(noAux.direita,canvas,False)
        
    def preOrdem(self,noAux,canvas,resetTime):
        if resetTime:
            self.time = 0
            print()
            print("Walk Pre Order!")
        canvas.update()
        if noAux is None:
            return
        print (noAux.valor,end = " ")
        canvas.after(self.time,self.mudaCor,canvas,noAux,True)
        canvas.after(self.time+1500,self.mudaCor,canvas,noAux,False)
        self.time += 1500
        self.preOrdem(noAux.esquerda,canvas,False)
        self.preOrdem(noAux.direita,canvas,False)
        
    def posOrdem(self,noAux,canvas,resetTime):
        if resetTime:
            self.time = 0
            print()
            print("Walk Pos Order!")
        canvas.update()
        if noAux is None:
            return
        self.posOrdem(noAux.esquerda,canvas,False)
        self.posOrdem(noAux.direita,canvas,False)
        print (noAux.valor, end = " ")
        canvas.after(self.time,self.mudaCor,canvas,noAux,True)
        canvas.after(self.time+1500,self.mudaCor,canvas,noAux,False)
        self.time += 1500
    def findNo(self,noAux,aux):
        if noAux is None:
            return
        if noAux.circulo is aux or noAux.texto is aux:
            self.find = noAux
        self.findNo(noAux.esquerda,aux)
        self.findNo(noAux.direita,aux)
        return self.find
    def insert(self,noAux,valorIn,x,y,canvas,resetNoIn):
        if resetNoIn:
            self.noIn = None
        if noAux is None:
            circ = canvas.create_oval(x-10,y-10,x+10,y+10,width = 2,fill="white")
            text = canvas.create_text(x,y,text = valorIn)
            self.noIn = No(valorIn,circ,text,x,y)
            return self.noIn
        if valorIn < noAux.valor:
            noAux.esquerda = self.insert(noAux.esquerda,valorIn,x,y,canvas,False)
            if(noAux.esquerda is self.noIn):
                linha = Linha(canvas,noAux,noAux.esquerda,"esquerda")
                noAux.esquerda.linha = linha
        elif valorIn > noAux.valor:
            noAux.direita = self.insert(noAux.direita,valorIn,x,y,canvas,False)
            if(noAux.direita is self.noIn):
                linha = Linha(canvas,noAux,noAux.direita,"direita")
                noAux.direita.linha = linha
        if noAux.valor == valorIn:
             messagebox.showerror("ERROR","The value is already in the tree!")
        return noAux
    def insertNo(self,valorIn,x,y,canvas):
        self.root = self.insert(self.root,valorIn,x,y,canvas,True)
    def deletar(self,noAux,no,canvas):
        if no.valor < noAux.valor:
            noAux.left = self._del()
    def mudaCor(self,canvas,no,vF):
        if vF:
            canvas.itemconfig(no.circulo,outline="blue")
        else:
            canvas.itemconfig(no.circulo,outline="black")

class Menu(tk.LabelFrame):
    def __init__(self,master):
        super().__init__(master,text = "Binary Search Tree Manager")
        self.lf = tk.LabelFrame(self,text = "Infos")
        self.info = tk.Label(self.lf, text = "Left Button Mouse = Select Node\Insert Node\nRight Button Mouse = Remove Node\nIf Node is selected you can move by clicking on Canvas\n If root is selected you can insert")
        self.valno = tk.LabelFrame(self,text = "Node Value")
        self.caminhamento = tk.LabelFrame(self,text = "Walk")
        self.search = tk.LabelFrame(self,text = "Search Value")
        self.entrada = tk.Entry(self.valno,width = 10,relief = "groove",justify = tk.CENTER)
        self.searchEntry = tk.Entry(self.search,width = 10, relief = "groove", justify = tk.CENTER)
        self.searchButton = tk.Button(self.search,text = "Search")
        self.emOrdem = tk.Button(self.caminhamento,text = "In Order")
        self.preOrdem = tk.Button(self.caminhamento,text = "Pre Order")
        self.posOrdem = tk.Button(self.caminhamento,text = "Pos Order")
        self.lf.grid(sticky = tk.N, row = 0, column = 0)
        self.valno.grid(sticky = tk.EW,row = 1,column = 0)
        self.caminhamento.grid(sticky = tk.EW,row = 2, column = 0)
        self.search.grid(sticky = tk.EW, row = 3, column = 0)
        self.entrada.pack(fill=tk.BOTH)
        self.emOrdem.pack(fill=tk.BOTH)
        self.preOrdem.pack(fill=tk.BOTH)
        self.posOrdem.pack(fill=tk.BOTH)
        self.searchEntry.pack(fill=tk.BOTH)
        self.searchButton.pack(fill=tk.BOTH)
        self.info.pack()
class CanvasTree(tk.Canvas):
    def __init__(self,master,tree,menu):
        super().__init__(master, bg = "white", width = 600, height = 700)
        self.menu = menu
        self.arvore = tree
        self.selecionado = None
        self.bind("<Button-1>",self.draw_No)
        self.bind("<Button-3>",self.removeNo)
        self.update()
    def draw_No(self,event):
        x,y = event.x,event.y
        valor = self.menu.entrada.get()
        if(self.arvore.root is None):
            try:
                valor = int(valor)
                self.menu.entrada.delete(0,"end")
                self.arvore.insertNo(valor,x,y,self)
                partialEmOrdem = partial(self.arvore.emOrdem,self.arvore.root,self,True)
                self.menu.emOrdem.configure(command = partialEmOrdem)
                partialPreOrdem = partial(self.arvore.preOrdem,self.arvore.root,self,True)
                self.menu.preOrdem.configure(command = partialPreOrdem)
                partialPosOrdem = partial(self.arvore.posOrdem,self.arvore.root,self,True)
                self.menu.posOrdem.configure(command = partialPosOrdem)
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
                elif self.selecionado is self.arvore.root:
                    try:
                        valor = int(valor)
                        if(not item):
                            self.menu.entrada.delete(0,"end")
                            if(x > self.arvore.root.x):
                                if(valor > self.arvore.root.valor):
                                    self.arvore.insertNo(valor,x,y,self)
                                elif valor < self.arvore.root.valor:
                                    messagebox.showerror("ERROR","The value is lower than root!")
                            else:
                                if(valor < self.arvore.root.valor):
                                    self.arvore.insertNo(valor,x,y,self)
                                elif valor > self.arvore.root.valor:
                                    messagebox.showerror("ERROR","The value is bigger than root!")
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
        self.title("BinarySearchTree")
        self.geometry("800x800")
        self.frmPilha = FrameTree(self)
        self.frmPilha.pack()
            
pilha=Tela()
pilha.mainloop()
