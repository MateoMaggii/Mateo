from tkinter import font, messagebox
from tkinter import *
import random

def obvio():
    messagebox.showinfo(message="Es una cita, te espero el 4 de mayo jiji", title="")
def button_hover(event):
    x = random.randint(10, 400)
    y = random.randint(10, 400)
    my_button_2.place(x=x, y=y)
def exit_(event):
    x = random.randint(10, 400)
    y = random.randint(10, 400)
    my_button_2.place(x=x, y=y)
root = Tk()
root.geometry("600x400")
root.iconbitmap('C:Downloads/299063_heart_icon.ico')
root.configure(background='#FFC7FA')
root.title('Invitacion para el cine')


label_0 = Label(root, text="Queres ir al cine conmigo?", bg='#FFC7FA',fg='black', width=0, font=("BubbleGum", 30))
label_0.place(x=90, y=60)

my_button_1 = Button(root, text="SI", width=5, height=1, font=("Bubblegum", 30), bg='#FF4141', fg='white', command=obvio)
my_button_1.place(x=100, y=220)

my_button_2 = Button(root, text="NO", width=5, height=1, font=("BubbleGum", 30),bg='#FF4141', fg='white')
my_button_2.place(x=350, y=220)

my_button_2.bind("<Enter>", button_hover)
my_button_2.bind("<Leave>", exit_)

root.mainloop()