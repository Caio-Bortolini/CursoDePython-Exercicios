#classificação de idades
from datetime import date
nacimento = int(input("Data de nascimento: "))
anoAtual = date.today().year
idade = anoAtual - nacimento

if idade <= 9:
    print("Quem nasceu em {} tem {} anos e sua categoria é: MIRIM".format(nacimento,idade))
elif idade >9 and idade <=14:
    print("Quem nasceu em {} tem {} anos e sua cateagoria é: INFANTIL".format(nacimento, idade))
elif idade >14 and idade<=19:
    print("Quem nasceu em {} tem {} anos e sua categoria é: JUNIOR".format(nacimento,idade))
elif idade >19 and idade <=25:
    print("Quem nasceu em {} tem {} anos e sua categoria é: SENIOR".format(nacimento,idade))
elif idade >25:
    print("Quem nasceu em {} tem {} anos e sua categoria é: MASTER".format(nacimento,idade))

