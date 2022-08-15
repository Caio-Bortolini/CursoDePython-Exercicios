def contador(inicio, fim, passo):
    if passo < 0:
        passo *= -1
    if passo == 0:
        passo = 1

    print(f"Contagem de {inicio} até {fim} de {passo} em {passo}")

    if inicio < fim:
        for cont in range(inicio, fim+1, passo):
            print(f"{cont}", end=' ')
        print()
    else:
        if inicio >= fim:
            for cont in range(inicio, fim-1, -passo):
                print(f"{cont}", end=' ')


#Programa principal

contador(0, 100, 10)
contador(10, 0, 2)

print("AGORA É SUA VEZ DE CONTAR!!")

ini = int(input("Inicio: "))
fimm = int(input("Fim: "))
passoo = int(input("Passo: "))

contador(ini, fimm, passoo)


