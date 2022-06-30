#Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
from datetime import datetime
atual = datetime.today().year

totMAior = 0
totMenor = 0


for i in range(1,5):
    nascimento = int(input("Em que ano a {}º pessoa nasceu? ".format(i)))
    idade = atual - nascimento

    if idade >= 18:
        totMAior = totMAior +1
    else:
        totMenor = totMenor +1

print("Ao todo tivemos {} pessoas menores de idade\nE {} pessoas maiores de idadade.".format(totMenor, totMAior))