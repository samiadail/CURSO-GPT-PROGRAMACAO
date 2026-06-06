# Biblioteca de requisições
import requests 


def get_clima(cidade):
    
    api_key = ("f94df017b4600171fb5ca127a884a55b")
    # cidade = "Americana"
    

    url = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={api_key}&units=metric&lang-pt"
        
        
        
    try:
        dados = requests.get(url)
        resposta = dados.json()
        
        temperaturaAtual = resposta['main']['temp']
        umidade = resposta['main']['humidity']
        descricao= resposta['weather'][0]['description']

        return f"\n A temperatura atual é: {temperaturaAtual} |\n A umidade atual é: {umidade} |\n Descrição: {descricao}. | \n"
        
        
    except:
        return("Não foi possível realizar a amostra de dados")    
        
        
        
print(get_clima("Campinas"))
        
        
        
        # print(temperaturaAtual)
        # print(umidade)
        # print(descricao)