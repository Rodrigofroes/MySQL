import mysql.connector

bdc = mysql.connector.connect(
    host = 'localhost',
    username = 'root',
    password = '',
    database = 'cadastro'
)

mycursor = bdc.cursor()

mycursor.execute(
    """ USE cadastro
"""
)

mycursor.execute ( """
    CREATE TABLE IF NOT EXISTS usuario (
        id INT NOT NULL AUTO_INCREMENT,
        nome VARCHAR(30),
        senha VARCHAR(30),
        PRIMARY KEY(id)
    );
"""
)

mycursor.execute("""SELECT nome, senha, email FROM usuario ORDER BY nome""")

result = mycursor.fetchall()


print('Dados salvos:')
for row in result:
    print(row)
