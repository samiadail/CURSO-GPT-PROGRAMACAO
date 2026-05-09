print("\tBem vindo ao portal Educacional do Platini")

notaUm = float(input("Digite a primeira nota do aluno: "))
notaDois = float(input("Digite a segunda nota do aluno "))
notaTres = float(input("Digite a terceira nota do aluno "))
notaQuatro = float(input("Digite a quarta nota do aluno "))


media = (notaUm + notaDois + notaTres + notaQuatro) / 4


print(f"\tA média é {media}")

# O "if" e "else" são condicionais, e você pode tomar decisões. VVVVVVVV

if media >= 6:
    print("Parabéns! Você está aprovado!")
    
else: 
    print("Você está reprovado! Estude mais no ano que vem!")

notaTodas = (notaUm + notaDois + notaTres + notaQuatro)

print(f"\tA soma de todas as notas é: {notaTodas}")