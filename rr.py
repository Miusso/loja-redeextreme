import tkinter as tk

def login():
    loginp = entry_username.get()
    password = entry_password.get()

    # Verifica se o usuário e a senha estão corretos (neste exemplo, são 'admin' e 'senha')
    if username == 'admin' and password == 'senha':
        lbl_result.config(text="Login bem-sucedido!", fg="green")
    else:
        lbl_result.config(text="Nome de usuário ou senha incorretos", fg="red")

# Cria uma janela
root = tk.Tk()
root.title("")

# Widgets

login = tk.Label(root, text= "LOGIN!")
login.grid(row=0, column=1, padx=10, pady=10, sticky=tk.W)

lbl_username = tk.Label(root, text="Nome de Usuário:")
lbl_username.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)

entry_username = tk.Entry(root)
entry_username.grid(row=1, column=1, padx=10, pady=5)

lbl_password = tk.Label(root, text="Senha:")
lbl_password.grid(row=2, column=0, padx=10, pady=5, sticky=tk.W)

entry_password = tk.Entry(root, show="*")
entry_password.grid(row=2, column=1, padx=10, pady=5)

btn_login = tk.Button(root, text="Login", command=login)
btn_login.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

lbl_result = tk.Label(root, text="", fg="black")
lbl_result.grid(row=4, column=0, columnspan=2)

# Loop principal
root.mainloop()