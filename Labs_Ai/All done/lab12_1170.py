from tkinter import *
class MenuDemo:
    def __init__(self):
        self.window=Tk()
        self.window.title("Menu Demo")
        menubar=Menu(self.window)
        self.window.config(menu=menubar)
        operationMenu=Menu(menubar,tearoff=0)
        menubar.add_cascade(label="Operation",menu=operationMenu)
        operationMenu.add_command(label="Add",command=self.add)
        operationMenu.add_command(label="Subtract",command=self.subtract)
        operationMenu.add_separator()
        operationMenu.add_command(label="Multiply",command=self.multiply)
        operationMenu.add_command(label="Divide",command=self.divide)
        exitMenu=Menu(menubar,tearoff=0)
        menubar.add_cascade(label="Exit",menu=exitMenu)
        exitMenu.add_command(label="Quit",command=self.window.quit)
        self.frame1=Frame(self.window)
        self.frame1.grid(row=1,column=1,pady=10)
        Label(self.frame1,text="Number 1:").pack(side=LEFT)
        self.v1=StringVar()
        Entry(self.frame1,width=5,textvariable=self.v1,justify=RIGHT).pack(side=LEFT)
        Label(self.frame1,text="Number 2:").pack(side=LEFT)
        self.v2=StringVar()
        Entry(self.frame1,width=5,textvariable=self.v2,justify=RIGHT).pack(side=LEFT)
        Label(self.frame1,text="Result:").pack(side=LEFT)
        self.v3=StringVar()
        Entry(self.frame1,width=5,textvariable=self.v3,justify=RIGHT).pack(side=LEFT)
    def add(self):
        self.v3.set(float(self.v1.get())+float(self.v2.get()))
    def subtract(self):
        self.v3.set(float(self.v1.get())-float(self.v2.get()))  
    def multiply(self):
        self.v3.set(float(self.v1.get())*float(self.v2.get()))
    def divide(self):
        self.v3.set(float(self.v1.get())/float(self.v2.get()))

MenuDemo()
mainloop()
# from tkinter import *
# window=Tk()
# canvas=Canvas(window,bg="white",width=200,height=200)
# canvas.pack()
# def mousePressed(event):
#     canvas.create_text(event.x,event.y,fill="red",text="Hello")
# canvas.bind("<Button-1>", mousePressed)
# window.mainloop()