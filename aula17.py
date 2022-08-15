num = [1, 3, 7, 9]
num[0] = 33
num.append(222)
num.insert(2,8)
#num.sort(reverse=True)
#num.pop(2) sem parametro elimina o ultimo
if 33 in num:
    num.remove(33)
print(num)

print("=-"*15)

print(f"Essa lista tem {len(num)} elementos")

valores = []

valores.append(5)
valores.append(7)
valores.append(2)

print("=-"*15)

for v in valores:
    print(f"Os valores são {v}...")
print("=-"*15)

for c, v in enumerate(valores):
    print(f"Na posição {c} encontrei {v}")
print("=-"*15)

for cont in range(0,3):
    valores.append(int(input(f"Digite o {cont} valor: ")))

print(valores)
