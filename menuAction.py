import tkinter

def add_button(x,y,txt,cmd):
	run_button = tkinter.Button(root, text = txt, command = print("-----"))
	run_button.place(x = x, y = y)