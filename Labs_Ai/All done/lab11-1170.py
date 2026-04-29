#!Question 4
# from tkinter import *
# from tkinter import messagebox

# from matplotlib.pyplot import grid  
# def processOK():
#     messagebox.showinfo("Message", "You clicked OK")
# def processCancel():
#     messagebox.showinfo("Message", "You clicked Cancel")
# window = Tk()
# window.geometry("300x200")
# window.title("Lab 11")
# Label_1 = Label(window, text="Python programming in window")
# Label_1.pack()
# b1=Button(window,text="OK",bg="Yellow",command=processOK).pack(side=TOP)
# b2=Button(window,text="Cancel",bg="Green",command=processCancel).pack(side=TOP)
# window.mainloop()
#!Question 2
# root=Tk()
# frame=Frame(root)
# frame.pack()
# bottomframe=Frame(root)
# bottomframe.pack(side=BOTTOM)
# redb1=Button(frame,text="Red",bg="Red").pack(side=LEFT),
# Greenb2=Button(frame,text="Yellow",bg="Yellow").pack(side=RIGHT),
# redb3=Button(frame,text="Green",bg="Green").pack(side=TOP),
# blueb1=Button(bottomframe,text="Blue",bg="Blue").pack(side=TOP),
# root.mainloop()
#!Question 3
# root=Tk()
# b=0
# for r in range(5):
#     for c in range(5):
#         btn=Button(root,text=str(b),width=5,height=2,bg="Black",fg="White",activebackground="Green",activeforeground="White",relief="raised")
#         btn.grid(row=r,column=c)
#         b=b+1
# root.mainloop()
#!Question 4
# top=Tk()
# L1=Label(top,text="Physics")
# L1.place(x=10,y=10)
# E1=Entry(top,bd=5).place(x=60,y=10)
# L2=Label(top,text="Mathematics").place(x=10,y=50)
# E2=Entry(top,bd=5).place(x=60,y=50)
# L3=Label(top,text="total").place(x=10,y=150)
# E3=Entry(top,bd=5).place(x=60,y=150)
# B1=Button(top,text="add").place(x=100,y=100)
# top.geometry("200x200")
# top.mainloop()