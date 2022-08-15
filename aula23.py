try:
    valor1 = int(input("Digite um número:"))
    valor2 = int(input("Digite mais um: "))
    r = valor1 / valor2
except:
    print("Houve um problema. Sinto muito")


else:
    print(f"O resultado é {r}")

finally:
    print("Volte sempre. Obrigado")

#################################################################

try:
    valor1 = int(input("Digite um número:"))
    valor2 = int(input("Digite mais um: "))
    r = valor1 / valor2
except Exception as erro:
    print(f"Problema encontrado: {erro.__class__}. Sinto muito")

else:
    print(f"O resultado é {r}")

finally:
    print("Volte sempre. Obrigado")

#####################################################################

try:
    valor1 = int(input("Digite um número:"))
    valor2 = int(input("Digite mais um: "))
    r = valor1 / valor2

except (ValueError, TypeError):
    print("Tivemos um problema com os tipos de dados que voce digitou")
except ZeroDivisionError:
    print("Não é possível dividir um número por 0")
except KeyboardInterrupt:
    print("Usuário preferiu não infromar os dados")
except Exception as erro:
    print(f"O erro encontrado foi {erro.__cause__}")

else:
    print(f"O resultado é {r}")

finally:
    print("Volte sempre. Obrigado")


