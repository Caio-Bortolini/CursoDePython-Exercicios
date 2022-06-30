#Faça um programa que leia um número qualquer e mostre o seu fatorial.

n = int(input("Digite um número para saber seu Fatorial: "))
c = n
f = 1

print("Calculando {}! = ".format(n), end='')
while c > 1:
    print("{} ".format(c), end='')
    print(" x " if c > 1 else " = ",end='')
    f=f*c
    c = c -1

print("{}".format(f))
