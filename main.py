from ast import Lambda
from cProfile import label
from cgitb import text
from ctypes import alignment
from distutils.cmd import Command
from importlib.machinery import WindowsRegistryFinder
from tkinter import *
from tkinter import messagebox
root=Tk()
root.title("Tic Tac Toe")
k=PhotoImage(file="icon ttt.png")
root.iconphoto(True,k)
root.geometry("235x300")
clicked=True
count=0
def b_click(b):
    global clicked,count
    if b["text"]==" " and clicked==True:
        b["text"]="X"
        clicked=False
        count+=1
        checkwin()
    elif b["text"]==" " and clicked==False:
        b["text"]='O'
        clicked=True
        count+=1
        checkwin()
    else:
        messagebox.showerror("Tic Tac Toe","this box is already filled ")
def disable_all_button():
    b1.config(state=DISABLED)
    b2.config(state=DISABLED)
    b3.config(state=DISABLED)
    b4.config(state=DISABLED)
    b5.config(state=DISABLED)
    b6.config(state=DISABLED)
    b7.config(state=DISABLED)
    b8.config(state=DISABLED)
    b9.config(state=DISABLED)
def checkwin():
    global Winner 
    winner=False
    if ( b1["text"]=="X" and b2["text"]=="X" and b3["text"]=="X"):
        b1.config(bg="red")
        b2.config(bg="red")
        b3.config(bg="red")
        winner=True
        messagebox.showinfo("Tic Tac Toe","Congratulations X you win")
        disable_all_button()
    elif (b4["text"]=="X" and b5["text"]=="X" and b6["text"]=="X") :
        b4.config(bg="red")
        b5.config(bg="red")
        b6.config(bg="red")
        winner=True
        messagebox.showinfo("Tic Tac Toe","Congratulations X you win")
        disable_all_button()
    elif (b7["text"]=="X" and b8["text"]=="X" and b9["text"]=="X"):
        b7.config(bg="red")
        b8.config(bg="red")
        b9.config(bg="red")
        winner=True 
        messagebox.showinfo("Tic Tac Toe","Congratulations X you win")
        disable_all_button()
    elif (b1["text"]=="X" and b4["text"]=="X" and b7["text"]=="X") :
        b1.config(bg="red")
        b4.config(bg="red")
        b7.config(bg="red")
        winner=True
        messagebox.showinfo("Tic Tac Toe","Congratulations X you win")
        disable_all_button()
    elif (b2["text"]=="X" and b5["text"]=="X" and b8["text"]=="X") :
        b5.config(bg="red")
        b2.config(bg="red")
        b8.config(bg="red")
        winner=True
        messagebox.showinfo("Tic Tac Toe","Congratulations X you win")
        disable_all_button() 
    elif (b3["text"]=="X" and b6["text"]=="X" and b9["text"]=="X") :
        b9.config(bg="red")
        b6.config(bg="red")
        b3.config(bg="red")
        winner=True 
        messagebox.showinfo("Tic Tac Toe","Congratulations X you win")
        disable_all_button()
    elif (b1["text"]=="X" and b5["text"]=="X" and b9["text"]=="X") :
        b1.config(bg="red")
        b5.config(bg="red")
        b9.config(bg="red")
        winner=True 
        messagebox.showinfo("Tic Tac Toe","Congratulations X you win")
        disable_all_button()
    elif (b3["text"]=="X" and b5["text"]=="X" and b7["text"]=="X"):
        b7.config(bg="red")
        b5.config(bg="red")
        b3.config(bg="red")
        winner=True
        messagebox.showinfo("Tic Tac Toe","Congratulations X you win")
        disable_all_button()
    elif ( b1["text"]=="O" and b2["text"]=="O" and b3["text"]=="O") :
        b1.config(bg="red")
        b2.config(bg="red")
        b3.config(bg="red")
        winner=False
        messagebox.showinfo("Tic Tac Toe","Congratulations O you win")
        disable_all_button()
    elif (b4["text"]=="O" and b5["text"]=="O" and b6["text"]=="O") :
        b4.config(bg="red")
        b5.config(bg="red")
        b6.config(bg="red")
        winner=False
        messagebox.showinfo("Tic Tac Toe","Congratulations O you win")
        disable_all_button()
    elif (b7["text"]=="O" and b8["text"]=="O" and b9["text"]=="O") :
        b7.config(bg="red")
        b8.config(bg="red")
        b9.config(bg="red")
        winner=False
        messagebox.showinfo("Tic Tac Toe","Congratulations O you win")
        disable_all_button()
    elif (b1["text"]=="O" and b4["text"]=="O" and b7["text"]=="O") :
        b1.config(bg="red")
        b4.config(bg="red")
        b7.config(bg="red")
        winner=False 
        messagebox.showinfo("Tic Tac Toe","Congratulations O you win")
        disable_all_button()
    elif (b2["text"]=="O" and b5["text"]=="O" and b8["text"]=="O") :
        b5.config(bg="red")
        b2.config(bg="red")
        b8.config(bg="red")
        winner=False
        messagebox.showinfo("Tic Tac Toe","Congratulations O you win") 
        disable_all_button()
    elif (b3["text"]=="O" and b6["text"]=="O" and b9["text"]=="O") :
        b6.config(bg="red")
        b9.config(bg="red")
        b3.config(bg="red")
        winner=False 
        messagebox.showinfo("Tic Tac Toe","Congratulations O you win")
        disable_all_button()
    elif (b1["text"]=="O" and b5["text"]=="O" and b9["text"]=="O") :
        b1.config(bg="red")
        b5.config(bg="red")
        b9.config(bg="red")
        winner=False 
        messagebox.showinfo("Tic Tac Toe","Congratulations O you win")
        disable_all_button()
    elif (b3["text"]=="O" and b5["text"]=="O" and b7["text"]=="O"):
        b3.config(bg="red")
        b5.config(bg="red")
        b7.config(bg="red")
        winner=False
        messagebox.showinfo("Tic Tac Toe","Congratulations O you win")
        disable_all_button()
    elif winner==False and count==9:
        messagebox.showinfo("Tic Tac Toe","no one wins play again")

b1=Button(root,text=" ",height=6,width=10,bg="SystemButtonFace",command=lambda: b_click(b1))
b2=Button(root,text=" ",height=6,width=10,bg="SystemButtonFace",command=lambda: b_click(b2))
b3=Button(root,text=" ",height=6,width=10,bg="SystemButtonFace",command=lambda: b_click(b3))
b4=Button(root,text=" ",height=6,width=10,bg="SystemButtonFace",command=lambda: b_click(b4))
b5=Button(root,text=" ",height=6,width=10,bg="SystemButtonFace",command=lambda: b_click(b5))
b6=Button(root,text=" ",height=6,width=10,bg="SystemButtonFace",command=lambda: b_click(b6))
b7=Button(root,text=" ",height=6,width=10,bg="SystemButtonFace",command=lambda: b_click(b7))
b8=Button(root,text=" ",height=6,width=10,bg="SystemButtonFace",command=lambda: b_click(b8))
b9=Button(root,text=" ",height=6,width=10,bg="SystemButtonFace",command=lambda: b_click(b9))

b1.grid(row=0,column=0)
b2.grid(row=0,column=1)
b3.grid(row=0,column=2)

b4.grid(row=1,column=0)
b5.grid(row=1,column=1)
b6.grid(row=1,column=2)

b7.grid(row=2,column=0)
b8.grid(row=2,column=1)
b9.grid(row=2,column=2)
root.mainloop()