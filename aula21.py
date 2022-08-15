
#help(print())

#def contador(i, f, p):

#docstring
    #'''

    #:param i: inicio
    #:param f: fim
    #:param p: passo
    #:return: nao tem
    #Função criada por Caio Bortolini
    #'''#

#help(contador())
###############################################################

def somar(a=0, b=0, c=0):

    s = a + b + c
    print(f"A soma vale {s}")

somar(20,3)

###############################################################

def funcao():
    #global n1
    n1 = 200
    print(f"N1 dentro vale {n1}")
    #escopo local

n1  = 5
print(f"N1 fora vale {n1}")
#escopo global

funcao()

#################################################################

def somador(a=0, b=0, c=0):
    s = a+b+c
    return s


r1 = somador(3,5)
r2 = somador(6,8,9)
r3 = somador(1,1,1)

print(f"Os resultados foram {r1}, {r2} e {r3}")


