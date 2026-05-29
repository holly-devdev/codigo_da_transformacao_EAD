from flask import Flask, request, jsonify

app = Flask(__name__)

posts = []
comentarios = []
usuarios = {"admin": "senha123"}

@app.route("/login", methods=["POST"])
def login():
    dados = request.get_json()
    username = dados.get("username")
    password = dados.get("password")
    if usuarios.get(username) == password:
        return jsonify({"token": "autenticado_sucesso"})
    return jsonify({"erro": "Nao autorizado"}), 401

@app.route("/posts", methods=["POST"])
def criar_post():
    dados = request.get_json()
    novo_post = {"id": len(posts) + 1, "titulo": dados.get("titulo"), "conteudo": dados.get("conteudo")}
    posts.append(novo_post)
    return jsonify(novo_post)

@app.route("/posts", methods=["GET"])
def listar_posts():
    return jsonify(posts)

@app.route("/comentarios", methods=["POST"])
def criar_comentario():
    dados = request.get_json()
    novo_comentario = {"post_id": dados.get("post_id"), "texto": dados.get("texto")}
    comentarios.append(novo_comentario)
    return jsonify(novo_comentario)

if __name__ == "__main__":
    app.run()
