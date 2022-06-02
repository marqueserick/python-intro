import random as rd
print("Bem-vindo ao jogo de adivinhação!!!")
#numero_secreto = int(rd.uniform(0,1)*100)
#numero_secreto = rd.randint(1,100)
numero_secreto = rd.randrange(1,101)

nivel = input("Selecione um nível de dificuldade\n(1) Fácil (2) Médio (3) Difícil\n")
if nivel == '1':
    total_tentativas = 10
elif nivel == '2':
    total_tentativas = 5
elif nivel == '3':
    total_tentativas = 3
else:
    total_tentativas = 1

for rodada in range(1,(total_tentativas+1)):
    print("Tentativa {} de {}".format(rodada,total_tentativas))
    chute_str = input("Digite um número de 1 a 100: ")
    chute = int(chute_str)
    acertou = numero_secreto == chute
    maior = chute>numero_secreto
    menor = chute<numero_secreto

    print("Você digitou",chute)

    if chute < 1 or chute > 100:
        print("Você deve digitar um número entre 1 e 100", end="\n\n")
        continue

    if (acertou):
        print("Você acertou!!!")
        break

    else:
        print("Você errou!!! :(", end=" ")
        if(maior):
            print("Seu chute foi maior que o número secreto", end="\n\n")

        elif(menor):
            print("Seu chute foi menor que o número secreto", end="\n\n")
else:
    print("Fim de Jogo\nO número secreto era {}".format(numero_secreto))