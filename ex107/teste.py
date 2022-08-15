import moeda

p = float(input("Digite p preço: R$"))

print(f"De {p} com aumento sai {moeda.aumentar(p, 80)}")
print(f"De {p} com desconto sai: {moeda.diminuir(p, 15)}")
print(f"O dobro de {p} é {moeda.dobro(p)}")
print(f"A metade de {p} é {moeda.metade(p)}")

