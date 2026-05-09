print(" -------------------------------------")
print("|    Coleta de dados, para registro   |")
print(" -------------------------------------")


# DECLARAÇÕES DE VARIÁVEIS
nome = input('Digite o seu nome: ')                                 #Variavel da linguagem "Python"
email = input("Digite o seu email: ")                               #Variavel da linguagem "Python"
cidade = input("Digite sua cidade: ")                               #Variavel da linguagem "Python"
estado = input("Digite seu estado: ")                               #Variavel da linguagem "Python"
pais = input("Digite seu país: ")                                   #Variavel da linguagem "Python"

idadeAtual = int(input("Digite sua idade: "))                       #Variavel da linguagem "Python"
idadeFutura = idadeAtual + 1                                        #Variavel da linguagem "Python"
anoAtual = int(input("Digite o ano atual: "))
anoNascimento = int(input("Digite seu ano de Nascimento: "))        #Variavel da linguagem "Python"
anosPassados = anoAtual - anoNascimento                             #Variavel da linguagem "Python"

print(" -------------------------------------")
print("|    Coleta de dados, para registro   |")
print(" -------------------------------------")


# EXIBE AS INFORMAÇÕES DO USUÁRIO COM MENSAGENS PERSONALIDAS.

print(f"Seu nome é: {nome}")            # O "f" minúsculo antes das aspas,permite que eu trabalhe com variáveis na frase. 
print(f"Seu email é: {email}")          # As chaves "{}" servem para eu chamar uma variável para dentro da frase.
print(f"Sua cidade é: {cidade}")
print(f"Seu estado é: {estado}")
print(f"Seu país é: {pais}")
print(f"Sua idade atual é: {idadeAtual}")
print(f"No ano que vem sua idade será: {idadeFutura}")
print(f"Se passaram {anosPassados} anos, desde o ano que você nasceu!!!")

print(" -------------------------------------")


#print(f"Olá {nome}, o seu email é {email}")

