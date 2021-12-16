#from tkinter import *
from tkinter import *
from  kalah import Kalah
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
from functools import partial
import copy

def buttonPress():
    pass
def make_turn(position,arr):
    if k.player_turn:
        k.make_turn(position)
        update(arr)



    if not k.player_turn:
        print(sli1.get())
        k1 = copy.deepcopy(k)
        a, b, c = k1.minimax(sli1.get(), -40, 40, False)
        print(k.ai_board, "before")

        k.make_turn(c)
        print(k.ai_board)
        update(arr) 

def update(arr):
    temp = k.player_board+[k.player_kalah]+k.ai_board[::-1]+[k.ai_kalah]
    for i in range(len(temp)):
        arr[i].configure(text = temp[i]) 
        #return arr

# root window
k = Kalah()
root = tk.Tk()
root.geometry('330x200')
root.resizable(False, False)
root.title('Kalah game')

sli1 = Scale(root, from_=1, to=3, tickinterval=1, orient=HORIZONTAL)
sli1.place(x = 0, y = 5)
#sli1.pack()



arr= []
button = Button(root,text='3',command=partial(make_turn,0,arr), height= 2, width=4)
button.place(x = 45, y = 120)
arr.append(button)
button = Button(root,text='3',command=partial(make_turn,1,arr), height= 2, width=4)
button.place(x = 85, y = 120)
arr.append(button)
button = Button(root,text='3',command=partial(make_turn,2,arr), height= 2, width=4)
button.place(x = 125, y = 120)
arr.append(button)
button = Button(root,text='3',command=partial(make_turn,3,arr), height= 2, width=4)
button.place(x = 165, y = 120)
arr.append(button)
button = Button(root,text='3',command=partial(make_turn,4,arr), height= 2, width=4)
button.place(x = 205, y = 120)
arr.append(button)
button = Button(root,text='3',command=partial(make_turn,5,arr), height= 2, width=4)
button.place(x = 245, y = 120)
arr.append(button)

button = Button(root,text='0',command=buttonPress, height= 6, width=5)
button.place(x = 285, y = 60)
arr.append(button)

button = Button(root,text='3',command=buttonPress, height= 2, width=4)
button.place(x = 45, y = 60)
arr.append(button)
button = Button(root,text='3',command=buttonPress, height= 2, width=4)
button.place(x = 85, y = 60)
arr.append(button)
button = Button(root,text='3',command=buttonPress, height= 2, width=4)
button.place(x = 125, y = 60)
arr.append(button)
button = Button(root,text='3',command=buttonPress, height= 2, width=4)
button.place(x = 165, y = 60)
arr.append(button)
button = Button(root,text='3',command=buttonPress, height= 2, width=4)
button.place(x = 205, y = 60)
arr.append(button)
button = Button(root,text='3',command=buttonPress, height= 2, width=4)
button.place(x = 245, y = 60)
arr.append(button)

button = Button(root,text='0',command=buttonPress, height= 6, width=5)
button.place(x = 0, y = 60)
arr.append(button)

#arr[2].configure(text = "12") 
arr = update(arr)

root.mainloop()


#k.make_turn(2)

""" root = Tk() # create parent window
 
# use Button and Label widget to create a simple TV remote 
turn_on = Button(root, text="ON")
turn_on.pack()
 
turn_off = Button(root, text="OFF", command=root.quit)
turn_off.pack()
 
volume = Label(root, text="VOLUME")
volume.pack()
 
vol_up = Button(root, text="+")
vol_up.pack()
 
vol_down = Button(root, text="-")
vol_down.pack()
 
root.mainloop() """
