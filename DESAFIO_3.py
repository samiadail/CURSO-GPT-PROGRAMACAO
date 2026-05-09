print("-" * 40)
print("|\t\tCALCULADORA\t\t|")
print("-" * 40)

numUm = int(input("Digite o Primeiro número: "))
numDois = int(input("Digite o Segundo número: "))

resultado = input("Digite a operação (+, -, *, /): ")

if resultado == "+":
    print(numUm + numDois)

elif resultado == "-":
    print(numUm - numDois)

elif resultado == "*":
    print(numUm * numDois)

elif resultado == "/":
    print(numUm / numDois)

else:
    print("Você não usou uma das opções")