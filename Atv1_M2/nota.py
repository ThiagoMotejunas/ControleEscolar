import customtkinter as ctk
from CTkMessagebox import CTkMessagebox
from conexao import *
from collections import Counter
import matplotlib.pyplot as plt
import numpy as np
from tkinter import messagebox
from collections import defaultdict

def frmNota():

    #Criação da tela
    global janela_nota
    global entry_id, entry_nota, entry_id_aluno, entry_id_materia, entry_id_professor
    janela_nota = ctk.CTk()
    janela_nota.title("Notas")
    janela_nota.geometry("600x400+100+100")
    janela_nota.resizable(False, False)

    #Moldura 1
    frame_0 = ctk.CTkFrame(janela_nota)
    frame_0.pack()

    # Moldura CRUD
    frame_CRUD = ctk.CTkFrame(janela_nota)
    frame_CRUD.pack()

    # Moldura Fechar
    frame_fechar = ctk.CTkFrame(janela_nota)
    frame_fechar.pack()

    # Entrada de dados

    #ID 
    label_id = ctk.CTkLabel(frame_0, text="Digite o ID: ", font=("Arial", 12))
    label_id.grid(row = 0, column = 0 , padx = 5, pady = 15)

    entry_id = ctk.CTkEntry(frame_0,font=("Arial", 12))
    entry_id.insert(0, "Sem id caso cadastro")
    entry_id.grid(row=0, column=1, padx=5, pady=10)

    # Nota
    label_nota = ctk.CTkLabel(frame_0, text="Digite a nota: ", font=("Arial", 12))
    label_nota.grid(row = 1, column = 0 , padx = 5, pady = 15)

    entry_nota = ctk.CTkEntry(frame_0,font=("Arial", 12))
    entry_nota.grid(row=1, column=1, padx=5, pady=10)

    # ID ALUNO
    label_id_aluno = ctk.CTkLabel(frame_0, text="Digite o id do aluno: ", font=("Arial", 12))
    label_id_aluno.grid(row = 2, column = 0 , padx = 5, pady = 15)

    entry_id_aluno = ctk.CTkEntry(frame_0,font=("Arial", 12))
    entry_id_aluno.grid(row=2, column=1, padx=5, pady=10)

    # ID PROFESSOR
    label_id_professor = ctk.CTkLabel(frame_0, text="Digite o id do professor: ", font=("Arial", 12))
    label_id_professor.grid(row = 3, column = 0 , padx = 5, pady = 15)

    entry_id_professor = ctk.CTkEntry(frame_0,font=("Arial", 12))
    entry_id_professor.grid(row=3, column=1, padx=5, pady=10)

     # ID MATERIA
    label_id_materia = ctk.CTkLabel(frame_0, text="Digite o id da matéria: ", font=("Arial", 12))
    label_id_materia.grid(row = 4, column = 0 , padx = 5, pady = 15)

    entry_id_materia = ctk.CTkEntry(frame_0,font=("Arial", 12))
    entry_id_materia.grid(row=4, column=1, padx=5, pady=10)

    # Botões CR

    # Cadastrar
    botao_cadastrar = ctk.CTkButton(frame_CRUD, text="Cadastrar", font=("Helvetica", 12, "bold"), command=cadastrar_nota)
    botao_cadastrar.grid(row=0, column=0, padx=5, pady=10)

    # Consultar
    botao_consultar = ctk.CTkButton(frame_CRUD, text="Consultar", font=("Helvetica", 12, "bold"), command=consultar_nota)
    botao_consultar.grid(row=0, column=1, padx=5, pady=10)

    # Alterar
    botao_alterar = ctk.CTkButton(frame_CRUD, text="Alterar", font=("Helvetica", 12, "bold"), command=alterar_nota)
    botao_alterar.grid(row=0, column=2, padx=5, pady=10)

    # Gráfico
    botao_grafico = ctk.CTkButton(frame_CRUD, text="Gráfico", font=("Helvetica", 12, "bold"), command=gerar_grafico_medias)
    botao_grafico.grid(row=0, column=3, padx=5, pady=10)

    # Botões
    botao_fechar = ctk.CTkButton(frame_fechar, text="Fechar", font=("Helvetica", 12, "bold"), command=fechar_nota)
    botao_fechar.grid(row=0, column=0, padx=5, pady=10)

    janela_nota.mainloop()

