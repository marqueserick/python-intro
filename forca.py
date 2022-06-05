import random as rd
def jogar():
    print("Bem-vindo ao jogo de Forca")
    arquivo = open('palavras.txt', 'r')
    palavras = [linha for linha in arquivo]
    palavra_secreta = palavras[rd.randrange(0, len(palavras))].strip().upper()
    letras_acertadas = ["_" for p in palavra_secreta]
    erros = 0
    enforcou = False
    acertou = False

    print("Palavra secreta:",palavra_mascarada(letras_acertadas), end="\n\n")

    nivel = input("Selecione um nível de dificuldade\n(1) Fácil (2) Médio (3) Difícil\n")
    if nivel == '1':
        total_tentativas = 7
    elif nivel == '2':
        total_tentativas = 5
    elif nivel == '3':
        total_tentativas = 3
    else:
        total_tentativas = 1

    while(not enforcou and not acertou):
        print("Resta(m) {} tentativa(s)".format((total_tentativas-erros)))
        chute = input("Escolha uma letra... ").upper()
        if len(chute) > 1:
            chute = chute.strip()[0]
        
        if chute in palavra_secreta:
            for i in range(len(palavra_secreta)):
                if palavra_secreta[i] == chute:
                    letras_acertadas[i] = chute
                    acertou = "_" not in letras_acertadas
                    if acertou:
                        print("Parabéns, você descobriu a palavra secreta")
        else:
            erros+=1
            if erros == total_tentativas:
                print("Você foi enforcado")
                enforcou = True

        if enforcou:
            print("A palavra secreta era {}".format(palavra_secreta))
        else:
            print(palavra_mascarada(letras_acertadas), end="\n\n")
    else:
        print("Fim de jogo!")

def palavra_mascarada(palavra):
    mascara =""
    for p in palavra:
        mascara = mascara + p + " "
    return mascara
if __name__ == "__main__":
    jogar()