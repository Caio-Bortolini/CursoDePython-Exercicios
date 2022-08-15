
timesA = ('Palmeiras', 'Corinthians', 'Fluminense', 'Atléico MG', 'Atletico PR',
         'Flamengo', 'Internacional', 'Bragantino', 'Santos', 'São Paulo', 'Botafogo',
         'Ceara', 'Coritiba', 'America MG', 'Avai','Cuiaba', 'Atlico G','Juventude', 'Fortaleza')

print(f"O cinco primeiros são: {timesA[:5]}")
print('-'*20)
print(f"Os quatro ultimos colocados: {timesA[15:20]}")
print('-'*20)
print(f"Times em ordem Alfaética: {sorted(timesA)}")
print('-'*20)
print(f"Bragantino esta em: {timesA.index('Bragantino')+1}º")