#Função cadastrar nota
def cadastrar_nota():
    #Abrir a conexão
    conexao, cursor = abrir_conexao()

    #Comando SQL para INSERIR 
    nota = entry_nota.get()
    id_aluno = entry_id_aluno.get()
    id_professor = entry_id_professor.get()
    id_materia = entry_id_materia.get()

    sql = f"INSERT into nota (nota, id_aluno, id_professor, id_materia) values ({nota}, {id_aluno}, {id_professor}, {id_materia})"
    cursor.execute(sql)
    conexao.commit()

    #Fechar a conexão
    fechar_conexao(conexao, cursor)

    CTkMessagebox(title="Cadastro", message="Cadastrado com sucesso", icon="check")


#Função consultar nota
def consultar_nota():
    #Abrir a conexão
    conexao, cursor = abrir_conexao()

    #Comando SQL para INSERIR 
    id = int(entry_id.get())
    sql = "select nota, id_aluno, id_professor, id_materia from nota where pk_id = %s"
    dados = (id, ) #tupla
    cursor.execute(sql, dados)

    resultado = cursor.fetchall()
    if resultado:
        for registro in resultado:
            entry_nota.insert('end', f"{registro[0]}")
            entry_id_aluno.insert('end', f"{registro[1]}")
            entry_id_professor.insert('end', f"{registro[2]}")
            entry_id_materia.insert('end', f"{registro[3]}")

        #Fechar a conexão
    fechar_conexao(conexao, cursor)

# Função alterar nota
def alterar_nota():
    #Abrir a conexão
    conexao, cursor = abrir_conexao()

    #Comando SQL para INSERIR 
    id_nota = int(entry_id.get())
    novo_nota = float(entry_nota.get())
    novo_id_aluno = int(entry_id_aluno.get())
    novo_id_professor = int(entry_id_professor.get())
    novo_id_materia = int(entry_id_materia.get())

    sql = "UPDATE nota SET nota = %s, id_aluno = %s, id_professor = %s, id_materia = %s WHERE pk_id = %s"
    dados = (novo_nota, novo_id_aluno, novo_id_professor, novo_id_materia, id_nota, )
    cursor.execute(sql, dados)
    conexao.commit()

    #Fechar a conexão
    fechar_conexao(conexao, cursor)

    CTkMessagebox(title="Alteração", message="Alterado com sucesso", icon="check")

def gerar_grafico_medias():

    try:
        # Abrir a conexão com o banco
        conexao, cursor = abrir_conexao()

        # Executar a query
        sql = "SELECT n.nota, m.nome_materia FROM nota n INNER JOIN materia m ON n.id_materia = m.pk_id;"
        cursor.execute(sql)
        resultados = cursor.fetchall()

        # Fechar conexão
        fechar_conexao(conexao, cursor)

        # Agrupar as notas por matéria
        notas_por_materia = defaultdict(list)
        for nota, materia in resultados:
            notas_por_materia[materia].append(nota)

        # Calcular a média por matéria
        materias = []
        medias = []

        for materia, notas in notas_por_materia.items():
            materias.append(materia)
            medias.append(sum(notas) / len(notas) if notas else 0)

        # Plotar gráfico
        y_pos = np.arange(len(materias))

        plt.figure(figsize=(10, 6))
        plt.bar(y_pos, medias, align="center", alpha=0.9)
        plt.xticks(y_pos, materias, rotation=45)
        plt.ylabel("Média das Notas")
        plt.title("UMC - Média das Notas por Matéria (turma)")
        plt.ylim(0, 10)
        plt.grid(axis="y", linestyle="--")

        for i, v in enumerate(medias):
            v_color = "blue" if v >= 6 else "red"
            plt.text(i, v + 0.1, f"{v:.1f}", color=v_color, fontweight="bold")

        plt.tight_layout()
        plt.show()

    except Exception as e:
        messagebox.showerror("Erro ao gerar gráfico", str(e))

    
    gerar_grafico_medias(materias, medias)
        
# Função fechar
def fechar_nota():
    janela_nota.destroy()