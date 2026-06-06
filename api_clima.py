# Biblioteca de requisições
import requests 
# Biblioteca de sistema
import os

api_key = ("f94df017b4600171fb5ca127a884a55b")

cidade = "Americana"


url = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={api_key}&units=metric&lang-pt"

dados = requests.get(url)

resposta = dados.json()



temperaturaAtual = resposta['main']['temp']
umidade = resposta['main']['humidity']
descricao= resposta['weather'][0]['description']




print(temperaturaAtual)
print(umidade)
print(descricao)



# print(resposta)










