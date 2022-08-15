lista = []

while True:
    lista.append(int(input("Digite um valor: ")))
    option = str(input("Quer continuar? [S/N]: ")).upper()

    if option not in "SN":
     print("Validos apenas [S/N]")
     option = str(input("Quer continuar? [S/N]: ")).upper()

    if "N" in option:
        break

print(f"Valores digitados: {lista}")

lista.sort(reverse=True)

print(f"Voce digitou {len(lista)} números")
print(f"Os valores em ordem decrescente: {lista}")

if 5 in lista:
    print("O valor 5 esta na lista")
else:
    print("Não tem valor 5 na lista")

