#comparando numeros

num1 = int(input("Digite o primeiro numero: "))
num2 = int(input("Digite o segundo número: "))

if num1 > num2:
    print("O primeiro número é maior")
elif num2 > num1:
    print("O segundo número é maior")
elif num1 == num2 and num2 ==num1:
    print("Os números são iguais")
