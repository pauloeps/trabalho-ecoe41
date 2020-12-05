import tkinter as tk
import pilha
import fila
import arvorebin
import arvorebinSearch

class Application(tk.Tk):
    def __init__(self):

        #Criacao da janela principal
        super().__init__()
        self.geometry("800x800")
        self.title("Estruturas de Dados")
         
        #Frames
        self.frmPilha = pilha.FramePilha(self)       
        self.frmFila = fila.FrameFila(self)
        self.frmArvBin = arvorebin.FrameTree(self)
        self.frmArvSrc = arvorebinSearch.FrameTree(self)
        
        #Menu
        self.menubar = tk.Menu(self)
        estruturamenu = tk.Menu(self.menubar)
        ajudamenu = tk.Menu(self.menubar)
        estruturamenu.add_command(label='Pilha', command=self.selPilha)
        estruturamenu.add_command(label='Fila', command=self.selFila)
        estruturamenu.add_command(label='Árvore Binária', command=self.selArvBin)
        estruturamenu.add_command(label='Árvore Binária de Busca', command=self.selArvSrc)
        ajudamenu.add_command(label='Sobre', command=self.selSobre)
        self.menubar.add_cascade(label="Estrutura", menu=estruturamenu)
        self.menubar.add_cascade(label="Ajuda", menu=ajudamenu)
        self.config(menu=self.menubar)

    #Funcao para retirar frames da janela
    def retirarFrames(self):
        self.frmPilha.pack_forget()
        self.frmFila.pack_forget()
        self.frmArvBin.pack_forget()
        self.frmArvSrc.pack_forget()
    
    #Funcao ao selecionar Pilha
    def selPilha(self):
        self.retirarFrames()
        self.frmPilha.pack()

    #Funcao ao selecionar Fila
    def selFila(self):
        self.retirarFrames()
        self.frmFila.pack()

    #Funcao ao selecionar Arvore Binaria
    def selArvBin(self):
        self.retirarFrames()
        self.frmArvBin.pack()

    #Funcao ao selecionar Arvore Binaria de Busca
    def selArvSrc(self):
        self.retirarFrames()
        self.frmArvSrc.pack()

    #Janela Sobre
    def selSobre(self):
        janelaSobre = tk.Tk()
        janelaSobre.geometry("500x250")
        janelaSobre.title("Sobre este trabalho")
        strSobre = ('Trabalho da disciplina ECOE41 - Tópicos Especiais em Programação Teórica\n'
        'Professores Edmilson Marmo Moreira e Edvard Martins de Oliveira\n'
        'Universidade Federal de Itajubá\n'
        '\nEste trabalho teve como propósito criar uma visualização\n'
        'de estruturas de dados, para permitir que uma pessoa que\n'
        'esteja estudando este assunto, possa aprender de uma forma\n'
        'interativa e visual.\n\n'
        'Criado por:\n'
        '- Gabriel Orlando Campista Petrucci\n'
        '- Jean Tan Li\n'
        '- Paulo Eduardo Paes Salomon\n')
        lblSobre = tk.Label(janelaSobre, text=strSobre)
        lblSobre.pack()
        janelaSobre.mainloop()

app=Application()
app.mainloop()
        