import moeda

p = float(input("Digite p preço: R$"))

print(f"De {moeda.moeda(p)} com aumento sai {(moeda.moeda(moeda.aumentar(p, 80)))}")
print(f"De {moeda.moeda(p)} com desconto sai: {moeda.moeda(moeda.diminuir(p, 15))}")
print(f"O dobro de {moeda.moeda(p)} é {moeda.moeda(moeda.dobro(p))}")
print(f"A metade de {moeda.moeda(p)} é {moeda.moeda(moeda.metade(p))}")

