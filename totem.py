import tkinter as tk
import webbrowser
from tkinter import PhotoImage

# Cria a janela principal
janela = tk.Tk()
# Define o tamanho da janela
janela.geometry("800x600+560+240")
# Define a cor de fundo da janela
janela.configure(bg="#40414f")
# Altera o ícone da janela para o ícone no caminho especificado
janela.wm_iconbitmap("logoDPU.ico")
# Altera o titulo da janela
janela.wm_title("Consulta Processual")
# Cria a função para exibir o popup quando a janela for fechada
def popup_fechar():
    popup = tk.Tk()
    popup.geometry("300x100+835+490")
    popup.wm_iconbitmap("logoDPU.ico")
    popup.wm_title("Não pode fechar")
    label = tk.Label(popup, text="Impossível fechar essa janela", font=("Helvetica", 16))
    label.pack(side="top", fill="x", pady=10)
    botao_fechar = tk.Button(popup, text="Fechar", command=popup.destroy)
    botao_fechar.pack()
    popup.mainloop()
# Carregar a imagem
imagem = tk.PhotoImage(file='Imagens/IconeDPU.png')
# Criar o widget Label para exibir a imagem
label = tk.Label(janela, image=imagem, bg='#40414f', width=200, height=100)
# Posicionar a imagem na coordenada (x=10, y=10)
label.place(x=0, y=0)
# Sobrescreve a função de fechar da janela para exibir o popup
janela.protocol("WM_DELETE_WINDOW", popup_fechar)
# Define a ação do primeiro botão
def abrir_seeu():
    webbrowser.open("https://seeu.pje.jus.br/seeu/")
# Cria o primeiro botão
botao_consultar_seeu = tk.Button(janela, text="CONSULTAR SEEU", bg="#439738", height=5, width=25)
botao_consultar_seeu.configure(command=abrir_seeu)
# Cria o segundo botão
botao_outra_janela = tk.Button(janela, text="CONSULTAR OUTROS PORTAIS", bg="#439738", height=5, width=25)
# Define a ação do segundo botão
def abrir_outra_janela():
    janela.withdraw()
    outra_janela = tk.Tk()
    outra_janela.geometry("800x600")
    outra_janela.configure(bg="#40414f")
    outra_janela.wm_title("Outras Consultas")
    outra_janela.wm_iconbitmap("logoDPU.ico")
    # Criar os 4 botões e mostrar na tela
    botao_1 = tk.Button(outra_janela, text="CONSULTAR SITE 1", bg="#439738", height=5, width=25)
    botao_2 = tk.Button(outra_janela, text="CONSULTAR SITE 2", bg="#439738", height=5, width=25)
    botao_3 = tk.Button(outra_janela, text="CONSULTAR SITE 3", bg="#439738", height=5, width=25)
    botao_4 = tk.Button(outra_janela, text="CONSULTAR SITE 4", bg="#439738", height=5, width=25)
    botao_5 = tk.Button(outra_janela, text="CONSULTAR SITE 5", bg="#439738",height=5, width=25)
    botao_1.place(relx=0.4, rely=0.01)
    botao_2.place(relx=0.4, rely=0.2)
    botao_3.place(relx=0.4, rely=0.4)
    botao_4.place(relx=0.4, rely=0.6)
    botao_5.place(relx=0.4, rely=0.8)
    # Define a ação do botão para voltar à primeira janela
    def voltar_janela():
        outra_janela.withdraw()
        janela.deiconify()
    # Cria o botão para voltar à primeira janela
    botao_voltar = tk.Button(outra_janela, text="VOLTAR", bg="#439738", height=5, width=20)
    botao_voltar.configure(command=voltar_janela)
    # Adiciona o botão à segunda janela
    botao_voltar.place(relx=0.01, rely=0.8)
    # Criar a função de popup quando a tela for fechada
    def popup_fechar1():
        popup = tk.Tk()
        popup.wm_title("Impossível fechar")
        label = tk.Label(popup, text="Impossível fechar", font=("Helvetica", 16))
        label.pack(side="top", fill="x", pady=10)
        botao_fechar = tk.Button(popup, text="Fechar", command=popup.destroy)
        botao_fechar.pack()
        popup.mainloop()
    # Sobrescreve a função de fechar da janela para exibir o popup
    outra_janela.protocol("WM_DELETE_WINDOW", popup_fechar)
botao_outra_janela.configure(command=abrir_outra_janela)
# Exibe os botões na janela
botao_consultar_seeu.place(x=330, y=100)
botao_outra_janela.place(x=330, y=200)
# Exibe a janela
janela.mainloop()