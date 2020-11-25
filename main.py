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

app=Application()
app.mainloop()
        