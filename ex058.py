from random import randint
'''tentativas = 0
computador = randint(0,10)

acertou = False

while not acertou:
    jogador = int(input("Qual é o seu palpite? "))
    tentativas += 1

    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print("Mais... Tente novamente")
        elif jogador > computador:
            print("Menos... Tente novamente")

#if computador == jogador:
 #   print("Voce conseguiu")


print("Fim")
print("Acertou com {} tentativas".format(tentativas))'''



computador = randint(0,10)
jogador = int(input("Qual é o seu palpite? "))

tentativas = 1

while jogador != computador:
    jogador = int(input("Qual é o seu palpite? "))
    tentativas +=1

    if jogador < computador:
        print("Mais... Try again")
    elif jogador > computador:
        print("Menos... Try again")
    elif jogador == computador:
        print("Acertou!!")




print("Voce tentou {} vezes até conseguir".format(tentativas))


