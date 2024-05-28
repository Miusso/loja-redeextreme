

from tkinter import *

def login():
    usuario = 'vinny'
    senha = '123'

    usu = input("Digite seu login: ")
    sen = input("Digite seu senha: ")

    if usu == usu and sen == senha:
        con["text"] = ()
        print("\nLogado com sucesso")
    else:
        print("Usuario ou senha errado! ")

menu = Tk()
menu.title("")
menu.geometry("300x300")

r = Label(menu, text="")
r.grid(padx=10, pady=10)

senha = Entry(menu, takefocus="1")

b = Button(menu, text="LOGIN", command=login)
r.grid(padx=60, pady=20)



con = Label(menu, text="")
b.grid(column=2, row=2)


menu.mainloop()