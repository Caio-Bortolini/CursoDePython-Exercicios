lista = []
dados = []
maior = 0
menor = 0

while True:

    lista.append(str(input("Digite seu nome: ")))
    lista.append(float(input("Seu peso: ")))

    if len(dados) == 0:
        maior = menor = lista[1]
    else:
        if lista[1] > maior:
            maior = lista[1]
        if lista[1] < menor:
            menor = lista[1]

    dados.append(lista[:])
    lista.clear()

    option = str(input("Deseja continuar? [S/N]: "))

    if option in "Nn":
        break


print(dados)

print(f"Foram cadastrados {len(dados)} pessoas")
print(f"O maior peso foi de {maior}kg. Peso de ", end='')
for p in dados:
    if p[1] == maior:
        print(f"{p[0]}", end='')

print(f"O menor peso foi de {menor}kg. Peso de ", end='')

for p in dados:
    if p[1] == menor:
        print(f"{p[0]}", end='')


