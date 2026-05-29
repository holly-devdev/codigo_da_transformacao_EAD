import requests

url = "https://api.open-meteo.com/v1/forecast?latitude=-23.55&longitude=-46.63&current_weather=true"

try:
    resposta = requests.get(url, timeout=5)
    resposta.raise_for_status()
    dados = resposta.json()
    print("Conexão bem-sucedida! Dados recebidos.")
except requests.exceptions.ConnectionError:
    print("Erro: Falha na conexão! Verifique sua internet.")
except requests.exceptions.Timeout:
    print("Erro: O site demorou demais para responder.")
except requests.exceptions.HTTPError:
    print("Erro: O site da API encontrou um problem.")
