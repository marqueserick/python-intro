
print("Bem-vindo ao jogo de adivinhação!!!")
numero_secreto = 55
chute = int(input("Digite um número: "))
print("Você digitou",chute)

if (numero_secreto == chute):
    print("Você acertou!!!")
else:
    print("Você errou :(")
