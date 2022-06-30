#media escolar

nota1 = float(input("Primeira nota: "))
nota2 = float(input("Segunda nota: "))
nota3 = float(input("Terceira nota: "))
nota4 = float(input("Quarta nota: "))

media = (nota1 + nota2 + nota3 + nota4) / 4

if media <5:
    print("Aluno REPROVADO!! a media foi de {}".format(media))
elif media > 5 and media<=6.9:
    print("Aluno esta de recuperação. a media foi de {}".format(media))
elif media > 7:
    print("APROVADOO!!! a media foi de {}".format(media))