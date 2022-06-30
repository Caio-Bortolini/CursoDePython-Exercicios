#Exercício Python 28: Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint
from time import sleep

sorteio = randint(0,5)
chute = int(input("Que número vc acha que o computador escolheu? "))

print("PROCESSANDO...")
sleep(2)

print("O computador escolheu o: {}\n Voce escolheu o numero: {}".format(sorteio, chute))

if sorteio == chute:
    print("Parabéns voce acertou")
else:
    print("Voce errou! Tente novamente.")

#print(sorteio)



