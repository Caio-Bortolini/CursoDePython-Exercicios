#calculando descontos

produto = float(input("Qual é o preço do produto? R$"))

desconto = produto *5/100
descontoFinal = produto - desconto

print("Com o desconto de 5% o valor: R${}, fica por R${:.2f}".format(produto,descontoFinal))
