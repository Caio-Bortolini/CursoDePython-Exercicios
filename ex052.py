#Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

cont = 0

num = int(input("Digite um número: "))

for i in range(0, num + 1):
    if num % 2 == 0:
     cont = cont + 1
print("O número {} foi divisivel {} vezes".format(num, cont))
