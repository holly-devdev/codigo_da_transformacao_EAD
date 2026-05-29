import sqlite3

conexao = sqlite3.connect("banco_dados.db")
cursor = conexao.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS Clientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT NOT NULL
)
""")

conexao.commit()
conexao.close()
print("Tabela Clientes criada com sucesso!")
