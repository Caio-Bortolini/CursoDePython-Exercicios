
dados = {}
lista = []
soma = media = 0
while True:
    dados['Nome'] = str(input("Nome: "))
    dados['Idade'] = int(input("Idade: "))
    soma += dados['Idade']
    dados['Sexo'] = str(input("Sexo: [M/F]: ")).upper()

    lista.append(dados.copy())




    while dados['Sexo'] != "M" and dados['Sexo'] != "F":
        print("Responda apenas [F ou M]")
        dados['Sexo'] = str(input("Sexo: [M/F]: ")).upper()

    opt = str(input("Quer continuar? [S/N]: ")).upper()

    while opt != 'N' and opt !='S':
        print("Responda apenas [S ou N.]")
        opt = str(input("Quer continuar? [S/N]: ")).upper()

    if 'N' in opt:
        break

media = soma / len(lista)

print(lista)

print(f"Ao todo temos {len(lista)} pessoas")

print(f"A media de idade entre as pessoas é de {media}")

print(f"As mulheres cadastradas foram ", end=' ')

for p in lista:
    if p['Sexo'] == 'F':
        print(f"{p['Nome']}")

print(f"Pessoas acima da media")
for p in lista:
    if p['Idade'] >= media:
        print('   ')
        for k, v in p.items():
            print(f"{k} = {v};", end='')

print("<<< ENCERRADO >>>")



