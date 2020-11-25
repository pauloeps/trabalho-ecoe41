"""
import tkinter as tk

class FramePilha(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.lblPilha = tk.Label(self, text='Implementacao Pilha')
        self.lblPilha.pack()

class FrameFila(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.lblFila = tk.Label(self, text='Implementacao Fila')
        self.lblFila.pack()

class JanelaSecundaria(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Uma janela secundaria")
        self.geometry('300x300')
"""

import tkinter as tk
import pilha
import fila

class Application(tk.Tk):
    def __init__(self):

        #Criacao da janela principal
        super().__init__()
        self.geometry("800x800")
        self.title("Estruturas de Dados")
         
        #Frames
        self.frmPilha = pilha.FramePilha(self)       
        self.frmFila = fila.FrameFila(self)
        
        #Menu
        self.menubar = tk.Menu(self)
        estruturamenu = tk.Menu(self.menubar)
        estruturamenu.add_command(label='Pilha', command=self.selPilha)
        estruturamenu.add_command(label='Fila', command=self.selFila)
        estruturamenu.add_command(label='Outra Janela', command=self.abrirJanSec)
        self.menubar.add_cascade(label="Estrutura", menu=estruturamenu)
        self.config(menu=self.menubar)

    #Funcao para retirar frames da janela
    def retirarFrames(self):
        self.frmPilha.pack_forget()
        self.frmFila.pack_forget()
    
    #Funcao ao selecionar Pilha
    def selPilha(self):
        self.retirarFrames()
        self.frmPilha.pack()

    #Funcao ao selecionar Fila
    def selFila(self):
        self.retirarFrames()
        self.frmFila.pack()

    #Funcao para abrir janela secundaria
    def abrirJanSec(self):
        print('Fui Executado!')
        jSec = JanelaSecundaria()
        jSec.mainloop()

app=Application()
app.mainloop()
        