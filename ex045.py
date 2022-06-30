#GAME:Pedra papel tesoura

from random import randint
from time import sleep

itens = ('Pedra','Papel','Tesoura')

computador = randint(0,2)

print('''Suas opçoes:
[0] Pedra
[1] Papel
[2] Tesoura''')

jogador = int(input("Qual sera a sua jogada? "))

print("JO")
sleep(1)
print("KEN")
sleep(1)
print("PO")


print("-="*10)
print("O computador jogou {}".format(itens[computador]))
print("O jogador jogou {}".format(itens[jogador]))
print("-="*10)

#if jogador == computador:
 #   print("EMPATE!!")

if computador == 0:
    if jogador == 0:
        print("EMPATE")
    elif jogador ==1:
        print("JOGADOR VENCEU!!")
    elif jogador ==2:
        print("COMPUTADOR VENCEU!!")
    else:
        print("Jogada inválida")

elif computador == 1:
    if jogador == 0:
        print("COMPUTADOR VENCEU!!")
    elif jogador == 1:
        print("EMPATE")
    elif jogador == 2:
        print("JOGADOR VENCEU!!")
    else:
        print("Opção inválida")

elif computador == 2:
     if jogador == 0:
         print("JOGADOR VENCEU!!")
     elif jogador == 1:
         print("COMPUTADOR VENCEU!!")
     elif jogador == 2:
         print("EMPATE")
     else:
         print("Opção inválida")




