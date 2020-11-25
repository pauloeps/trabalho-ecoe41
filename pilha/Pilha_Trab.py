import tkinter as tk
from tkinter import messagebox
#variável para controlar o tamanho do bloco da pilha
l = 20
#Classe que desenha o bloco da pilha
class Draw_Rect:
    def __init__(self,canvas,y,value,larg,alt):
        self.y = y
        self.canvas = canvas
        self.start = -40
        self.end = 0
        self.text_pos = (self.start + self.end)/2
        self.value = value   
        self.rect_draw = self.canvas.create_rectangle(larg-l,self.start,larg+l,self.end,outline = "blue",tag = 'elem')
        self.rect_text = self.canvas.create_text((larg,self.text_pos),text = value,font=("Courier", 18),tag = 'elem')
    def delete_rect(self):
        self.canvas.delete(self.rect_draw,self.rect_text)
    def appear(self,_start,speed,isPop = False): #Animação de subida na Pilha
        self.canvas.update()
        if (self.start <= _start) or isPop: #_start e _end são as posições que já sabemos onde os blocos ficarão
            if not isPop:
                aux = 1
            else:
                aux = -1
            self.start = self.start + (aux)*speed
            self.text_pos = self.text_pos + (aux)*speed
            self.canvas.move(self.rect_draw, 0 , (aux*speed))
            self.canvas.move(self.rect_text, 0 , (aux*speed))
            temp = self.canvas.after(10,self.appear, _start, speed,isPop)
        elif (self.start > _start): #caso ocorra de passar a posição definida
            speed = self.start - _start
            self.start -= speed
            #self.end += speed
            self.text_pos -= speed
            self.canvas.move(self.rect_draw, 0 , speed)
            self.canvas.move(self.rect_text, 0 , speed)
        if self.start <= 30 and isPop:
            self.delete_rect()
            print('oi')
            self.canvas.after_cancel(temp)
            

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
        
     def elem(self,pos):
         return self.items[pos]

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
        self.lista = list()
    def show_top(self):
        if not self.stack.isEmpty():
            self.canvas.itemconfig(self.stack.peek().rect_draw, outline = "red")
    def hide_top(self):
        if not self.stack.isEmpty():
            self.canvas.itemconfig(self.stack.peek().rect_draw, outline = "blue")
    def paint(self,*args):
        if self.option.get() == "Pop":
            self.canvas.itemconfig(self.canvas.info, text = "Remove Top\nSize:%d"%self.stack.size())
            self.show_top()
        elif self.option.get() == "New Stack":
            self.canvas.itemconfig(self.canvas.info, text = "Stack created\nSize:%s"%self.stack.size())
            self.hide_top()
        elif self.option.get() == "Push":
            self.canvas.itemconfig(self.canvas.info, text = "Inserting items\nSize:%d"%self.stack.size())
            self.hide_top()
    def do_action(self,event):
        op = self.get_opt()
        print("Operação : ",op)
        if op == "New Stack":
            if messagebox.askokcancel("Create new stack","This will delete the actual stack"):
                self.canvas.delete("elem")
                self.stack = Stack()
                self.paint()
                self.y = 0
        elif op == "Push" :
            try:
                if (self.y+40) < (self.alt):
                    self.lista += self.get_value()
                self.create_box()
            except:
                messagebox.showerror("ERROR","Invalid input")
        elif op == "Pop":
            try:
                print("Tamanho da pilha: ",self.stack.size())
                pos = self.stack.pop()
                pos.appear(-40,10,True)
                self.paint()
                self.y+=2*l
            except:
                messagebox.showerror("ERROR","Cannot remove from empty stack")
        self.opt_text.delete(0,"end")
    def get_opt(self):
        return self.option.get()
    def get_value(self):
        aux = self.opt_text.get().split(",")
        return [int(i) for i in aux]
    def create_box(self):
        if (self.y+40) < (self.alt) and len(self.lista) > 0:
            yi_pos = self.alt-10-2*l+self.y
            #yf_pos = 10+2*l+self.y
            rect = Draw_Rect(self.canvas,self.y,self.lista[0],self.larg,self.alt)
            self.stack.push(rect)
            rect.appear(yi_pos,10)
            self.paint()
            print("Tamanho da pilha : " ,self.stack.size())
            self.y-=2*l
            self.lista.pop(0)
            self.canvas.after(1000,self.create_box)
        else:
            print("No more space")
        
            
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
        self.title("Stack")
        self.geometry("800x800")
        self.app = FramePilha()
        self.app.pack()
            
            

pilha=Pilha()
pilha.mainloop()
        
