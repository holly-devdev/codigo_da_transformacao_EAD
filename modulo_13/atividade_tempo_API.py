import requests

url = "https://api.open-meteo.com/v1/forecast?latitude=-23.55&longitude=-46.63&current_weather=true"

resposta = requests.get(url)
dados = resposta.json()

print(dados)
