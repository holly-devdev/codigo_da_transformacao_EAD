from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/cadastrar", methods=["POST"])
def cadastrar():
    dados = request.get_json()
    nome = dados.get("nome")
    return jsonify({"status": "sucesso", "usuario_recebido": nome})

if __name__ == "__main__":
    app.run()
