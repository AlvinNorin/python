from Tkinter import *

## Create Window/GUI

master = Tk()

master.title("My first Application!")
master.configure(bg='white')

## Define "CloseWindow" = "Exit"

def closewindow():
	exit()


## Text field/Label num.1

label = Label(master, text="Hallo, this is my first GUI based application!", bg="white")
label.pack()


## Button num.1

button = Button(master, text="Exemple Button!", borderwidth=.010)
button.pack()


## Button num.2

button2 = Button(master, text="Close Window", command=closewindow, bg="red")
button2.pack()


master.geometry("360x200")


mainloop()


