import customtkinter
import tkinter as tk
from CTkMessagebox import CTkMessagebox
import nltk
nltk.download('punkt_tab')
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nota import *
from materia import *
from professor import *
from aluno import *
from conexao import *

# Baixa recursos do NLTK
nltk.download("punkt")

# ChatBot
def chatbot(mensagem):
    respostas = {
        "aluno": "Na aba alunos você consegue fazer as seguintes funções: "
        "\n » Cadastrar: Para cadastrar você irá colocar os dados do aluno sem o id"
        "\n » Consultar: Aqui você irá apenas colocar o id do aluno e clicar em consultar para trazer os dados do aluno"
        "\n » Alterar: Sugiro consultar o aluno antes de alterar os dados, o mais importante é não mudar o id do aluno"
        "\n » Deletar: Sugiro consultar o aluno antes de deletar os dados do aluno para que não seja excluido o aluno errado"
        "\n",
        "professor": "Na aba professor você consegue fazer as seguintes funções: "
        "\n » Cadastrar: Para cadastrar você irá colocar os dados do professor sem o id"
        "\n » Consultar: Aqui você irá apenas colocar o id do professor e clicar em consultar para trazer os dados do professor"
        "\n » Alterar: Sugiro consultar o professor antes de alterar os dados, o mais importante é não mudar o id do professor"
        "\n » Deletar: Sugiro consultar o professor antes de deletar os dados do professor para que não seja excluido o professor errado"
        "\n",
        "materia": "Na aba matéria você consegue fazer as seguintes funções: "
        "\n » Cadastrar: Para cadastrar você irá colocar os dados da matéria sem o id"
        "\n » Consultar: Aqui você irá apenas colocar o id da matéria e clicar em consultar para trazer os dados da matéria"
        "\n » Alterar: Sugiro consultar a matéria antes de alterar os dados, o mais importante é não mudar o id da matéria"
        "\n » Deletar: Sugiro consultar a matéria antes de deletar os dados da matéria para que não seja excluido a matéria errada"
        "\n",
        "nota": "Na aba nota você consegue fazer as seguintes funções: "
        "\n » Cadastrar: Para cadastrar você irá colocar os dados da nota sem o id"
        "\n » Consultar: Aqui você irá apenas colocar o id da nota e clicar em consultar para trazer os dados da nota"
        "\n » Alterar: Sugiro consultar a nota antes de alterar os dados, o mais importante é não mudar o id da nota"
        "\n",  
    }

    palavras = word_tokenize(mensagem.lower())
    stemmer = PorterStemmer()
    palavra_raiz = [stemmer.stem(palavra) for palavra in palavras]

    for palavra in palavra_raiz:
        if palavra in respostas:
            return respostas[palavra]

    return "Desculpe, não entendi sua pergunta. Poderia reformular?"

# Função enviar mensagem do usuário ao chatbot
def enviar_mensagem():
    mensagem_usuario = entrada_usuario.get()
    if mensagem_usuario.strip() == "":
        return
    resposta_chatbot = chatbot(mensagem_usuario)
    caixa_texto.configure(state="normal")
    caixa_texto.insert("end", f"Você: {mensagem_usuario}\n", "usuario")
    caixa_texto.insert("end", f"Chatbot: {resposta_chatbot}\n", "chatbot")
    caixa_texto.configure(state="disabled")
    entrada_usuario.delete(0, tk.END)

# Interface principal
def frmMain():
    global entrada_usuario, caixa_texto

    janelaMain = customtkinter.CTk()
    janelaMain.title("Sistema Escolar com ChatBot")
    janelaMain.geometry("700x600")
    janelaMain.resizable(False, False)
    

    # Frame dos botões superiores
    frame_botoes = customtkinter.CTkFrame(janelaMain)
    frame_botoes.pack(pady=10)

    botao_aluno = customtkinter.CTkButton(frame_botoes, text="Alunos", command=frmAluno)
    botao_aluno.grid(row=0, column=0, padx=10)

    botao_professor = customtkinter.CTkButton(frame_botoes, text="Professores", command=frmProfessor)
    botao_professor.grid(row=0, column=1, padx=10)

    botao_materia = customtkinter.CTkButton(frame_botoes, text="Matérias", command=frmMateria)
    botao_materia.grid(row=0, column=2, padx=10)

    botao_notas = customtkinter.CTkButton(frame_botoes, text="Notas", command=frmNota)
    botao_notas.grid(row=0, column=3, padx=10)

    # Frame do chat
    frame_chat = customtkinter.CTkFrame(janelaMain)
    frame_chat.pack(pady=10, fill="both", expand=True)

    caixa_texto = tk.Text(frame_chat, height=20, wrap=tk.WORD, state="disabled", bg="#1a1a1a", fg="white", font=("Arial", 12))
    caixa_texto.pack(padx=10, pady=10, fill="both", expand=True)
    caixa_texto.tag_config("usuario", foreground="lightgreen")
    caixa_texto.tag_config("chatbot", foreground="cyan")

    # Entrada do usuário e botão de enviar
    frame_entrada = customtkinter.CTkFrame(janelaMain)
    frame_entrada.pack(pady=10)

    entrada_usuario = customtkinter.CTkEntry(frame_entrada, width=400, placeholder_text="Digite sua mensagem...")
    entrada_usuario.grid(row=0, column=0, padx=10)

    botao_enviar = customtkinter.CTkButton(frame_entrada, text="Enviar", command=enviar_mensagem)
    botao_enviar.grid(row=0, column=1, padx=5)

    janelaMain.mainloop()