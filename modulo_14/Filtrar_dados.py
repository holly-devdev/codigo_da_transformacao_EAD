import sqlite3

conexao = sqlite3.connect("banco_dados.db")
cursor = conexao.cursor()

cursor.execute("SELECT * FROM Clientes WHERE nome LIKE 'A%'")
resultados = cursor.fetchall()

print("--- Clientes que começam com a letra A ---")
for cliente in resultados:
    print(cliente)

conexao.close()
