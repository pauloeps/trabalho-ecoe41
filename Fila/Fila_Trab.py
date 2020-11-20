import tkinter as tk
from tkinter import messagebox
#variável para controlar o tamanho do bloco da pilha
l = 20
#Classe que desenha o bloco da pilha
class Draw_Rect:
    def __init__(self,canvas,y,value,larg):
        self.y = y
        self.canvas = canvas
        self.value = value
        self.height = 2*l 
        self.rect_draw = self.canvas.create_rectangle(larg-l,10+self.y,larg+l,10+self.height+self.y,outline = "blue",tag = 'elem')
        self.rect_text = self.canvas.create_text((larg,10+l+self.y),text = value,font=("Courier", 18),tag = 'elem')
    def delete_rect(self):
        self.canvas.delete(self.rect_draw,self.rect_text)

class Queue:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def enqueue(self, item):
         self.items.append(item)

     def dequeue(self):
         return self.items.pop(0)

     def front(self):
         return self.items[0]

     def size(self):
         return len(self.items)

class Options(tk.LabelFrame):
    def __init__(self,master,canvas):
        super().__init__(master,text = "Queue Manager")
        self.y = 0
        self.radiob_list = list()
        self.opt = ["New Queue","Enqueue","Dequeue"]
        self.queue = Queue()
        self.canvas = canvas
        self.larg = self.canvas.winfo_reqwidth()/2
        self.alt = self.canvas.winfo_reqheight() 
        self.value = tk.StringVar()
        self.option = tk.StringVar()
        self.canvas.info = self.canvas.create_text((16,self.alt/2),font = ("Courier",16),anchor = tk.W)
        self.canvas.bind("<Button-1>",self.do_action)
        for i in range(3):
            self.radiob_list.append(tk.Radiobutton(self,text = self.opt[i],variable = self.option,value = self.opt[i]))
            self.radiob_list[i].grid(sticky = tk.W, row = i,column= 0,pady = 2)
        self.option.trace("w",self.paint)
        self.option.set(self.opt[0])
        self.label = tk.Label(self,text = "Value(s)")
        self.opt_text = tk.Entry(self,width=10,relief="groove",textvariable=self.value)
        self.label.grid(sticky = tk.N,row = 4,column =0)
        self.opt_text.grid(sticky = tk.N,row = 5, column = 0)
        self.opt_text.bind("<Return>",self.do_action)
        
    def show_front(self):
        if not self.queue.isEmpty():
            self.canvas.itemconfig(self.queue.front().rect_draw, outline = "red")
    def hide_front(self):
        if not self.queue.isEmpty():
            self.canvas.itemconfig(self.queue.front().rect_draw, outline = "blue")
    def paint(self,*args):
        if self.option.get() == "Dequeue":
            self.canvas.itemconfig(self.canvas.info, text = "Remove front\nSize:%d"%self.queue.size())
            self.show_front()
        elif self.option.get() == "New Queue":
            self.canvas.itemconfig(self.canvas.info, text = "Queue created\nSize:%s"%self.queue.size())
            self.hide_front()
        elif self.option.get() == "Enqueue":
            self.canvas.itemconfig(self.canvas.info, text = "Inserting items\nSize:%d"%self.queue.size())
            self.hide_front()
    def do_action(self,event):
        op = self.get_opt()
        print("Operação : ",op)
        if op == "New Queue":
            if messagebox.askokcancel("Create new queue","This will delete the actual queue"):
                self.canvas.delete("elem")
                self.queue = Queue()
                self.paint()
                self.y = 0
        elif op == "Enqueue" :
            try:
                values = self.get_value()
                print(values)
                for actual_val in values:
                    if (self.y) < (self.alt):
                        self.queue.enqueue(Draw_Rect(self.canvas,self.y,actual_val,self.larg))
                        print("Tamanho da fila : " ,self.queue.size())
                        self.paint()
                        self.opt_text.delete(0,"end")
                        self.y+=2*l
                    else:
                        print("No more space")
            except:
                messagebox.showerror("ERROR","Invalid input")
        elif op == "Dequeue":
            try:
                print("Tamanho da fila: ",self.queue.size())
                pos = self.queue.dequeue()
                pos.delete_rect()
                self.paint()
                self.y-=2*l
            except:
                messagebox.showerror("ERROR","Cannot remove from empty queue")
    def get_opt(self):
        return self.option.get()
    def get_value(self):
        aux = self.opt_text.get().split(",")
        return [int(i) for i in aux]
        
            
class FrameFila(tk.Frame):
    def __init__(self):
        super().__init__()
        self.tela = tk.Canvas(self,bg = "white", width = 600, height = 700)
        self.opt = Options(self,self.tela)
        self.tela.update()
        self.tela.grid(sticky = tk.W,row=0,column=1)
        self.opt.grid(sticky=tk.W,row = 0,column = 0)
class Fila(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Queue")
        self.geometry("800x800")
        self.app = FrameFila()
        self.app.pack()
            
            

fila = Fila()
fila.mainloop()
        
