
mais18 = 0
homens = 0
mulheremenos20 = 0

while True:
    print("-" * 30)
    print("CADASTRE UMA PESSOA")
    print("-" * 30)

    idade = int(input("Idade: "))
    #sexo = str(input("Sexo? [M/F]: ")).upper()
    #opcao = str(input("Quer continuar? [S/N]: ")).upper()

    sexo = ' '
    opcao = ' '

    while sexo not in 'MF':
        sexo = str(input("Sexo? [M/F]: ")).upper()

    while opcao not in 'SN':
        opcao = str(input("Quer continuar? [S/N]: ")).upper()


    if idade > 18:
        mais18+=1
    if idade < 20 and sexo =='F':
        mulheremenos20+=1
    if sexo == 'M':
        homens+=1

    if opcao == 'N':
        break

print(f'Total de pessoas com mais de 18 anos: {mais18}')
print(f'Ao todo temos {homens} homens cadastrado(s)')
print(f'E temos {mulheremenos20} mulher(s) com menos de 20 anos.')
