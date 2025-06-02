import customtkinter as ctk
from CTkMessagebox import CTkMessagebox
from conexao import *

def frmMateria():

    #Criação da tela
    global janela_materia
    global entry_id, entry_nome, entry_tempo
    janela_materia = ctk.CTk()
    janela_materia.title("Matéria")
    janela_materia.geometry("600x400+100+100")
    janela_materia.resizable(False, False)

    #Moldura 1
    frame_0 = ctk.CTkFrame(janela_materia)
    frame_0.pack()

    #Moldura CRUD
    frame_CRUD = ctk.CTkFrame(janela_materia)
    frame_CRUD.pack()

    #Moldura fechar
    frame_fechar = ctk.CTkFrame(janela_materia)
    frame_fechar.pack()

    #Entrada dos dados 
    
    #ID
    label_id = ctk.CTkLabel(frame_0, text="Digite o ID: ", font=("Arial", 12))
    label_id.grid(row = 0, column = 0 , padx = 5, pady = 15)

    entry_id = ctk.CTkEntry(frame_0,font=("Arial", 12))
    entry_id.insert(0, "Sem id caso cadastro")
    entry_id.grid(row=0, column=1, padx=5, pady=10)

    #Nome
    label_nome = ctk.CTkLabel(frame_0, text="Digite o nome da matéria: ", font=("Arial", 12))
    label_nome.grid(row = 1, column = 0 , padx = 5, pady = 15)

    entry_nome = ctk.CTkEntry(frame_0,font=("Arial", 12))
    entry_nome.grid(row=1, column=1, padx=5, pady=10)

    #tempo aula
    label_tempo = ctk.CTkLabel(frame_0, text="Digite o tempo da aula (min): ", font=("Arial", 12))
    label_tempo.grid(row = 2, column = 0 , padx = 5, pady = 15)

    entry_tempo = ctk.CTkEntry(frame_0,font=("Arial", 12))
    entry_tempo.grid(row=2, column=1, padx=5, pady=10)


    #Botões CRUD

    #Cadastrar
    botao_cadastrar = ctk.CTkButton(frame_CRUD, text="Cadastrar", font=("Helvetica", 12, "bold"), command=cadastrar_materia)
    botao_cadastrar.grid(row=0, column=0, padx=5, pady=10)

    #Consultar
    botao_consultar = ctk.CTkButton(frame_CRUD, text="Consultar", font=("Helvetica", 12, "bold"), command=consultar_materia)
    botao_consultar.grid(row=0, column=1, padx=5, pady=10)

    #Alterar
    botao_alterar = ctk.CTkButton(frame_CRUD, text="Alterar", font=("Helvetica", 12, "bold"), command=alterar_materia)
    botao_alterar.grid(row=0, column=2, padx=5, pady=10)

    #Deletar
    botao_deletar = ctk.CTkButton(frame_CRUD, text="Deletar", font=("Helvetica", 12, "bold"), command=deletar_materia)
    botao_deletar.grid(row=0, column=3, padx=5, pady=10)

    # Botões

    botao_fechar = ctk.CTkButton(frame_fechar, text="Fechar", font=("Helvetica", 12, "bold"), command=fechar_materia)
    botao_fechar.grid(row=0, column=0, padx=5, pady=10)

    janela_materia.mainloop()

#Função cadastrar materia
def cadastrar_materia():
    #Abrir a conexão
    conexao, cursor = abrir_conexao()

    #Comando SQL para INSERIR 
    nome = entry_nome.get()
    tempo_aula = int(entry_tempo.get())

    sql = f"INSERT into materia (nome_materia, tempo_aula) values ('{nome}', {tempo_aula})"
    cursor.execute(sql)
    conexao.commit()

    #Fechar a conexão
    fechar_conexao(conexao, cursor)

    CTkMessagebox(title="Cadastro", message="Cadastrado com sucesso", icon="check")


#Função consultar materia
def consultar_materia():
    #Abrir a conexão
    conexao, cursor = abrir_conexao()

    #Comando SQL para INSERIR 
    id = int(entry_id.get())
    sql = "select nome_materia, tempo_aula from materia where pk_id = %s"
    dados = (id, ) #tupla
    cursor.execute(sql, dados)

    resultado = cursor.fetchall()
    if resultado:
        for registro in resultado:
            entry_nome.insert('end', f"{registro[0]}")
            entry_tempo.insert('end', f"{registro[1]}")

        #Fechar a conexão
    fechar_conexao(conexao, cursor)

#Função alterar materia 
def alterar_materia():
    #Abrir a conexão
    conexao, cursor = abrir_conexao()

    #Comando SQL para INSERIR 
    id_materia = int(entry_id.get())
    novo_nome = entry_nome.get()
    novo_tempo = int(entry_tempo.get())

    sql = "UPDATE materia SET nome_materia = %s, tempo_aula = %s WHERE pk_id = %s"
    dados = (novo_nome, novo_tempo, id_materia, )
    cursor.execute(sql, dados)
    conexao.commit()

    #Fechar a conexão
    fechar_conexao(conexao, cursor)

    CTkMessagebox(title="Alteração", message="Alterado com sucesso", icon="check")


#Função deletar materia
def deletar_materia():
    #Abrir a conexão
    conexao, cursor = abrir_conexao()

    #Comando SQL para INSERIR 
    id_materia = int(entry_id.get())
    sql = "DELETE from materia WHERE pk_id = %s"
    dados = (id_materia,)
    cursor.execute(sql, dados)
    conexao.commit()

    #Fechar a conexão
    fechar_conexao(conexao, cursor)

    CTkMessagebox(title="Delete", message="Deletado com sucesso", icon="check")


# Função fechar
def fechar_materia():
    janela_materia.destroy()