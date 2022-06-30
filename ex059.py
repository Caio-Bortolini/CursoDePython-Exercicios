# menu de opções

valor1 = int(input("Primeiro valor: "))
valor2 = int(input("Segundo valor: "))

print("[ 1 ] SOMAR\n[ 2 ] MULIPLICAR\n[ 3 ] MAIOR\n[ 4 ] NOVOS NÚMEROS\n[ 5 ] SAIR DO PROGRAMA")

opcao = int(input("Informe a opção desejada: "))
soma = 0
mult = 0
maior = 0


while not opcao == 5:

    if opcao == 1:
        soma = valor1 + valor2
        print("A soma entre {} e {} é: {}".format(valor1,valor2,soma))

    elif opcao == 2:
        mult = valor1*valor2
        print("A multiplicação entre {} e {} é: {}".format(valor1,valor2,mult))

    elif opcao == 3:
        maior = valor1
        if maior > valor2:
            maior = valor1
        else:
            maior = valor2
        print("Maior número é o: {}".format(maior))

    elif opcao == 4:
        valor1 = int(input("Primeiro valor: "))
        valor2 = int(input("Segundo valor: "))
    else:
        print("Opção inválida. Tente novamente.")




    print("[ 1 ] SOMAR\n[ 2 ] MULIPLICAR\n[ 3 ] MAIOR\n[ 4 ] NOVOS NÚMEROS\n[ 5 ] SAIR DO PROGRAMA")
    opcao = int(input("Informe a opção desejada: "))

print("Voce saiu do programa")
