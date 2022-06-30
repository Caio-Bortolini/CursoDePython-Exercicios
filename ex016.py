#quebrando um número

from math import floor, ceil

num = float(input("Digite um número: "))
quebra = floor(num)
quebra2 = ceil(num)

print("O número  digitado foi: {} e sua porção inteira é: {}".format(num, quebra))
print("O número digitado foi:{} e sua porção arredondada é: {}".format(num, quebra2))

