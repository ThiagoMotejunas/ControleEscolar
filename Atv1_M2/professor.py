import customtkinter as ctk
from CTkMessagebox import CTkMessagebox
from conexao import *

def frmProfessor():

    #Criação da tela
    global janela_professor
    global entry_id, entry_nome, entry_cpf, entry_periodo
    janela_professor = ctk.CTk()
    janela_professor.title("Professores")
    janela_professor.geometry("600x400+100+100")
    janela_professor.resizable(False, False)

    #Moldura 1
    frame_0 = ctk.CTkFrame(janela_professor)
    frame_0.pack()

    # Moldura CRUD
    frame_CRUD = ctk.CTkFrame(janela_professor)
    frame_CRUD.pack()

    # Moldura Fechar
    frame_fechar = ctk.CTkFrame(janela_professor)
    frame_fechar.pack()

    # Entrada de dados

    #ID 
    label_id = ctk.CTkLabel(frame_0, text="Digite o ID: ", font=("Arial", 12))
    label_id.grid(row = 0, column = 0 , padx = 5, pady = 15)

    entry_id = ctk.CTkEntry(frame_0,font=("Arial", 12))
    entry_id.insert(0, "Sem id caso cadastro")
    entry_id.grid(row=0, column=1, padx=5, pady=10)


    # Nome

    label_nome = ctk.CTkLabel(frame_0, text="Digite o nome: ", font=("Arial", 12))
    label_nome.grid(row = 1, column = 0 , padx = 5, pady = 15)

    entry_nome = ctk.CTkEntry(frame_0,font=("Arial", 12))
    entry_nome.grid(row=1, column=1, padx=5, pady=10)

    # CPF
    label_cpf = ctk.CTkLabel(frame_0, text="Digite o cpf: ", font=("Arial", 12))
    label_cpf.grid(row = 2, column = 0 , padx = 5, pady = 15)

    entry_cpf = ctk.CTkEntry(frame_0,font=("Arial", 12))
    entry_cpf.grid(row=2, column=1, padx=5, pady=10)

    #Período
    label_periodo = ctk.CTkLabel(frame_0, text="Digite o período: ", font=("Arial", 12))
    label_periodo.grid(row = 3, column = 0 , padx = 5, pady = 15)

    entry_periodo = ctk.CTkEntry(frame_0,font=("Arial", 12))
    entry_periodo.grid(row=3, column=1, padx=5, pady=10)

    #Botões CRUD

    #Cadastrar
    botao_cadastrar = ctk.CTkButton(frame_CRUD, text="Cadastrar", font=("Helvetica", 12, "bold"), command=cadastrar_professor)
    botao_cadastrar.grid(row=0, column=0, padx=5, pady=10)

    #Consultar
    botao_consultar = ctk.CTkButton(frame_CRUD, text="Consultar", font=("Helvetica", 12, "bold"), command=consultar_professor)
    botao_consultar.grid(row=0, column=1, padx=5, pady=10)

    #Alterar
    botao_alterar = ctk.CTkButton(frame_CRUD, text="Alterar", font=("Helvetica", 12, "bold"), command=alterar_professor)
    botao_alterar.grid(row=0, column=2, padx=5, pady=10)

    #Deletar
    botao_deletar = ctk.CTkButton(frame_CRUD, text="Deletar", font=("Helvetica", 12, "bold"), command=deletar_professor)
    botao_deletar.grid(row=0, column=3, padx=5, pady=10)

    # Botões
    botao_fechar = ctk.CTkButton(frame_fechar, text="Fechar", font=("Helvetica", 12, "bold"), command=fechar_professor)
    botao_fechar.grid(row=0, column=0, padx=5, pady=10)

    janela_professor.mainloop()

#Função cadastrar professor
def cadastrar_professor():
    #Abrir a conexão
    conexao, cursor = abrir_conexao()

    #Comando SQL para INSERIR 
    nome = entry_nome.get()
    cpf = entry_cpf.get()
    periodo = entry_periodo.get()

    sql = f"INSERT into professor (nome_professor, cpf_professor, periodo) values ('{nome}', '{cpf}', '{periodo}')"
    cursor.execute(sql)
    conexao.commit()

    #Fechar a conexão
    fechar_conexao(conexao, cursor)

    CTkMessagebox(title="Cadastro", message="Cadastrado com sucesso", icon="check")


#Função consultar professor
def consultar_professor():
    #Abrir a conexão
    conexao, cursor = abrir_conexao()

    #Comando SQL para INSERIR 
    id = int(entry_id.get())
    sql = "select nome_professor, cpf_professor, periodo from professor where pk_id = %s"
    dados = (id, ) #tupla
    cursor.execute(sql, dados)

    resultado = cursor.fetchall()
    if resultado:
        for registro in resultado:
            entry_nome.insert('end', f"{registro[0]}")
            entry_cpf.insert('end', f"{registro[1]}")
            entry_periodo.insert('end', f"{registro[2]}")

        #Fechar a conexão
    fechar_conexao(conexao, cursor)

#Função alterar professor
def alterar_professor():
    #Abrir a conexão
    conexao, cursor = abrir_conexao()

    #Comando SQL para INSERIR 
    id_professor = int(entry_id.get())
    novo_nome = entry_nome.get()
    novo_cpf = entry_cpf.get()
    novo_periodo = entry_periodo.get()

    sql = "UPDATE professor SET nome_professor = %s, cpf_professor = %s, periodo = %s WHERE pk_id = %s"
    dados = (novo_nome, novo_cpf, novo_periodo, id_professor, )
    cursor.execute(sql, dados)
    conexao.commit()

    #Fechar a conexão
    fechar_conexao(conexao, cursor)

    CTkMessagebox(title="Alteração", message="Alterado com sucesso", icon="check")


#Função deletar professor
def deletar_professor():
    #Abrir a conexão
    conexao, cursor = abrir_conexao()

    #Comando SQL para INSERIR 
    id_professor = int(entry_id.get())
    sql = "DELETE from professor WHERE pk_id = %s"
    dados = (id_professor,)
    cursor.execute(sql, dados)
    conexao.commit()

    #Fechar a conexão
    fechar_conexao(conexao, cursor)

    CTkMessagebox(title="Delete", message="Deletado com sucesso", icon="check")

# Função fechar
def fechar_professor():
    janela_professor.destroy()