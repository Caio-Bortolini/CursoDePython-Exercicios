#Faça um programa que calcule a soma entre todos os números que são múltiplos de três e que se encontram no intervalo de 1 até 500.
cont = 0
soma = 0
for i in range(1, 501, 2):
    if i % 3 == 0:  #se o contador for divisivel por 3
        cont = cont + 1  #(contador de quantos numeros sao divisiveis por 3)
        #cont += 1
        soma = soma + i #soma recebe o que ela tem, mais o numero (acumulador)/ soma de todos os divisiveis por 3
        #soma += i

print("A soma de {} valores solicitados é {}".format(cont,soma))









