import tkinter as tk
from tkinter import messagebox
#variável para controlar o tamanho do bloco da pilha
l = 20
#Classe que desenha o bloco da pilha
class Draw_Rect:
    def __init__(self,canvas,y,value,larg,alt):
        self.y = y
        self.canvas = canvas
        self.value = value   
        self.rect_draw = self.canvas.create_rectangle(larg-l,alt-2*l+self.y,larg+l,alt+self.y,outline = "blue")
        self.rect_text = self.canvas.create_text((larg,alt-l+self.y),text = value,font=("Courier", 18))
    def delete_rect(self):
        self.canvas.delete(self.rect_draw,self.rect_text)

class Stack:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def peek(self):
         return self.items[-1]

     def size(self):
         return len(self.items)

class Options(tk.LabelFrame):
    def __init__(self,master,canvas):
        super().__init__(master,text = "Stack Manager")
        self.y = 0
        self.radiob_list = list()
        self.opt = ["New Stack","Push","Pop"]
        self.stack = Stack()
        self.canvas = canvas
        self.larg = self.canvas.winfo_reqwidth()/2
        self.alt = self.canvas.winfo_reqheight() - 10
        self.value = tk.StringVar()
        self.option = tk.StringVar()
        self.canvas.bind("<Button-1>",self.mouse_clicked)
        for i in range(3):
            self.radiob_list.append(tk.Radiobutton(self,text = self.opt[i],variable = self.option,value = self.opt[i]))
            self.radiob_list[i].grid(sticky = tk.W, row = i,column= 0,pady = 2)
        self.option.trace("w",self.paint)
        self.option.set(self.opt[0])
        self.label = tk.Label(self,text = "Value")
        self.opt_text = tk.Entry(self,width=4,relief="groove",textvariable=self.value)
        self.label.grid(sticky = tk.W,row = 4,column =0)
        self.opt_text.grid(sticky = tk.W,row = 4, column = 1,padx=10)
    def show_top(self):
        if not self.stack.isEmpty():
            self.canvas.itemconfig(self.stack.peek().rect_draw, outline = "red")
    def hide_top(self):
        if not self.stack.isEmpty():
            self.canvas.itemconfig(self.stack.peek().rect_draw, outline = "blue")
    def paint(self,*args):
        if self.option.get() == "Pop":
            self.show_top()
        else:
            self.hide_top()
    def mouse_clicked(self,event):
        op = self.get_opt()
        print("Operação : ",op)
        if op == "New Stack":
            if messagebox.askokcancel("Create new stack","This will delete the actual stack"):
                self.canvas.delete("all")
                self.stack = Stack()
                self.y = 0
        elif op == "Push" :
            try:
                if (self.alt-20+self.y) > 0:
                    self.stack.push(Draw_Rect(self.canvas,self.y,self.get_value(),self.larg,self.alt))
                    print("Tamanho da pilha : " ,self.stack.size())
                    self.y-=2*l
                else:
                    print("No more space")
            except:
                messagebox.showerror("ERROR","Value is invalid or stack does not exist")
        elif op == "Pop":
            try:
                print("Tamanho da pilha: ",self.stack.size())
                pos = self.stack.pop()
                pos.delete_rect()
                self.paint()
                self.y+=2*l
            except:
                messagebox.showerror("ERROR","Empty stack or stack does not exist")
    def get_opt(self):
        return self.option.get()
    def get_value(self):
        return int(self.opt_text.get())
        
            
class FramePilha(tk.Frame):
    def __init__(self):
        super().__init__()
        self.tela = tk.Canvas(self,bg = "white", width = 600, height = 700)
        self.opt = Options(self,self.tela)
        self.tela.update()
        self.tela.grid(sticky = tk.W,row=0,column=1)
        self.opt.grid(sticky=tk.W,row = 0,column = 0)
class Pilha(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Pilha DEMO")
        self.geometry("800x800")
        self.app = FramePilha()
        self.app.pack()
            
            

pilha=Pilha()
pilha.mainloop()
        
