from tkinter import *
from tkinter import messagebox
from tkinter import scrolledtext
from tkinter.ttk import Combobox
import re

def func(s, t, num):
    k = 0
    s2 = len(s) // 2
    s3 = len(s) // 3
    s4 = (len(s) * 2) // 3
    t4 = (len(t) * 3)//4
    if 12 > len(s[0:s2]) > 0 and len(t) > 0 and re.search('[a-z]', t[t4]) is None:
        if num == "*":
            k = (s[s3:s4].count('*'))
        if num == "&":
            k = (s[s3:s4].count('&'))
    else:
        k = -1
    return k

def clicked():
    res = func(inp1.get(), inp2.get(), combo.get())
    if res == -1:
        messagebox.showinfo('Ошибка', 'Введенные строчки не соответствуют условию задания.')
    else:
        restxt.delete('1.0', END)
        restxt.insert('1.0', res)

window = Tk()
window.title("Практическая работа №1")
window.geometry('400x160')
window.resizable(False, False)
window.configure(background='#a5a4a3')
f_inp = LabelFrame(window, text="Введите строки s, t соответственно")
f_inp.pack()
inp1 = Entry(f_inp, width=50)
inp1.pack()
inp2 = Entry(f_inp, width=50)
inp2.pack()
f_mid = Frame(window, width=50)
f_mid.pack()
combo = Combobox(f_mid, width=5, state="readonly")
combo['values'] = ("*", "&")
combo.current(0)
combo.pack()
btn = Button(f_mid, text="Посчитать количество указанных символов", command=clicked)
btn.pack()
f_text = Frame(window, width=50)
f_text.pack()
restxt = scrolledtext.ScrolledText(f_text, width=40, height=2)
restxt.insert('1.0', "Поле результата")
restxt.pack()
window.mainloop()