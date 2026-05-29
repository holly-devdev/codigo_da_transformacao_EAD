from flask import Flask, jsonify
import pytest

app = Flask(__name__)

@app.route("/api")
def home():
    return jsonify({"status": "sucesso"})

@pytest.fixture
def cliente():
    return app.test_client()

def test_api_status(cliente):
    resposta = cliente.get("/api")
    assert resposta.status_code == 200
    assert resposta.json == {"status": "sucesso"}
