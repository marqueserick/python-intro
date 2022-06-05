from turtle import end_fill
import adivinhacao
import forca

print("""#######################
Bem-vindo ao menu de jogos
#######################""")
op = input("Pressione 1 para jogar Adivinhação\nPressione 2 para jogar Forca\n")
if op =='1':
    adivinhacao.jogar()
elif op =='2':
    forca.jogar()
else:
    print("Fechando o menu de jogos...")