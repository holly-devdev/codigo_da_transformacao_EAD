import sqlite3

conexao = sqlite3.connect("banco_dados.db")
cursor = conexao.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS Tarefas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    descricao TEXT NOT NULL
)
""")

cursor.execute("INSERT INTO Tarefas (descricao) VALUES ('Estudar Python para o Modulo 11')")
cursor.execute("INSERT INTO Tarefas (descricao) VALUES ('Fazer compras no mercado')")

cursor.execute("DELETE FROM Tarefas WHERE id = 2")

cursor.execute("SELECT * FROM Tarefas")
lista_tarefas = cursor.fetchall()

print("--- Minhas Tarefas ---")
for tarefa in lista_tarefas:
    print(tarefa)

conexao.commit()
conexao.close()
