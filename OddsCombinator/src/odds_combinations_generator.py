import pandas as pd
import tkinter as tk
from tkinter import ttk

# Definir a função que gera as combinações de odds
def gerar_combinacoes():
    # Obter os valores de entrada dos campos de texto e convertê-los em floats
    odds_values = [[float(e.get()) for e in row] for row in odds_entries]

    # Inicializar uma lista vazia para armazenar as combinações
    combinacoes = []

    # Percorrer cada conjunto de odds na lista de entrada
    for i in range(len(odds_values)):
        # Extrair os valores de Time 1, Empate e Time 2
        time1 = odds_values[i][0]
        empate = odds_values[i][1]
        time2 = odds_values[i][2]
        # Percorrer os outros conjuntos de odds na lista de entrada
        for j in range(len(odds_values)):
            # Verificar se o índice é diferente do atual
            if j != i:
                # Extrair os valores de Time 1, Empate e Time 2
                time1_2 = odds_values[j][0]
                empate_2 = odds_values[j][1]
                time2_2 = odds_values[j][2]
                # Percorrer os outros conjuntos de odds na lista de entrada
                for k in range(len(odds_values)):
                    # Verificar se o índice é diferente dos anteriores
                    if k != i and k != j:
                        # Extrair os valores de Time 1, Empate e Time 2
                        time1_3 = odds_values[k][0]
                        empate_3 = odds_values[k][1]
                        time2_3 = odds_values[k][2]
                        # Criar uma lista com uma combinação de odds
                        combinacao = [time1, empate_2, time2_3]
                        # Calcular a odd total da combinação
                        odd_total = round(time1 * empate_2 * time2_3, 2)
                        # Adicionar a odd total à lista da combinação
                        combinacao.append(odd_total)
                        # Adicionar a lista da combinação à lista de combinações
                        combinacoes.append(combinacao)
    # Retornar a lista de combinações
    return combinacoes

# Definir a função para criar a interface gráfica
def criar_interface():
    root = tk.Tk()
    root.title("Gerador de Combinações de Odds")

    # Criar uma lista para armazenar os campos de entrada de odds
    global odds_entries
    odds_entries = []

    # Adicionar campos de entrada para cada conjunto de odds
    for i, odd in enumerate(odds_labels):
        ttk.Label(root, text=odd).grid(row=i, column=0)
        entry_row = []
        for j in range(3):
            entry = ttk.Entry(root)
            entry.grid(row=i, column=j+1)
            entry.insert(tk.END, "0.00")
            entry_row.append(entry)
        odds_entries.append(entry_row)

    # Adicionar um botão para gerar as combinações
    ttk.Button(root, text="Gerar Combinações", command=gerar_e_salvar_combinacoes).grid(row=len(odds_labels), columnspan=4)

    root.mainloop()

# Definir a função para gerar e salvar as combinações
def gerar_e_salvar_combinacoes():
    # Chamar a função que gera as combinações de odds
    combinacoes = gerar_combinacoes()

    # Criar um dataframe pandas com as combinações
    df = pd.DataFrame(combinacoes, columns=["Time 1", "Empate", "Time 2", "Odd Total"])

    # Salvar o dataframe em um arquivo xlsx
    df.to_excel(r'C:\Users\Matheus A Aleixo\Documents\WORKSPACE_PYTHON\probabilidades_odds\combinações.xlsx', index=False)
    # Mostrar uma mensagem de confirmação
    print("Arquivo xlsx gerado com sucesso!")

# Lista de labels para os campos de entrada de odds
odds_labels = ["Odds 1", "Odds 2", "Odds 3", "Odds 4"]

# Criar a interface gráfica
criar_interface()
