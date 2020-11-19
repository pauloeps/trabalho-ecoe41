"""" 
Este codigo ilustra um exemplo de como sera a aplicacao principal.
Criaremos uma classe que herda de tk.Frame para cada estrutura
e toda a implementacao deve ficar dentro deste frame, que sera
instanciado nesta classe principal que ira criar a janela e 
alterar os frames de cada estrutura conforme selecionarmos no
menu.

Cada classe representando uma estrutura diferente, deve estar
no seu proprio arquivo, porem aqui foi colocado em um arquivo
so por motivos de facilidade de visualizacao do codigo.

Por motivos de simplicidade, o unico elemento dos frames usados
para demonstracao e um label, porem na implementacao real, iremos
colocar todos os elementos da interface criada dentro deste frame.

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

class Application(tk.Tk):
    def __init__(self):

        #Criacao da janela principal
        super().__init__()
        self.geometry("800x600")
        self.title("Estruturas de Dados")
        
        #Frames
        self.frmPilha = FramePilha(self)       
        self.frmFila = FrameFila(self)
        
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
        