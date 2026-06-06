import requests 

# Para criar uma função, utilizamos o comando "def"

# -----------------------------------------------------------------------------------


# def get_moedas():

#     url = "https://api.exchangerate-api.com/v4/latest/BRL"
#     try:
#         dados = requests.get(url)
#         resposta = dados.json()
#         valor_moeda_base = resposta['rates']['BRL']
#         dolar = 1 / resposta['rates']['USD']
#         euro = 1 / resposta['rates']['EUR']
#         return f"{dolar:.2f} USD = 1 BRL | {euro:.2f} = 1 BRL"

#     except:
#         return("Não foi possível realizar a conversão de valores")
        
# print(get_moedas())
        
        
# ---------------------------------------------------------------------------------





                    # ATIVIDADE PRATIVA 05 - CONSUMINDO API'S EXTERNAS
        
def get_moedas():

    url = "https://api.exchangerate-api.com/v4/latest/USD"       # mudou o "USD"
    try:
        dados = requests.get(url)
        resposta = dados.json()
        valor_moeda_base = resposta['rates']['USD']         # mudei o "USD"
        real =  resposta['rates']['BRL']                 # coloquei " * " no lugar do " / "
        euro =  resposta['rates']['EUR']                 # coloquei " * " no lugar do " / "
        librasEsterlinas =  resposta['rates']['GBP']     # coloquei " * " no lugar do " / "
        pesoArgentino =  resposta['rates']['ARS']        # coloquei " * " no lugar do " / "
        
        
        return f"{real:.2f} BRL = 1 USD | {euro:.2f} EUR = 1 USD | {librasEsterlinas:.2f} GBP = 1 USD | {pesoArgentino:.2f} ARS = 1 USD "

    except:
        return("Não foi possível realizar a conversão de valores")
        
print(get_moedas())
        