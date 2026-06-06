# API que realiza conversão entre moedas
import requests

# URL da API
url = "https://api.exchangerate-api.com/v4/latest/BRL"

dados = requests.get(url)

resposta = dados.json()


# valor_moeda_base = resposta['rates']['BRL']

# print(valor_moeda_base)




# valor_moeda_base = resposta['rates']['BRL']
# dolar = 1 / resposta['rates']['USD']

# print(f" {dolar:.2f} BRL = 1 USD ")


                    # ATIVIDADE - TRANSFROMAR EURO EM REAL 
                    
valor_moeda_base = resposta['rates']['BRL']
euro = 1 / resposta['rates']['EUR']

print(f" {valor_moeda_base:.2f} EUR = {euro:.2f} BRL")






