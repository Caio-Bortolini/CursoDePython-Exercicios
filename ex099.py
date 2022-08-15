def lin():
    print("-="*30)


def analise(*num):
    lin()
    print("Análisandos os valores passados...")
    print(f"{num }. Foram informados {len(num)} números", end='')
    print(f" O maior valor informado foi o {max(num)}")


analise(2,5,6,8,9,20,4,1)
analise(2,3)

#OUTRA MANEIRA DE FAZER

def maior(*num):
    cont = maior = 0
    print("-="*30)
    print("Análisando os valores...")
    for valor in num:
        print(valor, end=' ')

        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont+=1
    print(f"Foram informados {cont} números")
    print(f"O maior valor informado foi {maior}")


maior(5,10)
maior(19,3,5,6,4,89)

