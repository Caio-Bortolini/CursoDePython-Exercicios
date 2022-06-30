distancia = int(input("Qual a distância em Km a ser percorrida? "))


if distancia <=200:
    viagemAte200 = distancia * 0.50
    print("Com a diststancia de {}Km, seram cobrados R$0,50 por Km para viagens de até 200Km\nVoce pagara: R${}".format(distancia, viagemAte200))

else:
    viagemMaisLonga = distancia * 0.45
    print("Com a diststancia de {}Km, seram cobrados R$045 por Km para viagens de mais longas que 200Km\nVoce pagara: R${}".format(distancia, viagemMaisLonga))
