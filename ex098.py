from time import sleep


def lin():
    print('-=' * 20)


def cresc():
    lin()
    print('Contagem de 1 até 10 de 1 em 1')
    for c in range(1,11,1):
        print(c, end=' ')
    print()
    lin()

def desc():
    print('Contagem de 10 ate 0 de 2 em 2')
    for c in range(10,-1, -2):
        print(c, end=' ')

    print()
    lin()


def pessoa():

    for c in range(inicio, fim+1, passo):
        print(c, end=' ')
    print(f"Contagem de {inicio} até {fim} de {passo} em {passo}")


#PROGRAMA PRINCIPAL
sleep(1)
cresc()
sleep(1)
desc()
sleep(1)

print("AGORA É SUA VEZ DE PERSONALIZAR A CONTAGEM!!")

inicio = int(input("Início: "))
fim = int(input("Fim: "))
passo = int(input("Passo: "))

sleep(1)

pessoa()


