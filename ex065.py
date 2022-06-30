
numero = int(input("Digite um número: "))

opcao = str(input("Quer continuar? S/N: ")).upper()

cont = 1
soma = numero

maior = 0
menor = 0

while opcao == 'S':
    numero = int(input("Digite um número: "))
    opcao = str(input("Quer continuar? S/N: ")).upper()
    cont+=1
    soma = soma + numero
    media = soma / cont

    if cont ==1:
        maior = menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero




    if opcao != 'S' and opcao !='N':
        print("Digite apenas S ou N")

print("Voce digitou {} números. E a média foi {:.2f}".format(cont, media))
print("O menor número digitado foi o {} e o maior {}".format(menor, maior))



