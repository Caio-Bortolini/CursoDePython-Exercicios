def ficha(jog='<anonimo>', gol=0):
    print(f"o jogador {jog} fez {gol} Gol(s) no campeonato")


n = str(input("Nome do jogador: "))
g = str(input("Quantos gols? : "))

if g.isnumeric():
    g = int
else:
    g = 0

if n.strip() == '':
    ficha(gol=g)
else:
    ficha(n, g)

