#conversor de moedas

reais = float(input("Quantos reais você tem na carteira? R$"))

dolar = reais/5.17
euro = reais/5.40
libra = reais/ 6.31
btc =  reais /162.2

print("Com {:.2f} reais, você pode comprar {:.2f} Dolares".format(reais,dolar))

print("Com {:.2f} reais, você pode comprar {:.2f} Euros".format(reais,euro))

print("Com {:.2f} reais, você pode comprar {:.2f} Libras".format(reais,libra))

print("Com {:.2f} reais, você pode comprar {:.7f} Bitcoins".format(reais,btc))

