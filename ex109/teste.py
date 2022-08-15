import moeda

p = float(input("Digite p preço: R$"))

print(f"De {moeda.moeda(p)} com aumento sai {moeda.aumentar(p, 80)}")
print(f"De {moeda.moeda(p)} com desconto sai: {moeda.diminuir(p, 15, True)}")
print(f"O dobro de {moeda.moeda(p)} é {moeda.dobro(p, True)}")
print(f"A metade de {moeda.moeda(p)} é {moeda.metade(p, True)}")

