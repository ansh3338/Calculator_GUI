from tkinter import *
import math

# function for calculating 
def click(e):
    text=e.widget.cget("text")
    # print(text)

    # calculation of [+ , - , * , / , % ] operations 
    if text == "=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            try:
                value = eval(e1.get())
            except Exception as a:
                # print(a)
                value = "Error"

        scvalue.set(value)
        e1.update()

# calculation of additive inverse of number
    elif text == "+/-":
        if scvalue.get().isdigit():
            value = 0 - int(scvalue.get())
        else:
            try:
                value = 0 - eval(e1.get())
            except Exception as a:
                # print(a)
                value = "Error"

        scvalue.set(value)
        e1.update()

# calculation of multiplicative inverse of number
    elif text == '1/x':
        if scvalue.get().isdigit():
            value = 1/(int(scvalue.get()))
        else:
            try:
                value = 1/(eval(e1.get()))
            except Exception as a:
                # print(a)
                value = "Error"

        scvalue.set(value)
        e1.update()

# calculation of square of number 
    elif text == 'x²':
        if scvalue.get().isdigit():
            value = (int(scvalue.get())) ** 2
        else:
            try:
                value = (eval(e1.get())) ** 2
            except Exception as a:
                # print(a)
                value = "Error"

        scvalue.set(value)
        e1.update()

# calculation of square root 
    elif text == '√x':
        if scvalue.get().isdigit():
            value = math.sqrt(int(scvalue.get()))
        else:
            try:
                value = math.sqrt(eval(e1.get()))
            except Exception as a:
                # print(a)
                value = "Error"

        scvalue.set(value)
        e1.update()

# backspace button 
    elif text == '<-':

        yo = len(scvalue.get())
        str = ""
        for i in range(yo-1):
            str = str + scvalue.get()[i]
        scvalue.set(str)


        e1.update()


    elif text == "c":
        scvalue.set("")
        e1.update()
    else:
        scvalue.set(scvalue.get() + text)
        e1.update()


ansh = Tk()

# defination of screen size 
ansh.geometry("400x390")
# limiting size of box 
ansh.maxsize(width=400, height=390)
ansh.configure(bg="lightgreen")
ansh.title("Calculator")

scvalue = StringVar()
scvalue.set("")

# construction of box on number is to be displayed in calculator 
e1 = Entry(ansh,textvar = scvalue,width=18,bd=3,font="default 30")
e1.place(x=0,y=0)

# Construction of various buttons of calculator 

b = Button(ansh,bg="#EE82EE",text="%",width=13,font="default 9 bold",height=3)
b.place(x=0,y=53)
b.bind("<Button-1>",click)
b = Button(ansh,bg="#EE82EE",text="c",width=13,font="default 9 bold",height=3)
b.place(x=100,y=53)
b.bind("<Button-1>",click)
b = Button(ansh,bg="#EE82EE",text="c",width=13,font="default 9 bold",height=3)
b.place(x=200,y=53)
b.bind("<Button-1>",click)
b = Button(ansh,bg="skyblue",text="<-",width=13,font="default 9 bold",height=3)
b.place(x=300,y=53)
b.bind("<Button-1>",click)

b = Button(ansh,bg="#EE82EE",text="1/x",width=13,font="default 9 bold",height=3)
b.place(x=0,y=109)
b.bind("<Button-1>",click)
b = Button(ansh,bg="#EE82EE",text="x²",width=13,font="default 9 bold",height=3)
b.place(x=100,y=109)
b.bind("<Button-1>",click)
b = Button(ansh,bg="#EE82EE",text="√x",width=13,font="default 9 bold",height=3)
b.place(x=200,y=109)
b.bind("<Button-1>",click)
b = Button(ansh,bg="yellow",text="/",width=13,font="default 9 bold",height=3)
b.place(x=300,y=109)
b.bind("<Button-1>",click)

b = Button(ansh,bg="#DCD0FF",text="7",width=13,font="default 9 bold",height=3)
b.place(x=0,y=165)
b.bind("<Button-1>",click)
b = Button(ansh,bg="#DCD0FF",text="8",width=13,font="default 9 bold",height=3)
b.place(x=100,y=165)
b.bind("<Button-1>",click)
b = Button(ansh,bg="#DCD0FF",text="9",width=13,font="default 9 bold",height=3)
b.place(x=200,y=165)
b.bind("<Button-1>",click)
b = Button(ansh,bg="yellow",text="*",width=13,font="default 9 bold",height=3)
b.place(x=300,y=165)
b.bind("<Button-1>",click)

b = Button(ansh,bg="#DCD0FF",text="4", font="default 9 bold",width=13,height=3)
b.place(x=0,y=221)
b.bind("<Button-1>",click)
b = Button(ansh,bg="#DCD0FF",text="5",width=13,font="default 9 bold",height=3)
b.place(x=100,y=221)
b.bind("<Button-1>",click)
b = Button(ansh,bg="#DCD0FF",text="6",width=13,font="default 9 bold",height=3)
b.place(x=200,y=221)
b.bind("<Button-1>",click)
b = Button(ansh,bg="yellow",text="-",width=13,font="default 9 bold",height=3)
b.place(x=300,y=221)
b.bind("<Button-1>",click)

b = Button(ansh,bg="#DCD0FF",text="1",width=13,font="default 9 bold",height=3)
b.place(x=0,y=277)
b.bind("<Button-1>",click)
b = Button(ansh,bg="#DCD0FF",text="2",width=13,font="default 9 bold",height=3)
b.place(x=100,y=277)
b.bind("<Button-1>",click)
b = Button(ansh,bg="#DCD0FF",text="3",width=13,font="default 9 bold",height=3)
b.place(x=200,y=277)
b.bind("<Button-1>",click)
b = Button(ansh,bg="yellow",text="+",width=13,font="default 9 bold",height=3)
b.place(x=300,y=277)
b.bind("<Button-1>",click)

b = Button(ansh,bg="#FFDAB9",text="+/-",width=13,font="default 9 bold",height=3)
b.place(x=0,y=333)
b.bind("<Button-1>",click)
b = Button(ansh,bg="#DCD0FF",text="0",width=13,font="default 9 bold",height=3)
b.place(x=100,y=333)
b.bind("<Button-1>",click)
b = Button(ansh,bg="#FFDAB9",text=".",width=13,font="default 9 bold",height=3)
b.place(x=200,y=333)
b.bind("<Button-1>",click)
b = Button(ansh,bg="lightgreen",text="=",width=13,font="default 9 bold",height=3)
b.place(x=300,y=333)
b.bind("<Button-1>",click)


# piece of code to load calculator GUI window 
ansh.mainloop()