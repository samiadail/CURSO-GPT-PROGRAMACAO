listaNotas = []     #Criamos um lista vazia


print("-" * 50)
print("Bem vindo a I.A. que calcula notas e média final ")
print("-" * 50)

while True:
    notas = input("Digite a nota que deseja inserir (digite sai para parar): ")

    if notas.lower() == "sair":                     # Comando LOWER obriga a entrada a ser minúscula
        break
    else:
        listaNotas.append(float(notas))             # Insere dados em uma lista

media = sum(listaNotas) / len(listaNotas)           # Comando "sum" -> SOMA
                                                    # Insere dados em uma lsita

print("-" * 50)
print(f"A media final do aluno é {media:.3f}")      # o ":.2f" serve para limitar o tanto de casas decimais
print("-" * 50)

if media >= 6:
    print("Você foi aprovado!!!")
else:
    print("Você está reprovado!!! Não falte e estude mais!!!")
    
print("-" * 50)