from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

def iniciar_banco():
    conexao = sqlite3.connect("usuarios.db")
    cursor = conexao.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS Usuarios (id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT)")
    conexao.commit()
    conexao.close()

iniciar_banco()

@app.route("/cadastrar", methods=["POST"])
def cadastrar_no_banco():
    dados = request.get_json()
    nome = dados.get("nome")
    
    conexao = sqlite3.connect("usuarios.db")
    cursor = conexao.cursor()
    cursor.execute("INSERT INTO Usuarios (nome) VALUES (?)", (nome,))
    conexao.commit()
    conexao.close()
    
    return jsonify({"status": "Usuario salvo no banco de dados"})

if __name__ == "__main__":
    app.run()
