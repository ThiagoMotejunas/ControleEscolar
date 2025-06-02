import customtkinter as ctk
from CTkMessagebox import CTkMessagebox
from conexao import *

def frmAluno():

    #Criação da tela
    global janela_aluno
    global entry_id, entry_nome, entry_idade, entry_cpf, entry_email
    janela_aluno = ctk.CTk()
    janela_aluno.title("Alunos")
    janela_aluno.geometry("600x400+100+100")
    janela_aluno.resizable(False, False)

    #Moldura 1
    frame_0 = ctk.CTkFrame(janela_aluno)
    frame_0.pack()

    #Moldura CRUD
    frame_CRUD = ctk.CTkFrame(janela_aluno)
    frame_CRUD.pack()

    #Moldura fechar
    frame_fechar = ctk.CTkFrame(janela_aluno)
    frame_fechar.pack()

    #Entrada dos dados 
    
    #ID
    label_id = ctk.CTkLabel(frame_0, text="Digite o ID: ", font=("Arial", 12))
    label_id.grid(row = 0, column = 0 , padx = 5, pady = 15)

    entry_id = ctk.CTkEntry(frame_0,font=("Arial", 12))
    entry_id.insert(0, "Sem id caso cadastro")
    entry_id.grid(row=0, column=1, padx=5, pady=10)

    #Nome
    label_nome = ctk.CTkLabel(frame_0, text="Digite o nome: ", font=("Arial", 12))
    label_nome.grid(row = 1, column = 0 , padx = 5, pady = 15)

    entry_nome = ctk.CTkEntry(frame_0,font=("Arial", 12))
    entry_nome.grid(row=1, column=1, padx=5, pady=10)

    #Idade
    label_idade = ctk.CTkLabel(frame_0, text="Digite a idade: ", font=("Arial", 12))
    label_idade.grid(row = 2, column = 0 , padx = 5, pady = 15)

    entry_idade = ctk.CTkEntry(frame_0,font=("Arial", 12))
    entry_idade.grid(row=2, column=1, padx=5, pady=10)

    #CPF
    label_cpf = ctk.CTkLabel(frame_0, text="Digite o cpf: ", font=("Arial", 12))
    label_cpf.grid(row = 3, column = 0 , padx = 5, pady = 15)

    entry_cpf = ctk.CTkEntry(frame_0,font=("Arial", 12))
    entry_cpf.grid(row=3, column=1, padx=5, pady=10)

    #Email
    label_email = ctk.CTkLabel(frame_0, text="Digite o email: ", font=("Arial", 12))
    label_email.grid(row = 4, column = 0 , padx = 5, pady = 15)

    entry_email = ctk.CTkEntry(frame_0,font=("Arial", 12))
    entry_email.grid(row=4, column=1, padx=5, pady=10)

    #Botões CRUD

    #Cadastrar
    botao_cadastrar = ctk.CTkButton(frame_CRUD, text="Cadastrar", font=("Helvetica", 12, "bold"), command=cadastrar_aluno)
    botao_cadastrar.grid(row=0, column=0, padx=5, pady=10)

    #Consultar
    botao_consultar = ctk.CTkButton(frame_CRUD, text="Consultar", font=("Helvetica", 12, "bold"), command=consultar_aluno)
    botao_consultar.grid(row=0, column=1, padx=5, pady=10)

    #Alterar
    botao_alterar = ctk.CTkButton(frame_CRUD, text="Alterar", font=("Helvetica", 12, "bold"), command=alterar_aluno)
    botao_alterar.grid(row=0, column=2, padx=5, pady=10)

    #Deletar
    botao_deletar = ctk.CTkButton(frame_CRUD, text="Deletar", font=("Helvetica", 12, "bold"), command=deletar_aluno)
    botao_deletar.grid(row=0, column=3, padx=5, pady=10)

    # Botão Fechar
    botao_fechar = ctk.CTkButton(frame_fechar, text="Fechar", font=("Helvetica", 12, "bold"), command=fechar_aluno)
    botao_fechar.grid(row=0, column=0, padx=5, pady=10)

    janela_aluno.mainloop()


#Função cadastrar aluno
def cadastrar_aluno():
    #Abrir a conexão
    conexao, cursor = abrir_conexao()

    #Comando SQL para INSERIR 
    nome = entry_nome.get()
    idade = int(entry_idade.get())
    cpf = entry_cpf.get()
    email = entry_email.get()

    sql = f"INSERT into alunos (nome, idade, cpf, email) values ('{nome}', {idade}, '{cpf}', '{email}')"
    cursor.execute(sql)
    conexao.commit()

    #Fechar a conexão
    fechar_conexao(conexao, cursor)

    CTkMessagebox(title="Cadastro", message="Cadastrado com sucesso", icon="check")


#Função consultar aluno 
def consultar_aluno():
    #Abrir a conexão
    conexao, cursor = abrir_conexao()

    #Comando SQL para INSERIR 
    id = int(entry_id.get())
    sql = "select nome, idade, cpf, email from alunos where pk_id = %s"
    dados = (id, ) #tupla
    cursor.execute(sql, dados)

    resultado = cursor.fetchall()
    if resultado:
        for registro in resultado:
            entry_nome.insert('end', f"{registro[0]}")
            entry_idade.insert('end', f"{registro[1]}")
            entry_cpf.insert('end', f"{registro[2]}")
            entry_email.insert('end', f"{registro[3]}")

        #Fechar a conexão
    fechar_conexao(conexao, cursor)

#Função alterar aluno 
def alterar_aluno():
    #Abrir a conexão
    conexao, cursor = abrir_conexao()

    #Comando SQL para INSERIR 
    id_aluno = int(entry_id.get())
    novo_nome = entry_nome.get()
    novo_idade = int(entry_idade.get())
    novo_cpf = entry_cpf.get()
    novo_email = entry_email.get()

    sql = "UPDATE alunos SET nome = %s, idade = %s, cpf = %s, email = %s WHERE pk_id = %s"
    dados = (novo_nome, novo_idade, novo_cpf, novo_email, id_aluno, )
    cursor.execute(sql, dados)
    conexao.commit()

    #Fechar a conexão
    fechar_conexao(conexao, cursor)

    CTkMessagebox(title="Alteração", message="Alterado com sucesso", icon="check")


#Função deletar aluno
def deletar_aluno():
    #Abrir a conexão
    conexao, cursor = abrir_conexao()

    #Comando SQL para INSERIR 
    id_aluno = int(entry_id.get())
    sql = "DELETE from alunos WHERE pk_id = %s"
    dados = (id_aluno,)
    cursor.execute(sql, dados)
    conexao.commit()

    #Fechar a conexão
    fechar_conexao(conexao, cursor)

    CTkMessagebox(title="Delete", message="Deletado com sucesso", icon="check")


# Função fechar
def fechar_aluno():
    janela_aluno.destroy()