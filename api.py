# INSTALAR BIBLIOTECA
# pip install requests

# SEGUNDO PASSO: ADICIONAR/IMPORT AO CÓDIGO
import requests

url  = "https://viacep.com.br/ws/13386-068/json/"

dados = requests.get(url).json()

print(dados)



print("-" * 50)

cep = input("Digite seu CEP: ")        # RECEBE O CEP DIGITADO PELO USUARIO
nome = input("Digite seu nome: ")
email = input("Digite o seu email: ")
telefone = input("Digite o seu telefone: ")

print()


# ATRIBUINDO VARIÁVEIS PARA CADA UM DOS RESULTADOS
# rua = dados['logradouro']
# bairro = dados['bairro']
# cidade = dados['localidade']

# print(rua)
# print(bairro)
# print(cidade)


# MÉTODO CLASSICO
# print(f"https://viacep.com.br/ws/{cep}/json/")      # UTILIZAMOS O "f" STRING, PARA CONSEGUIR INSERIR UMA VARIÁVEL
# print()


# MÉTODO COM IF
if len(cep) == 8 and cep.isdigit():
    print(f"https://viacep.com.br/ws/{cep}/json/")
else:
    print("ERRO!!!  Você digitou algo errado ou falta ter 8 algarismo")
    


print(f"\nBem vindo ao Mercado Livre {nome}! O seu e-mail é {email}. O seu telefone é {telefone}. Você mora na rua {dados['logradouro']}, na cidade {dados['localidade']}, no estado de {dados['estado']}.\n")


