numeros = ('um', 'dois', 'tres', 'quatro', 'cinco',
           'seis', 'sete', 'oito', 'nove', 'dez',
           'onze', 'doze', 'treze', 'quatorze',
           'quinze', 'dezesseis', 'dezessete',
           'dezoito', 'dezenove', 'vinte')

while True:
    digitado = int(input("Digite um número entre 0 e 20: "))

    if 0 <= digitado <=20:
        break
    print(f" Tente novamnte", end='')

print(f"O número digitado foi o {numeros[digitado-1]}")
