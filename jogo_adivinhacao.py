print("Bem-vindo ao jogo de adivinhação!!!")
numero_secreto = 55
total_tentativas = 3

while(total_tentativas>0):
    chute_str = input("Digite um número: ")
    chute = int(chute_str)
    acertou = numero_secreto == chute
    maior = chute>numero_secreto
    menor = chute<numero_secreto

    print("Você digitou",chute)

    if (acertou):
        print("Você acertou!!!")
        break
    else:
        total_tentativas-=1
        print("Você errou!!! :(", end=" ")
        if(maior):
            print("Seu chute foi maior que o número secreto")
        elif(menor):
            print("Seu chute foi menor que o número secreto")
    print("Resta(m) {} tentativa(s)".format(total_tentativas))
else:
    print("Fim de Jogo")
