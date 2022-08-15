
jogador = {}
partidas = []

jogador['Nome'] = str(input("Nome: "))
tot = int(input(f"Quantas partidas {jogador['Nome']} jogou: "))

for c in range(1,tot+1):
    partidas.append(int(input(f"Quantos gols na partida {c}º: ")))

jogador['Gols'] = partidas[:]
jogador['Total'] = sum(partidas)

print(jogador)

for k, v in jogador.items():
    print(f"O campo {k} tem o valor {v}")

print(f"O jogador {jogador['Nome']} jogou {[len(jogador['Gols'])]} partidas.")

for k, v in enumerate(jogador['Gols']):
    print(f"Na partida {k} fez {v} gols")


