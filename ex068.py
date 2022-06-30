
from random import randint
vitoria = 0
while True:
    jogador = int(input("Digite um valor: "))
    computador = randint(0,11)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input("Par ou Impar? [P/I]: ")).upper()
    print(f"Voce jogou {jogador} e o computador {computador}. Total de {total}")

    if tipo == 'P':
        if total %2 ==0:
            print("Voce venceu")
            vitoria+=1
        else:
            print("Voce perdeu")
            break

    elif tipo == 'I':
        if total %2 ==1:
            print("Voce venceu")
            vitoria+=1
        else:
            print("Voce perdeu")
            break


print(f"Voce venceu {vitoria} vezes")






