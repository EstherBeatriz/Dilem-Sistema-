import mysql.connector as mc

bd = mc.connect(
        host = "localhost",
        user = "root_dev",
        password = "admin",
        database = "bd_dilem"
    )





def cadastro_usuario(nome, email, ocupacao, instituicao, senha, bd):
    if bd.is_connected():
        comando = 'insert into usuarios(nome,email, ocupacao, instituicao, senha) values (%s, %s, %s, %s, %s)'
        cursor = bd.cursor()
        valores = (nome, email, ocupacao, instituicao, senha) 
        cursor.execute(comando, valores)
        bd.commit()
        
       
        
#VERIFQUE O USUÁRIO -------------------

def verifica_login_usuario(email, senha, bd):
    # Estabelecendo conexão com o banco de dados
    # bd = bd.connector.connect(
    #     host="localhost",
    #     user="usuario",
    #     password="senha",
    #     database="nome_do_banco_de_dados"
    # )
    #if bd.is_connected():
    # Criando cursor para executar as operações SQL
    cursor = bd.cursor()

    # Definindo a instrução SQL para selecionar o usuário com o e-mail e senha fornecidos
    consulta = "SELECT email, senha FROM usuario WHERE email = %s AND senha = %s"

    # Definindo os valores a serem usados na consulta
    valores = (email, senha)

    # Executando a consulta SQL
    cursor.execute(consulta, valores)

    # Obtendo o resultado da consulta
    resultado = cursor.fetchall()

    # Verificando se a consulta retornou algum resultado
    if len(resultado) == 1:
        return True
    else:
        return False
    
    
    

