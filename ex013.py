#reajuste de salario

print("Voce terá 15% de aumento no seu salário.\nDigite abaixo seu sálario atual para ver o novo salário.")

atual = float(input("Qual é o salário atual? "))

reajuste = atual *15/100

novoSalario = atual + reajuste

print("De R${}, agora com 15% de aumento, seu salário será R${:.2f}".format(atual,novoSalario))

