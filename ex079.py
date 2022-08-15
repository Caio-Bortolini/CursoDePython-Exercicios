num = []

while True:

    n = int(input("Digite um número: "))
    if n not in num:
        num.append(n)
        print("Valor adicionado com sucesso!!")
    else:
     print("Valor duplicado. Não vou adicionar.")



    option = str(input("Quer continuar? [S/N]: "))


    if option in 'Nn':
        break


print(sorted(num))



