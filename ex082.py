
listaP = []
pares = []
impares = []

while True:
    num = (int(input("Digite um número: ")))
    listaP.append(num)

    if num %2 ==0:
        pares.append(num)
    else:
        impares.append(num)

    option = str(input("Deseja continuar? [S/N]: "))
    if option in "Nn":
        break


print(f"A lista completa é: {listaP}")
print(f"A lista de pares é: {pares}")
print(f"A lista de ímpares é: {impares}")

