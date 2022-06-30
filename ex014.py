#conversor de temperatura

temperaturaC = float(input("Informe a temperatura em Cº: "))

farenheit = temperaturaC *1.8 +32

kelvin = temperaturaC + 273

print("{}ºC correspondem à: {}°F e {}K".format(temperaturaC, farenheit, kelvin))

