
numero = cont = s = 0

while True:
    numero = int(input("Digite um numero ou (999 para finalizar): "))
    if numero == 999:
        break
    cont+=1
    s+= numero

print(f"Foram {cont} números digitados com a soma de {s}")

