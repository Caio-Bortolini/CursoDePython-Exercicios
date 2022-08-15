
def lin():
    print('-'*30)


lin()
print('CADASTRO')
lin()


def bloco(txt):
    print('-'*30)
    print(txt)
    print('-'*30)


bloco('Olá Mundo')
bloco('Capitão América')


def soma(a,b):
    s = a+b
    print(s)


soma(1,1)
soma(20,30)
soma(a=1, b=1)


def calculo(a,b):
    print(f" A = {a} e B = {b}")
    s = a + b
    print(f"Resultado de a + b = {s}")


calculo(90,1)
calculo(5,90)


def contador(*num):
    tam = len(num)
    print(f"Recebi os números {num} ao todo são {tam} números")
    print(f'A soma dos números é: {sum(num)}')



contador(2,2,4,5)






