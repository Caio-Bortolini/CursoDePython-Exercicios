somaIdade = 0
mediaIdade = 0
maiorIdadeHomem = 0
nomeVelho = ''
menorIdadeMulher = 0
contMulher = 0


for i in range(1, 5):
    print("--- {}º PESSOA ---".format(i))
    nome = str(input("Digite seu nome: "))
    idade = int(input("Digite sua idade: "))
    sexo = str(input("Sexo [M/F]? ")).upper()
    somaIdade += idade

    mediaIdade = somaIdade / 4

    if i == 1 and sexo in'Mm':
        maiorIdadeHomem = idade
        nomeVelho = nome
    if sexo in 'Mm' and idade > maiorIdadeHomem:
        maiorIdadeHomem = idade
        nomeVelho = nome

    if i == 1 and sexo in 'Ff':
        menorIdadeMulher = idade

    if sexo in 'Ff' and idade < 20:
        menorIdadeMulher = idade
        contMulher = contMulher + 1



print("Media das idades das {} pessoas é de {}".format(i,mediaIdade))
print("O nome do homem mais velho é {} e sua idade é de {} anos".format(nomeVelho, maiorIdadeHomem))
print("A quantidade de mulheres menores de 20 anos é de {}".format(contMulher))
