
import tkinter as tk
import conn




def login():
    email = email_entry.get()
    senha = senha_entry.get()
    # Aqui você pode adicionar lógica para verificar o login
    print("Login - Email:", email, "Senha:", senha)

def cadastrar():
    email = email_entry.get()
    senha = senha_entry.get()
    # Aqui você pode adicionar lógica para o cadastro do usuário
    print("Cadastro - Email:", email, "Senha:", senha)

# Criando a janela
root = tk.Tk()
root.title("Login e Cadastro")

# Criando os campos de texto
email_label = tk.Label(root, text="E-mail:")
email_label.pack()
email_entry = tk.Entry(root)
email_entry.pack()

senha_label = tk.Label(root, text="Senha:")
senha_label.pack()
senha_entry = tk.Entry(root, show="*")  # A opção show="*" mascara a senha
senha_entry.pack()

# Criando os botões
login_button = tk.Button(root, text="Login", command=login)
login_button.pack()

cadastro_button = tk.Button(root, text="Cadastro", command=cadastrar)
cadastro_button.pack()

# Executando a interface
root.mainloop()