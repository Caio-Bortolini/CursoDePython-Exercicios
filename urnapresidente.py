print("Voto para presidente\n[17]-Bolsonaro\n[13]-Lula\n[40]-Sergio Moro\n[56]-Ciro Gomes")

voto = int(input('Para quem deseja votar? '))
print("Obrigado por votar")
if voto == 17:
    print("Voce votou em Bolsonaro, capitão da reserva do exército.")
elif voto == 13:
    print("Voce votou no Lula, bandido e ex presidiário. Voce é um idiota e burro pra caralho!!")
elif voto == 40:
    print("Voce votou em Sergio Morto, ex juiz do STF.")
elif voto == 56:
    print("Voce votou em Ciro Gomes, o estressadinho.")
else:
    print("Insira um número correto!")
