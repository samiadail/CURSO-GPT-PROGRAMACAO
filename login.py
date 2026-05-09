#  "" print(type(nomeUsuario)) " -- ele mostra que tipo de variavel eu coloquei
print("-" * 50)
print("Sistema de autenticação")
print("-" * 50)

nomeUsuario = input("Digite seu nome: ")
senhaUsuario = int(input("Digite a sua senha: "))

if nomeUsuario == "sami" and senhaUsuario == "123":
    print("Acesso liberado!")
else:
    print("Acesso negado! Verfique as informações de login e tente novamente!")

