
def leiaInt(msg):

    while True:

       try:
        n = int(input(msg))

       except(ValueError, TypeError):
           print("Digite um número inteiro válido")
           continue

       except KeyboardInterrupt:
           print("O usuário prefiriu não informar os dados")

       except Exception as erro:
           print(f"O ereo encontrado foi {erro.__cause__}")

       else:
           return n


def linha(tam=42):
    return '-' * tam


def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabecalho("MENU")
    c = 1
    for item in lista:
        print(f"{c} - {item}")
        c+=1

    print(linha())
    opc = leiaInt("Sua opção: ")
    return opc




