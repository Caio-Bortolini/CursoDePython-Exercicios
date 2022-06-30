#detector de paléndromo

frase = str(input("Digite uma frase: ")).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''

for i in range(len(junto) -1, -1, -1):
    inverso = inverso + junto[i]
if inverso == junto:
    print("Temos um palindromo")
else:
    print("Não é um palíndromo")
