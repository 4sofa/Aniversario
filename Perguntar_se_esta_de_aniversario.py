import tkinter as tk
from tkinter import messagebox
from datetime import date
from PIL import Image, ImageTk


# Função para calcular a diferença de tempo até o próximo aniversário
def calcular_diferenca(hoje, aniversario):
    if aniversario < hoje:
        aniversario = aniversario.replace(year=hoje.year + 1)
    diferenca = aniversario - hoje
    return diferenca.days


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
        dias = calcular_diferenca(hoje, aniversario)

        if dia == hoje.day and mes == hoje.month:
            message = "Feliz aniversário!!!! Você está de aniversário hoje."
            messagebox.showinfo("Resultado", message)
        else:
            meses = dias // 30
            dias_restantes = dias % 30

            if meses == 0:
                message = ('Hoje não é seu aniversário.\nFaltam {} meses e {} dias para seu aniversário.'
                           .format(meses, dias_restantes))
                messagebox.showinfo("Resultado", message)
            else:
                message = ('Hoje não é seu aniversário.\nFaltam {} meses e {} dias para seu aniversário.'
                           .format(meses, dias_restantes))
                messagebox.showinfo("Resultado", message)
    except ValueError:
        messagebox.showerror("ERRO", "Por favor insira valores válidos.")


# Cria uma imagem RGB com uma cor de fundo específica

def criar_background(cor, largura, altura):
    imagem = Image.new("RGB", (largura, altura), cor)
    return imagem


# Criação da Janela Principal
root = tk.Tk()
root.title("Você está de aniversário?")


# Define as dimensões da janela

largura_janela = 800
altura_janela = 600

# Centraliza a janela na tela
largura_tela = root.winfo_screenwidth()
altura_tela = root.winfo_screenheight()
pos_x = (largura_tela - largura_janela) // 2
pos_y = (altura_tela - altura_janela) // 2
root.geometry(f"{largura_janela}x{altura_janela}+{pos_x}+{pos_y}")

# Cria a imagem de fundo
imagem_fundo = criar_background("lightblue", largura_janela, altura_janela)

# Converte a imagem para um formato compatível com Tkinter
imagem_fundo_tk = ImageTk.PhotoImage(imagem_fundo)

# Cria um Canvas para exibir a imagem de fundo
canvas = tk.Canvas(root, width=largura_janela, height=altura_janela)
canvas.pack(fill="both", expand=True)
canvas.create_image(0, 0, image=imagem_fundo_tk, anchor="nw")

# Criação dos widgets
label_dia = tk.Label(root, text="Insira o dia de nascimento: ", bg="lightblue")
label_dia_window = canvas.create_window(largura_janela//2, altura_janela//3 - 40, window=label_dia)

entry_dia = tk.Entry(root)
entry_dia_window = canvas.create_window(largura_janela//2, altura_janela//3, window=entry_dia)

label_mes = tk.Label(root, text="Insira o mês de nascimento: ", bg="lightblue")
label_mes_window = canvas.create_window(largura_janela//2, altura_janela//3 + 40, window=label_mes)

entry_mes = tk.Entry(root)
entry_mes_window = canvas.create_window(largura_janela//2, altura_janela//3 + 80, window=entry_mes)

button_verificar = tk.Button(root, text="Verificar", command=acertar_data)
button_verificar_window = canvas.create_window(largura_janela//2, altura_janela//3 + 120, window=button_verificar)

# Inicia o loop principal da interface gráfica
root.mainloop()
