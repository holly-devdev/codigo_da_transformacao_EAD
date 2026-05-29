import requests

filme = input("Digite o nome de um filme em inglês (ex: Inception): ")
url = "https://api.themoviedb.org/3/search/movie?api_key=b63c273ecb15a67cb97cbcf4939b8b0e&query=" + filme

resposta = requests.get(url)
dados = resposta.json()

if dados["results"]:
    primeiro_filme = dados["results"][0]
    print("\n--- INFORMAÇÕES DO FILME ---")
    print("Título:", primeiro_filme["title"])
    print("Data de Lançamento:", primeiro_filme["release_date"])
    print("Sinopse:", primeiro_filme["overview"])
else:
    print("Filme não encontrado!")
