import tkinter as tk
from tkinter import ttk
# tk._test()

def greet():
    print("Hello world")

root = tk.Tk()
root.title("hello")

# greet_button = ttk.button(first argument is the element you want this element to be put inside, text="the stuff that should be inside the button"
# ,command=greet ... basically a higher order function that will run when this button is clicked)

greet_button = ttk.Button(root,text="hello world",command=greet)
greet_button.pack(side = "left",fill="x",expand=True)

quit_button = ttk.Button(root,text="quit",command=root.destroy)
quit_button.pack(side = "left",fill="x",expand=True)

user_name = tk.StringVar()
name_lable = ttk.Label(root,text="Name: ") 
name_lable.pack(side="left",padx = (0,10))

name_entry = ttk.Entry(root,width = 15, textvariable = user_name)
name_entry.pack(side="left")
name_entry.focus()

def printer_fn():
    print(user_name.get())

printer_button = ttk.Button(root,text="Print name",command=printer_fn)
printer_button.pack(side = "left",fill="x",expand=True)

root.mainloop()


greet()


