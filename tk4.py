from tkinter import *

def max():
    no = int(txtno.get())
    no2 = int(txtno2.get())
    if no > no2:
        strans.set(str(no))
    else:
        strans.set(str(no2))
    

root = Tk()
root.title("add")
root.geometry("400x300")

strans = StringVar(root)

lblno = Label(root,text="Number1",font=("Arial",16))
lblno.grid(row=0,column=0)

txtno = Entry(root)
txtno.grid(row=0,column=1)

lblno2 = Label(root,text="Number2",font=("Arial",16))
lblno2.grid(row=1,column=0)

txtno2 = Entry(root)
txtno2.grid(row=1,column=1)

bnt = Button(root,text="max",command=max)
bnt.grid(row=2,column=0)

lblno3 = Label(root,text="Answer",font=("Arial",16))
lblno3.grid(row=3,column=0)

txtno3 = Entry(root,textvariable=strans)
txtno3.grid(row=3,column=1)


root.mainloop()