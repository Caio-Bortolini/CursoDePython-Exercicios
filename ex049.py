#tabauda

numero = int(input("Qual tabuada deseja saber? "))

soma = 0
cont = 0
for i in range(0,10, 1):
    cont = cont +1
    soma = numero * cont
    print("{} x {} = {}".format(numero, cont, soma))
