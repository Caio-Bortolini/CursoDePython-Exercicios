# nome = str(input("Qual é o seu nome? "))

# if nome == "Caio":
#  print("Seu nome é lindo!!")
# else:
#   print("Seu nome é tão normal.")
# print("Bom dia, {}".format(nome))

n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
n3 = float(input("Digite a terceira nota: "))
n4 = float(input("Digite a quarta nota: "))
m = (n1 + n2 + n3 + n4) / 4
print("Sua média foi: {}".format(m))
if m >= 5:
    print("Parabéns voce foi aprovado!!")
else:
    print("Voce esta reprovado.")

