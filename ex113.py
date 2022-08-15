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



def leiaFloat(msg):

    while True:
        try:
            n = float(input(msg))

        except(ValueError, TypeError):
            print("Digite apenas número float")
            continue
        except KeyboardInterrupt:
            print("O usuário preferiu não informar os dados.")
            return 0
        except Exception as erro:
            print(f"Foi encontrado o seguinte erro: {erro.__cause__}")
        else:
            return n





num = leiaInt("Digite um número inteiro: ")
print(f"voce digitou o número {num}")

num2 = leiaFloat("Digite um número float: ")
print(f"Voce digitou o número {num2}")

