import forca
import adivinhacao

def escolher_jogo():
    print("*********************************")
    print("*********Escolha o jogo!*********")
    print("*********************************")

    print("(1)Forca (2)Adivinhação")

    jogo = int(input("Qual o jogo você quer? "))

    if(jogo == 1):
        print("Jogando Forca!")
        forca.jogar()
    elif(jogo == 2):
        print("Jogando Adivinhação!")
        adivinhacao.jogar()
    else:
        print("Escolha 1 ou 2!")

if(__name__ == "__main__"):
    escolher_jogo()
