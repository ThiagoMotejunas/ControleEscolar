import mysql.connector

def abrir_conexao():
    try:
        conexao = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="escola_bd",
        )
        cursor = conexao.cursor()
        return conexao, cursor
    
    except mysql.connector.Error as erro:
        print("Erro ao abrir a conexão:", erro)
        return None, None

def fechar_conexao(conexao, cursor):
    if conexao.is_connected():
        cursor.close()
        conexao.close()
        print("Conexão fechada com sucesso.")
    else:
        print("Conexão já está fechada.")