
numeros = (int(input("Digite um número:")),
           int(input("Mais um número: ")),
           int(input("Outro número: ")),
           int(input("Ultimo número: ")))

print(f"Voce digitou os valores {numeros}")

print(f"Quantas vezes apareceu o valor 9: {numeros.count(9)} vezes")

if 3 in numeros:
    print(f"O valor 3 apareceu na {numeros.index(3)+1}ºposição")
else:
    print("Número 3 não encontrado")

print(f"Os valores pares digitados foram", end=' ')
for n in numeros:
    if n %2==0:
        print(n, end=' ')





