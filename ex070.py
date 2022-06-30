totalCompra = qtdPrduto1k = 0
nomeBarato = ''
cont = 0
menor = 0


while True:

    produto = str(input("Nome do produto: "))
    valor = float(input("Valor: R$ "))

    cont+=1

    opcao = ' '

    totalCompra += valor

    if totalCompra >1000:
        qtdPrduto1k+=1


    if cont ==1:
        menor = valor
        nomeBarato = produto
    else:
        if valor < menor:
            menor = valor
            nomeBarato = produto


    while opcao not in 'SN':
        opcao = str(input("Quer continuar? [S/N]: ")).upper()


    if opcao == 'N':
        break

print(f"Total gasto na compra: {totalCompra}")
print(f"Produtos com valor acima de mil reais: {qtdPrduto1k}")
print(f"Nome do produto mais barato: {nomeBarato} e custa R${menor}")

