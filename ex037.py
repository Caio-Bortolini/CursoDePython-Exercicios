#conversor de bases numericas

inteiro = int(input("Digite um número inteiro: "))

print("Escolha uma das opções\n[1] Converter para binário\n[2] Converter para octal\n[3] Converter para hexadecimal")

escolhido = int(input("Opção: "))

#binario = bin(inteiro)
octal = oct(inteiro)
hexadecimal= hex(inteiro)

if escolhido == 1:
    print("{} em binário é: {}".format(inteiro, bin(inteiro)[2:]))
elif escolhido == 2:
    print("{} em octal é: {}".format(inteiro, octal[2:]))
elif escolhido == 3:
    print("{} em hexadecimal é: {}".format(inteiro, hexadecimal[2:]))
else:
    print("Opção não encontrada.")
