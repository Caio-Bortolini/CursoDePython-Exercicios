from datetime import date
ano = int(input("Que ano voce quer analisar? Coloque 0 para saber o ano atual: "))
if ano == 0:
    ano = date.today().year
if ano % 4 ==0 and ano %100 !=0 or ano %100 ==0:
    print("O ano de {} é BISSEXTO".format(ano))
else:
    print("O ano de {} NÃO É BISSEXTO".format(ano))
