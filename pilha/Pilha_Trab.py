import tkinter as tk
from tkinter import messagebox
class Draw_Rect:
    def __init__(self,canvas,y,value,larg,alt):
        self.y = y
        self.canvas = canvas
        self.value = value   
        self.rect_draw = self.canvas.create_rectangle(larg-10,alt-20+self.y,larg+10,alt+self.y)
        self.rect_text = self.canvas.create_text((larg,alt-10+self.y),text = value)
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
    opt = ("Create","Push","Pop","Delete")
    def __init__(self,master,canvas):
        super().__init__(master,text = "Stack Manager")
        self.y = 0
        self.stack = None
        self.canvas = canvas
        self.larg = self.canvas.winfo_reqwidth()/2
        self.alt = self.canvas.winfo_reqheight() 
        self.value = tk.StringVar()
        self.option = tk.StringVar()
        #opt_label = tk.Label(self,text = "Stack Options")
        #opt_label.grid(sticky = tk.W,row=0,column=0)
        self.opt_menu = tk.OptionMenu(self,self.option, *self.opt)
        self.option.set(self.opt[0])
        self.label = tk.Label(self,text = "Value")
        self.opt_text = tk.Entry(self,width=4,relief="groove",textvariable=self.value)
        self.opt_apply = tk.Button(self,text="Apply", command = self.apply_opt)
        
        self.opt_menu.grid(sticky=tk.W,row=0,column=0)
        self.opt_apply.grid(sticky =tk.W,row=3,column=0)
        self.label.grid(sticky = tk.W,row = 2,column =0)
        self.opt_text.grid(sticky = tk.W,row = 2, column = 1,padx=10)
        
    def get_opt(self):
        return self.option.get()
    def get_value(self):
        return int(self.opt_text.get())
    def apply_opt(self):
        op = self.get_opt()
        print("Operação : ",op)
        if op == "Create":
            if self.stack is None:
                self.stack = Stack()
            elif messagebox.askokcancel("Create new stack","This will delete the actual stack"):
                self.canvas.delete("all")
                self.stack = Stack()
                self.y = 0
        elif op == "Push" :
            try:
                if (self.alt-20+self.y) > 0:
                    rect = Draw_Rect(self.canvas,self.y,self.get_value(),self.larg,self.alt)
                    self.stack.push(rect)
                    print("Tamanho da pilha : " ,self.stack.size())
                    self.y-=20
                else:
                    print("No more space")
            except:
                messagebox.showerror("ERROR","Value is invalid or stack does not exist")
        elif op == "Pop":
            try:
                print("Tamanho da pilha: ",self.stack.size())
                print(self.stack.peek())
                pos = self.stack.pop()
                pos.delete_rect()
                self.y+=20
            except:
                messagebox.showerror("ERROR","Empty stack or stack does not exist")
        if op == "Delete":
            if messagebox.askyesno("Delete stack","Delete the current stack?"):
                self.canvas.delete("all")
                self.stack = None
                self.y = 0
            
class Pilha(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Pilha DEMO")
        self.geometry("800x800")
        self.tela = tk.Canvas(self,bg = "white", width = 600, height = 600)
        self.opt = Options(self,self.tela)
        self.tela.update()
        self.tela.grid(sticky = tk.W,row=0,column=1)
        self.opt.grid(sticky=tk.W,row = 0,column = 0)

pilha=Pilha()
pilha.mainloop()
        
