
num = [[], []]

for i in range(1,8):
    valor = (int(input(f"Digite o {i}o número: ")))

    if valor %2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)


print(num)

num[0].sort()
num[1].sort()

print(f"Valores pares {num[0]}")
print(f"Valores impares {num[1]}")


