import tkinter as tk
from tkinter import messagebox
from datetime import date


# Função para calcular a diferença de tempo até o próximo aniversário
def calcular_diferenca(hoje, aniversario):
    if aniversario < hoje:
        aniversario = aniversario.replace(year=hoje.year + 1)
    diferenca = aniversario - hoje
    return diferenca.days, aniversario.year - hoje.year


# Função que verifica se hoje é o aniversário
def acertar_data():
    try:
        dia = entry_dia.get()
        mes = entry_mes.get()

        if len(dia) > 2 or len(mes) > 2:
            messagebox.showerror("ERRO", "Dia ou mês não podem ter mais de dois dígitos.")
            return

        dia = int(dia)
        mes = int(mes)

        if dia < 1 or dia > 31 or mes < 1 or mes > 12:
            messagebox.showerror("ERRO", "Por favor insira um dia ou mês válido.")
            return

        hoje = date.today()
        aniversario = date(hoje.year, mes, dia)
        dias, anos = calcular_diferenca(hoje, aniversario)

        if dia == hoje.day and mes == hoje.month:
            message = "Feliz aniversário!!!! Você está de aniversário hoje."
            messagebox.showinfo("Resultado", message)
        else:
            meses = dias // 30
            dias_restantes = dias % 30

            if anos == 0:
                message = ('Hoje não é seu aniversário.\nFaltam {} meses e {} dias para seu aniversário.'
                           .format(meses, dias_restantes))
                messagebox.showinfo("Resultado", message)
            else:
                message = ('Hoje não é seu aniversário.\nFaltam {} anos, {} meses e {} dias para seu aniversário.'
                           .format(anos, meses, dias_restantes))
                messagebox.showinfo("Resultado", message)
    except ValueError:
        messagebox.showerror("ERRO", "Por favor insira valores válidos.")


# Criação da Janela Principal
root = tk.Tk()
root.title("Você está de aniversário?")

# Criação dos widgets
label_dia = tk.Label(root, text="Insira o dia de nascimento: ")
label_dia.pack(pady=10)

entry_dia = tk.Entry(root)
entry_dia.pack(pady=5)

label_mes = tk.Label(root, text="Insira o mês de nascimento: ")
label_mes.pack(pady=10)

entry_mes = tk.Entry(root)
entry_mes.pack(pady=5)

button_verificar = tk.Button(root, text='Verificar', command=acertar_data)
button_verificar.pack(pady=15)

# Inicia o loop principal da interface gráfica
root.mainloop()
