import random

def jogar():
    print("*********************************")
    print("Bem vindo ao jogo de adivinhação!")
    print("*********************************")

    numero_secreto = random.randrange(1, 101)
    total_de_tentativas = 0
    pontos = 1000

    print("Qual o nível de dificuldade você quer?")
    print("(1)Fácil (2)Médio (3)Difícil")

    nivel = int(input("Defina o nível: "))

    if(nivel == 1):
        total_de_tentativas = 20
    elif(nivel == 2):
        total_de_tentativas = 10
    elif(nivel == 3):
        total_de_tentativas = 5
    else:
        print("escolha uma dificuldade digitando entre 1 e 3!")

    for rodada in range(1, total_de_tentativas + 1):

        print("tentativa {} de {}".format(rodada, total_de_tentativas))

        chute_str = input("Digite um número entre 1 e 100: ")
        print("Você digitou", chute_str)
        chute = int(chute_str)

        if(chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100!")
            continue

        igual = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if(igual):
            print("Você acertou e fez {} pontos!". format(pontos))
            break
        else:
            if(maior):
                print("Você errou! Um pouco menos :)!")
            elif(menor):
                print("Você errou! Um pouco mais :)!!")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos

    print("*********************************")
    print("*********Fim do jogo!************")
    print("*********************************")

if(__name__ == "__main__"):
    jogar()