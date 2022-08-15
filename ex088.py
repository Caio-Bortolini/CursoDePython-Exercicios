print('-'*20)
print("SORTEIO MEGA SENNA")
print('-'*20)

import random

#x = random.sample(range(1,60),6)

#temp = []

princi = []

qtdJogos = int(input("Quantos jogos você quer que eu soreteie?: "))
print(f'----- Sorteando {qtdJogos} jogos -----')

for i in range(1,qtdJogos+1):
    princi = [random.sample(range(1,60),6)]
    #princi.append(temp[:])
    #temp.clear()



    print(f"Jogo {i}: {princi}")

princi.sort()
