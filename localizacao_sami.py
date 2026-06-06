import requests as rq


cep = input("Digite seu cep: ")

url = f"https://viacep.com.br/ws/{cep}/json/"

dados = rq.get(url)

resposta = dados.json()

rua = resposta['logradouro']
bairro = resposta['bairro']
estado = resposta['estado']
cidade = resposta['localidade']

print(f"Voce mora na rua {rua}, no bairro {bairro}, na cidade de {cidade} no estado de {estado}.")