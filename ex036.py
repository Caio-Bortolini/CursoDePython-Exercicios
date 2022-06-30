#emprestimo bancario

valorCasa = float(input("Valor do imóvel? R$"))
salarioComprador = float(input("Salário? R$"))
anosPagamento = int(input("Em quantos anos deseja pagar? "))
minimo = salarioComprador *30 /100          #30% do salario

parcelamento = valorCasa / (anosPagamento *12)

print("Para pagar uma casa de R${:.2f} em {} anos, a prestação será de R${:.2f} mensais".format(valorCasa,anosPagamento, parcelamento))
#print("Comprando tem que pagar R${:.2f}, o minimo é de R${:.2f}".format(parcelamento, minimo))

if parcelamento <=minimo: #menor ou igual a 30% do salario

    print("EMPRÉSTIMO CONCEDIDO, pois o valor da parcela não ultrapassa 30% do salário.")
else:
    print("EMPRÉSTIMO NEGADO, pois o valor da parcela ultrapassa 30% do seu salário!")

