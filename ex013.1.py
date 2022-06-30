#desconto em formas de pagamento

print("Insnira o valor para saber os descontos em cada forma de pagamento.")

valor = float(input("Valor: R$"))

avista = valor *10/100
debito = valor *5/100
aprazo = valor *10/100

fimAvista = valor - avista
fimDebito = valor - debito
fimAprazo = valor + aprazo

print("Pagamento à vista: R${:.2f}\nPagamento no débito: R${:.2f}\nA prazo, parcelado: R${:.2f}".format(fimAvista, fimDebito, fimAprazo))

