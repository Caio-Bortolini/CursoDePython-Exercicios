#Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’. Caso esteja errado, peça a digitação novamente até ter um valor correto.

sexo = str(input("qual é o seu sexo? [ F/M ]: ")).strip().upper()

while sexo not in 'MmFf':
    sexo = str(input("Digite uma infromação válida: "))
print("Sexo {}, cadastrado com sucesso!!".format(sexo))

