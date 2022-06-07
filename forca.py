import random as rd

def jogar():
    print("Bem-vindo ao jogo de Forca")

    erros = 0
    acertou = False
    mascara = "_"
    total_tentativas = 7

    palavra_secreta = carrega_palavra_secreta()

    letras_acertadas = inicia_letras_acertadas(palavra_secreta, mascara)

    print("Palavra secreta:",palavra_mascarada(letras_acertadas), end="\n\n")

    while(not acertou):
        print("Resta(m) {} tentativa(s)".format((total_tentativas-erros)))
        chute = recebe_chute()
        
        if chute in palavra_secreta:
            letras_acertadas = verifica_chute(palavra_secreta, chute, letras_acertadas)
            acertou = mascara not in letras_acertadas
            if acertou:
                print("Parabéns, você descobriu a palavra secreta")
                mostrar_resultado(1)
        else:
            erros+=1
            desenha_forca(erros)

        if enforcou(erros, total_tentativas):
            print("Você foi enforcado")
            print("A palavra secreta era {}".format(palavra_secreta))
            mostrar_resultado(0)
            break;
        else:
            print(palavra_mascarada(letras_acertadas), end="\n\n")
    else:
        print("Fim de jogo!")

def palavra_mascarada(palavra):
    mascara =""
    for p in palavra:
        mascara = mascara + p + " "
    return mascara
    
def carrega_palavra_secreta():
    arquivo = open("palavras.txt", "r", encoding="UTF-8")
    palavras = [linha for linha in arquivo]
    arquivo.close()
    return palavras[rd.randrange(0, len(palavras))].strip().upper()

def inicia_letras_acertadas(palavra, mascara):
    return [mascara for p in palavra]

def recebe_chute():
    chute = input("Escolha uma letra... ").upper().strip()
    return chute[0] if len(chute)>1 else chute

def verifica_chute(palavra, chute, letras_acertadas):
    for i in range(len(palavra)):
        if palavra[i] == chute:
            letras_acertadas[i] = chute
    return letras_acertadas

def enforcou(erros, total_tentativas):
    return erros == total_tentativas

def mostrar_resultado(venceu):
    if venceu == 0:
        print("    _______________         ")
        print("   /               \       ")
        print("  /                 \      ")
        print("//                   \/\  ")
        print("\|   XXXX     XXXX   | /   ")
        print(" |   XXXX     XXXX   |/     ")
        print(" |   XXX       XXX   |      ")
        print(" |                   |      ")
        print(" \__      XXX      __/     ")
        print("   |\     XXX     /|       ")
        print("   | |           | |        ")
        print("   | I I I I I I I |        ")
        print("   |  I I I I I I  |        ")
        print("   \_             _/       ")
        print("     \_         _/         ")
        print("       \_______/           ")
    else:
        print("Parabéns, você ganhou!")
        print("       ___________      ")
        print("      '._==_==_=_.'     ")
        print("      .-\\:      /-.    ")
        print("     | (|:.     |) |    ")
        print("      '-|:.     |-'     ")
        print("        \\::.    /      ")
        print("         '::. .'        ")
        print("           ) (          ")
        print("         _.' '._        ")
        print("        '-------'       ")

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()


if __name__ == "__main__":
    jogar()
