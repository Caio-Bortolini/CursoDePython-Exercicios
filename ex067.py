print("="*30)
while True:
    numero = int(input("Qual tabuada deseja saber?: "))
    if numero <0:
        print("Programa encerrado!")
        break
    for i in range(1,11):
        tabaudada = numero*i

        print(f"{numero} x {i} = {tabaudada}")

    print("="*30)

