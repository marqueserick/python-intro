import adivinhacao

print("""#######################
Bem-vindo ao menu de jogos
#######################""")
op = input("Pressione 1 para jogar o Adivinhação")
if op =='1':
    adivinhacao.jogar()
else:
    print("Fechando o menu de jogos...")