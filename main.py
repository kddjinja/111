from tkinter import *
from playsound import playsound
import random
from tkinter import messagebox, Label
from tkinter.ttk import *


def Slide():
    import time
    Progress_Bar['value'] = 25
    window.update_idletasks()
    time.sleep(1)
    Progress_Bar['value'] = 50
    window.update_idletasks()
    time.sleep(1)
    Progress_Bar['value'] = 75
    window.update_idletasks()
    time.sleep(1)
    Progress_Bar['value'] = 100


def play():
    playsound(
        '8-Bit_Universe_-_Numb_73206306.mp3')  # здесь название звукового файла, его обязательно в папку, где лежит код


def clicked():
    symbols = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
               'm', 'n', 'o', 'p', 'q', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    res = txt.get()
    if (len(res) != 3):
        messagebox.showinfo(title='Ошибка!', message='Введите 3 символа!')
    elif (((str(res))[0] not in number) or ((str(res))[1] not in number)
          or ((str(res))[2] not in number)):
        messagebox.showinfo(title='Ошибка!', message='Формат ввода не соответствует требованиям')
    else:
        code = ''
        for i in range(5):
            code += symbols[random.randint(0, len(symbols) - 1)]
        code += '-'
        # XXXXX-XXXX-XXX-XX
        code += code[0:4]
        for i in range(6, 10):
            if (symbols.index(code[i]) + res[0])<len(symbols):
                code[i] = symbols[symbols.index(code[i]) + res[0]]
            else:
                code[i] = symbols[(symbols.index(code[i]) + res[0])-len(symbols)]
        code += '-'
        code += code[7:10]
        for i in range(11, 14):
            if (symbols.index(code[i]) - res[1]) < 0:
                code[i] = symbols[symbols.index(code[i]) - res[1]]
            else:
                code[i] = symbols[(symbols.index(code[i]) - res[1]) + len(symbols)]
        code += '-'
        code += code[11:13]
        for i in range(15, 17):
            if (symbols.index(code[i]) + res[2]) < len(symbols):
                code[i] = symbols[symbols.index(code[i]) + res[2]]
            else:
                code[i] = symbols[(symbols.index(code[i]) + res[2]) - len(symbols)]
        Slide()

        play()
        messagebox.showinfo(title='Ключ: ', message=code)


window = Tk()
window.title("Key Making")
window.geometry('700x352')
window.image = PhotoImage(file='pic.gif')  # название картинки, ее обязательно в папку, где лежит код
bg_logo: Label = Label(window, image=window.image)
bg_logo.grid(row=0, column=0)

lbl = Label(window, text='Введите 3-значное число ')
lbl.place(relx=.5, rely=.1, anchor="c")

txt = Entry(window, width=10)
txt.grid(column=1, row=0)
txt.place(relx=.5, rely=.2, anchor="c")
Progress_Bar = Progressbar(window, orient=HORIZONTAL, length=250, mode='determinate')
Progress_Bar.place(relx=.5, rely=.2, anchor="c")
Progress_Bar.grid(row=0, column=0)

btn = Button(window, text="Сгенерировать ключ", command=clicked)
btn.place(relx=.5, rely=.7, anchor="c")

window.mainloop()
