#Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.

soma = 0
cont = 0

#numeros = int(input("Digite o {} numero: ").format())

for i in range(1,7 ,1):
    #cont = cont + 1  ( o cont foi substituido pelo 'i')

    numeros = int(input("Digite o {}º numero: ".format(i)))

    if numeros % 2 ==0:
        soma = soma + numeros
        cont = cont +1

print("A soma dos {} números PARES é: {} ".format(cont, soma))







