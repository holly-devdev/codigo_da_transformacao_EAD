from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/saudacao", methods=["GET"])
def saudacao():
    return jsonify({"mensagem": "Bem-vindo a API Flask"})

if __name__ == "__main__":
    app.run()
