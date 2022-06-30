
numero = int(input("Digite um núemro ou [999] para finalizar: "))

cont = 0
soma = numero
fim = 999


while numero != 999:
    numero = int(input("Digite um núemro ou [999] para finalizar: "))

    soma = soma + numero

    cont +=1

    if numero == 999:
        soma = soma - fim


print("Voce digitou {} números. E a soma deles foi : {}".format(cont,soma))

