#gerenciador de pagamentos

valor = float(input("Qual é o valor da compra? R$:"))
print("Selecione a forma de pagamento\n[ 1 ] à vista dinheiro/cheque"
      "\n[ 2 ] a vista no cartao"
      "\n[ 3 ] 2x no cartão (preço formal)"
      "\n[ 4 ] 3x ou mais no cartão")

opcao = int(input("Selecione a opção: "))

if opcao == 1:
    desconto = (valor *10/100)
    descontoFinal = valor - desconto
    print("De R${} ficou por R${:.2f}".format(valor,descontoFinal))

elif opcao == 2:
    desconto = (valor *5/100)
    descontoFinal = valor - desconto
    print("De R${} ficou por R${:.2f}".format(valor,descontoFinal))

elif opcao == 3:
    print("Ficou por R${:.2f}".format(valor))

elif opcao == 4:
    juros = (valor *20/100)
    jurosFinal = valor + juros
    print("De R${} ficou por R${:.2f}".format(valor,jurosFinal))

else:
    print("Digite uma opção válida!")






