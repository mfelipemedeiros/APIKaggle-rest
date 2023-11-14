import tkinter as tk
from tkinter import ttk
import requests

def get_api_data():
    # Substitua 'URL_DA_API' pela URL real da API e 'SEU_TOKEN' pelo token Bearer correto
    url = 'http://localhost:8080/api/kaggle/v1/products'
    headers = {'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJwaXp6dXJnLWFwaSIsImlhdCI6MTY5OTkyMzgwNiwiZXhwIjoxNjk5OTM4MjA2LCJzdWIiOiJ0ZXN0ZUBlbWFpbC5jb20ifQ.2bYPCz-DyvU98aovPLb851k1lvBwIE61NJOokgFuaTQ'}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        fill_table(data)
    else:
        print("Falha ao obter dados da API")

def fill_table(data):
    # Limpar qualquer dado existente na tabela
    for row in treeview.get_children():
        treeview.delete(row)
    
    # Preencher a tabela com os dados da API
    for item in data:
        treeview.insert('', 'end', values=(item[''], item['product_name'], item['sale_price']))  # Substitua 'campoX' pelos campos reais da API

# Criar a janela
root = tk.Tk()
root.title("Dados da API")

# Criar a tabela
treeview = ttk.Treeview(root, columns=('id', 'nome do produto', 'preço'))  # Substitua pelos nomes reais dos campos
treeview.heading('#0', text='id')
treeview.heading('id', text='nome do produto')
treeview.heading('nome do produto', text='preço')
treeview.heading('preço', text='Campo 3')
treeview.pack()

# Botão para obter dados da API
get_data_button = tk.Button(root, text="Obter Dados da API", command=get_api_data)
get_data_button.pack()

# Executar a interface
root.mainloop()