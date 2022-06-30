salarioAtual = float(input("Digite seu salário atual: "))

if salarioAtual > 1250:

    novoSalario = (salarioAtual * 10) / 100
    reajuste = salarioAtual + novoSalario
    print("Quem ganhava R${:.2f}, agora passa a ganhar: R${:.2f}".format(salarioAtual, reajuste))
else:
    novoSalario = (salarioAtual * 15) / 100
    reajuste = salarioAtual + novoSalario
    print("Quem ganhava R${:.2f}, agora passa a ganhar: R${:.2f}".format(salarioAtual, reajuste))

conta = 19 % 2
print(conta)
