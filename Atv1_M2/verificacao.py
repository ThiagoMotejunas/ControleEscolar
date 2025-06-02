import customtkinter
from CTkMessagebox import CTkMessagebox
from main import *

def frmVerificacao():

    global janela_verificacao
    global entry_usuario, entry_senha
    janela_verificacao = customtkinter.CTk()
    janela_verificacao.title("Login")
    janela_verificacao.geometry("300x200+100+100")
    janela_verificacao.resizable(False, False)

    #Moldura 1
    frame_0 = customtkinter.CTkFrame(janela_verificacao)
    frame_0.pack()

    #Moldura botões
    frame_botoes = customtkinter.CTkFrame(janela_verificacao)
    frame_botoes.pack()

    #Entrada dos dados 
    
    #ID
    label_usuario = customtkinter.CTkLabel(frame_0, text="Digite o usuário: ", font=("Arial", 12))
    label_usuario.grid(row = 0, column = 0 , padx = 5, pady = 15)

    entry_usuario = customtkinter.CTkEntry(frame_0,font=("Arial", 12))
    entry_usuario.grid(row=0, column=1, padx=5, pady=10)

    #Nome
    label_senha = customtkinter.CTkLabel(frame_0, text="Digite a senha: ", font=("Arial", 12))
    label_senha.grid(row = 1, column = 0 , padx = 5, pady = 15)

    entry_senha = customtkinter.CTkEntry(frame_0, font=("Arial", 12), show="*")
    entry_senha.grid(row=1, column=1, padx=5, pady=10)

    # Botões

    botao_entrar = customtkinter.CTkButton(frame_botoes, text="Entrar", font=("Helvetica", 12, "bold"), command=login)
    botao_entrar.grid(row=0, column=1, padx=5, pady=10)

    botao_fechar = customtkinter.CTkButton(frame_botoes, text="Fechar", font=("Helvetica", 12, "bold"), command=fechar)
    botao_fechar.grid(row=0, column=0, padx=5, pady=10)

    janela_verificacao.mainloop()

# Função fechar
def fechar():
    janela_verificacao.destroy()

#função de verificação do login
def login():
    # Dados fixos 
    usuario_correto = "admin"
    senha_correta = "1234"

    # Verificação
    if entry_usuario.get() == usuario_correto and entry_senha.get() == senha_correta:
        fechar()
        frmMain()
        
    else:
        CTkMessagebox(title="Erro", message="Usuário ou senha incorretos", icon="warning")

frmVerificacao()





