import sqlite3

conexao = sqlite3.connect("banco_dados.db")
cursor = conexao.cursor()

cursor.execute("INSERT INTO Clientes (nome, email) VALUES ('Ana Silva', 'ana@email.com')")
cursor.execute("INSERT INTO Clientes (nome, email) VALUES ('Carlos Souza', 'carlos@email.com')")

cursor.execute("SELECT * FROM Clientes")
print("Clientes cadastrados:", cursor.fetchall())

cursor.execute("UPDATE Clientes SET email = 'ana.silva@email.com' WHERE nome = 'Ana Silva'")

cursor.execute("DELETE FROM Clientes WHERE nome = 'Carlos Souza'")

conexao.commit()
conexao.close()
print("Operações CRUD executadas com sucesso!")
