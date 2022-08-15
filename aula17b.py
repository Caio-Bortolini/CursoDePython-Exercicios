
teste = []
teste.append('Caio')
teste.append(21)


galera = []
galera.append(teste[:])
print(galera)

teste[0] = 'Maria'
teste[1] = 18
print(teste)

galera.append(teste)
print(galera)


