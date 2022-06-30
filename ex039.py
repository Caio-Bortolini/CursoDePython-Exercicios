#alistamento militar

nascimento = int(input("Ano de nascimento: "))
anoAtual = 2022
alistamento = 18
idade = anoAtual - nascimento
anoAlistamento = alistamento - idade

previsao = anoAtual + anoAlistamento

if idade <=16 and idade <18:
    print("Quem nasceu em {} tem {} anos em {}".format(nascimento,idade,anoAtual))
    print("Ainda faltam {} anos para o seu alistamento".format(anoAlistamento))
    print("Seu alistamento será em {}".format(previsao))
elif idade == 18:
    print("Voce tem {} anos. Se aliste o quanto antes!!".format(idade))
elif idade >18:
    print("Quem nasceu em {} tem {} anos em {}".format(nascimento, idade, anoAtual))
    print("Voce deveria ter se alistado há {} anos atrás.".format(anoAlistamento))
    print("Seu alistamento foi em {}".format(previsao))
    print("Procure regularizar!")

