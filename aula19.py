
pessoas = {'Nome': 'Caio', 'Sobrenome': 'Bortolini', 'Sexo': 'M', 'Idade': 21}

#print(pessoas)
#print(pessoas['Nome'])
#print(pessoas['Sexo'])

print(f'O {pessoas["Nome"]} tem {pessoas["Idade"]} anos')

#print(pessoas.keys())
#print(pessoas.values())
#print(pessoas.items())

#for k in pessoas:
    #print(f"{k}")

pessoas['Nome'] = 'Antonio'
pessoas['Peso'] = 90 #nao precisa de append

del pessoas['Sexo']

for k, v in pessoas.items():
    print(f"{k} = {v}")


