import tkinter as tk
from tkinter import ttk
import requests

def update_api_data():
    # Substitua 'URL_DA_API' pela URL real da API e 'SEU_TOKEN' pelo token Bearer correto
    url = 'http://localhost:8080/api/kaggle/v1/products/alterFull/{id}'
    headers = {'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJwaXp6dXJnLWFwaSIsImlhdCI6MTY5OTkyMzgwNiwiZXhwIjoxNjk5OTM4MjA2LCJzdWIiOiJ0ZXN0ZUBlbWFpbC5jb20ifQ.2bYPCz-DyvU98aovPLb851k1lvBwIE61NJOokgFuaTQ'}

    new_data = {
        'campo1': novo_campo1.get(),
        'campo2': novo_campo2.get(),
        'campo3': novo_campo3.get()
    }  # Substitua pelos campos e valores que deseja alterar na API

    response = requests.put(url, headers=headers, json=new_data)

    if response.status_code == 200:
        print("Dados atualizados com sucesso!")
    else:
        print("Falha ao atualizar os dados na API")

# Criar a janela
root = tk.Tk()
root.title("Atualizar Dados da API")

# Criar campos de entrada para os novos dados
novo_campo1 = tk.Entry(root)
novo_campo1_label = tk.Label(root, text="Novo Campo 1:")
novo_campo1_label.pack()
novo_campo1.pack()

novo_campo2 = tk.Entry(root)
novo_campo2_label = tk.Label(root, text="Novo Campo 2:")
novo_campo2_label.pack()
novo_campo2.pack()

novo_campo3 = tk.Entry(root)
novo_campo3_label = tk.Label(root, text="Novo Campo 3:")
novo_campo3_label.pack()
novo_campo3.pack()

# Botão para atualizar os dados na API
update_data_button = tk.Button(root, text="Atualizar Dados na API", command=update_api_data)
update_data_button.pack()

# Executar a interface
root.mainloop()
