import requests as rq


cep = input("Digite o CEP da sua casa: ")

url = f"https://viacep.com.br/ws/{cep}/json/"

dados = rq.get(url)

respota = dados.json()              # TODA FUNÇÃO "jSON" TEM LOGO EM SEGUIDA OS PARENTESES

print(respota)

