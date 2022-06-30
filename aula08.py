import math
num = int(input("Digite um número: "))

raiz = math.sqrt(num)

print("A raiz de {} é {:.1f}".format(num, raiz))


#import match: importa a biblioteca inteira

#from match import xxxx, yyyy: importa somente o xxx, yyyy da biblioteca// não precisa usar o math: raiz = sqrt(num)

#print("A raiz de {} é {}".format(num, math.ceil(raiz))) (Arredonda para cima// pra baixo: floor.)