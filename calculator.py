from tkinter import *


def button1():
    e.insert(END,1)

def button2():
    e.insert(END,2)

def button3():
    e.insert(END,3)
    
def button4():   
    e.insert(END,4)
    
def button5():
    e.insert(END,5)
    
def button6():
    e.insert(END,6)
    
def button7():
    e.insert(END,7)
    
def button8():
    e.insert(END,8)
    
def button9():
    e.insert(END,9)
    
def button0():
    e.insert(END,0)
    
def button12():
    e.insert(END,'+')

def button11():
    e.insert(END,'-')

def button13():
    e.insert(END,'*')

def button14():
    e.insert(END,'/')

def button10():
    gibtgleich = e.get()
    npc = eval(gibtgleich)
    e.insert(END,'='+ str(npc))

def buttonc():
    e.delete(0,END)
    
root = Tk()
root.geometry('300x200')
root.title('calculator')
e = Entry(width=33)

b1 = Button(text="1", width=5, height= 1, command = button1)

b2 = Button(text="2", width=5, height= 1, command = button2)

b3 = Button(text="3", width=5, height= 1, command = button3)

b4 = Button(text="4", width=5, height= 1, command = button4)

b5 = Button(text="5", width=5, height= 1, command = button5)

b6 = Button(text="6", width=5, height= 1, command = button6)

b7 = Button(text="7", width=5, height= 1, command = button7)

b8 = Button(text="8", width=5, height= 1, command = button8)

b9 = Button(text="9", width=5, height= 1, command = button9)

b0 = Button(text="0", width=5, height= 1, command = button0)

bminus = Button(text="+", width=5, height= 1, command = button12)

bplus = Button(text="-", width=5, height= 1, command = button11)

bpluss = Button(text="=", width=5, height= 1, command = button10)

bplusss = Button(text="*", width=5, height= 1, command = button13)

bplussss = Button(text="/", width=5, height= 1, command = button14)
bc = Button(text="C", width=5, height= 1, command = buttonc)

e.place(x=50,y=25)

b1.place(x=50,y=50)
b3.place(x=150,y=50)
b2.place(x=100,y=50)
b4.place(x=50,y=75)
b5.place(x=100,y=75)
b6.place(x=150,y=75)
b7.place(x=50,y=100)
b8.place(x=100,y=100)
b9.place(x=150,y=100)
b0.place(x=100,y=125)

bminus.place(x=200,y=50)
bplus.place(x=200,y=75)
bpluss.place(x=150,y=125)
bplusss.place(x=200,y=100)
bplussss.place(x=200,y=125)
bc.place(x=50,y=125)
root.mainloop()
