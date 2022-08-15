from random import randint
from time import sleep
from operator import itemgetter

resultados = {'Jogador1': randint(1,6),
              'Jogador2': randint(1,6),
              'Jogador3': randint(1,6),
              'Jogador4': randint(1,6)}

ranking = []

print("VALORES SORTEADOS:")

for k, v in resultados.items():
    print(f"Jogador {k} tirou {v} no dado")
    sleep(1)

ranking = sorted(resultados.items(), key=itemgetter(1), reverse=True)

for i, v in enumerate(ranking):
    print(f"{i+1}º lugar: {v[0]} com {v[1]}")
    sleep(1)
