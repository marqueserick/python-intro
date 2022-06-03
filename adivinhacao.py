import random as rd
def jogar():
    print("Bem-vindo ao jogo de adivinhação!!!")
    #numero_secreto = int(rd.uniform(0,1)*100)
    #numero_secreto = rd.randint(1,100)
    numero_secreto = rd.randrange(1,101)
    pontos = 1000
    pontos_perdidos = 0

    nivel = input("Selecione um nível de dificuldade\n(1) Fácil (2) Médio (3) Difícil\n")
    if nivel == '1':
        total_tentativas = 10
    elif nivel == '2':
        total_tentativas = 5
    elif nivel == '3':
        total_tentativas = 3
    else:
        total_tentativas = 1

    constante_precisao = 10 / total_tentativas

    for rodada in range(1,(total_tentativas+1)):
        print("Tentativa {} de {}".format(rodada,total_tentativas))
        chute_str = input("Digite um número de 1 a 100: ")
        chute = int(chute_str)

        if chute < 1 or chute > 100:
            pontos_perdidos += (100 * constante_precisao)
            print("Você deve digitar um número entre 1 e 100", end="\n\n")
            continue

        if numero_secreto == chute:
            print("Você acertou!!!")
            print("Sua precisão foi de {:.2f}%".format(precisao(pontos, pontos_perdidos)))
            break

        else:
            pontos_perdidos += (abs(chute-numero_secreto) * constante_precisao)
            print("Você errou!!! :(", end=" ")
            if chute > numero_secreto:
                print("O número secreto é menor que", chute, end="\n\n")

            elif chute < numero_secreto:
                print("O número secreto é maior que", chute, end="\n\n")
    else:
        print("Fim de Jogo\nO número secreto era {}".format(numero_secreto))
        print("Sua precisão foi de {:.2f}%".format(precisao(pontos, pontos_perdidos)))


def precisao(pontos, pontos_perdidos):
        return  abs((pontos - pontos_perdidos) * 100 / pontos)

if __name__ == "__main__":
    jogar()