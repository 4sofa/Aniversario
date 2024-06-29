import tkinter as tk
from tkinter import messagebox
from datetime import date


def acertar_data():
    try:
        dia = int(entry_dia.get())
        mes = int(entry_mes.get())
        hoje = date.today()
        if dia == hoje.day and mes == hoje.month:
            messagebox.showinfo("Resultado", "Feliz aniversário!!!!"
                                             "Você está de aniversário hoje.")
        else:
            messagebox.showinfo("Resultado", "Você não está de aniversário hoje.")
    except ValueError:
        messagebox.showerror("ERRO", "Por favor insira valores válidos.")


# Criação da Janela Principal
root = tk.Tk()

root.title("Você está de aniversário?")

# Criação dos widgets

label_dia = tk.Label(root, text="Insira o dia: ")
label_dia.pack(pady=10)

entry_dia = tk.Entry(root)
entry_dia.pack(pady=5)

label_mes = tk.Label(root, text="Insira o mes: ")
label_mes.pack(pady=10)

entry_mes = tk.Entry(root)
entry_mes.pack(pady=5)

button_verificar = tk.Button(root, text='Verificar', command=acertar_data)
button_verificar.pack(pady=15)

root.mainloop()
