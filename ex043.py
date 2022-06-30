#IMC

altura = float(input("Altura: "))
peso = float(input("Peso Kg: "))

imc = peso / (altura**2)

if imc <18.5:
    print("Seu IMC é de {:.1f}\nVoce esta abaixo do peso.".format(imc))
elif imc <25:
    print("Seu IMC é de {:.1f}\n Voce esta com o peso ideal".format(imc))
elif imc <30:
    print("Seu IMC é de {:.1f}\n Voce esta com Sobrepeso".format(imc))
elif imc <40:
    print("Seu IMC é de {:.1f}\n Voce esta com Obesidade".format(imc))
elif imc >40:
    print("Seu IMC é de {:.1f}\n Voce esta com Obesidade morbida".format(imc))

