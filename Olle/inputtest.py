from Tkinter import *
master = Tk()

Label(master, text="Input:").grid(row=0, sticky=W)

e1 = Entry(master)
e1.grid(row=0, column=1)

# Get the content of the e1 entry
content = e1.get()

# But if that's right, why doesn't this work?
print content

mainloop()
