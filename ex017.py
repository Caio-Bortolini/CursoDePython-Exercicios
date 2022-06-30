#caetos e hipotenusa

from math import hypot

co = float(input("Comprimento do cateto oposto: "))
ca = float(input("Comprimento do cateto adjacente: "))
hipo = hypot(co, ca)

print("O valor da hipotenusa é {:.2f}".format(hipo))
