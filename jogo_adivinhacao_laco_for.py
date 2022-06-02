print("Bem-vindo ao jogo de adivinhação!!!")
numero_secreto = 55
total_tentativas = 3
89
for rodada in range(1,(total_tentativas+1)):
    print("Tentativa {} de {}".format(rodada,total_tentativas))
    chute_str = input("Digite um número: ")
    chute = int(chute_str)
    acertou = numero_secreto == chute
    maior = chute>numero_secreto
    menor = chute<numero_secreto

    print("Você digitou",chute)

    if (acertou):
        print("Você acertou!!!")
        break;
    else:
        print("Você errou!!! :(", end=" ")
        if(maior):
            print("Seu chute foi maior que o número secreto")
        elif(menor):
            print("Seu chute foi menor que o número secreto")
else:
    print("Fim de Jogo")