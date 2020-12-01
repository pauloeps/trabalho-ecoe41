import tkinter as tk
from tkinter import messagebox
class No:
    def __init__(self,val,circ,text,x,y):
        self.valor = val
        self.circulo = circ
        self.texto = text
        self.direita = None
        self.esquerda = None
        self.x = x
        self.y = y
    def __str__(self):
        return "{0}".format(self.valor)

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
    def findNo(self,noAux,aux):
        if noAux is None:
            return
        if noAux.circulo is aux or noAux.texto is aux:
            print("noAUX",noAux)
            return noAux
        self.findNo(noAux.esquerda,aux)
        self.findNo(noAux.direita,aux)

class Menu(tk.LabelFrame):
    def __init__(self,master):
        super().__init__(master,text = "Binary Tree Manger")
        self.lf = tk.LabelFrame(self,text = "Infos")
        self.info = tk.Label(self.lf, text = "Left Button Mouse = Select Node\Insert Node\nRight Button Mouse = Remove Node\nIf Node Selected you can move with arrows")
        self.valno = tk.LabelFrame(self,text = "Value Node")
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
            except:
                messagebox.showerror("ERROR","Invalid input")
        else:
            if(self.selecionado is None):
                item = self.find_withtag(tk.CURRENT)
                if(item):
                    no = self.arvore.findNo(self.arvore.root,item[0])
                    print(no)
                    if(no):
                        self.selecionado = no
                        self.itemconfig(no.circulo, outline = "red")
            else:
                self.itemconfig(self.selecionado.circulo, outline = "black")
                if (valor==""):
                    self.coords(self.selecionado.circulo,x-10,y-10,x+10,y+10)
                    self.coords(self.selecionado.texto,x,y)
                else:
                    try:
                        valor = int(valor)
                        item = self.find_withtag(tk.CURRENT)
                        if(not item):
                            self.menu.entrada.delete(0,"end")
                            findNoSel = self.arvore.findNo(self.arvore.root,self.selecionado.circulo)
                            print (findNoSel)
                            if(x > findNoSel.x):
                                if(findNoSel.direita is None):
                                    circ = self.create_oval(x-10,y-10,x+10,y+10,width = 2,fill="white")
                                    text = self.create_text(x,y,text = valor)
                                    no = No(valor,circ,text,x,y)
                                    findNoSel.direita = no
                                    self.arvore.emOrdem(self.arvore.root)
                                else:
                                    messagebox.showerror("ERROR","Right node already exist!")
                            else:
                                if(findNoSel.esquerda is None):
                                    circ = self.create_oval(x-10,y-10,x+10,y+10,width = 2,fill="white")
                                    text = self.create_text(x,y,text = valor)
                                    no = No(valor,circ,text,x,y)
                                    findNoSel.esquerda = no
                                    self.arvore.emOrdem(self.arvore.root)
                                else:
                                    messagebox.showerror("ERROR","Left node already exist!")
                    except:
                        messagebox.showerror("ERROR","Invalid input")
                self.selecionado = None
                
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
        self.title("Stack")
        self.geometry("800x800")
        self.frmPilha = FrameTree(self)
        self.frmPilha.pack()
            
pilha=Tela()
pilha.mainloop()
