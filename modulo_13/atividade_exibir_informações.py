import requests

url = "https://api.open-meteo.com/v1/forecast?latitude=-23.55&longitude=-46.63&current_weather=true"

resposta = requests.get(url)
dados = resposta.json()

tempo_atual = dados["current_weather"]
temperatura = tempo_atual["temperature"]
vento = tempo_atual["windspeed"]

print("--- PREVISÃO DO TEMPO ---")
print("Temperatura atual:", temperatura, "°C")
print("Velocidade do vento:", vento, "km/h")
