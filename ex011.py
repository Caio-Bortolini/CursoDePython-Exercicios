#pintando a parede

larg = float(input("Qual é a largaura da sua parede? "))
alt = float(input("Qual a altura da sua parede? "))
area = larg*alt

print("Sua parede tem a dimensão de {} x {}, e possuí uma área de {} m²".format(larg,alt,area))

tinta = area/2
print("Voce precisa de {:2}L de tinta".format(tinta))



