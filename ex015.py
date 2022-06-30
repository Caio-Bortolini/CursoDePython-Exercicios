#aluguel de carros

qtdKM = float(input("Quantos KM você pretende rodar? "))
qtdDias = float(input("Quantos dias vai ficar o carro? "))

KmRodado = qtdKM *0.15
diausado = qtdDias *60

print("Por {} dias , ficaria por R${:.2f}\nPor {}km rodados, ficaria por R${}".format(qtdDias, diausado, qtdKM, KmRodado))






#Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.