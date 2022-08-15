brasil = []
estado1 = {'uf': 'SP', 'Cidade': 'São Paulo'}
estado2 = {'uf': 'RJ', 'Cidade': 'Rio de Janeiro'}

print(estado1['uf'])

brasil.append(estado1)
brasil.append(estado2)
print(brasil)

print(brasil[0]['uf'])
############################################################################################################################

brazil = []
estados = {}

for c in range(0,3):

    estados['UF'] = str(input("Digite o estado (UF): "))
    estados['Sigla'] = str(input("Digite a Sigla: "))
    brazil.append(estados.copy())

print(brazil)
############################################################################################################################

for e in brazil:
    print(e)

############################################################################################################################

for e in brazil:
    for k, v in e.items():
        print(f"O campo {k} tem o valor {v}")
############################################################################################################################

for e in brazil:
    for v in e.values():
        print(f" {v}")

