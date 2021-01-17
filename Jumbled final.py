import tkinter
from tkinter import *
import random
from tkinter import messagebox
from random import shuffle

answer = ["python", "coffee", "egypt", "chair", "study", "canada", "gallery"]
words = []
num = random.randint(0, len(words))

for i in answer:
    word = list(i)
    shuffle(word)
    words.append(word)

def initial():
    global words, num
    lb1.configure(text=words[num])

def ans_check():
    global words, answer, num
    user_input = e1.get()
    if user_input == answer[num]:
        messagebox.showinfo("Right", "Correct answer!")
        Reset()
    else:
        messagebox.showinfo("Sorry!", "Wrong answer.")
        e1.delete(0, END)

def Reset():
    global words, answer, num
    num = random.randint(0, len(words))
    lb1.configure(text=words[num])
    e1.delete(0, END)

root = tkinter.Tk()
root.geometry("400x400")

lb1 = Label(root, font='times 20')
lb1.pack(pady=30, ipady=10, ipadx=10)

answer12 = StringVar()  # Holds string
e1 = Entry(root, textvariable=answer)
e1.pack(ipadx=5, ipady=5)

button1 = Button(root, text="Check", width=20, fg="#6ab04c", command=ans_check)
button1.pack(pady=20)
button2 = Button(root, text="Reset", width=20, fg="#EA425C", command=Reset)
button2.pack()

initial()
root.mainloop()
