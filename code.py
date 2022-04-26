import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='XXXXXXXXXX',
    database='XXXXX',
)
cursor = conexao.cursor()

#CRUD

#CREATE
nome_jogo = "Rainbow Six"
categoria = "FPS"
comando = f'INSERT INTO jogos (nome_jogo, categoria) VALUES ("{nome_jogo}", "{categoria}")'
cursor.execute(comando)
conexao.commit() #edita o banco de dados

#READ
#nome_jogo = "Counter Strike"
#categoria = "FPS"
#comando = f'INSERT INTO jogos (nome_jogo, categoria) VALUES ("{nome_jogo}", "{categoria}")'
#cursor.execute(comando)
#conexao.commit() #edita o banco de dados

#UPDATE
#nome_jogo = "Counter Strike"
#categoria = "RPG"
#comando = f'UPDATE jogos SET categoria = "{categoria}" WHERE nome_jogo = "{nome_jogo}"'
#cursor.execute(comando)
#conexao.commit() #edita o banco de dados

#DELETE
#nome_jogo = "Counter Strike"
#comando = f'DELETE FROM jogos WHERE nome_jogo = "{nome_jogo}"'
#cursor.execute(comando)
#conexao.commit() #edita o banco de dados

cursor.close()
conexao.close()
