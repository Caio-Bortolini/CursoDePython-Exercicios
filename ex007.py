#Media de notas


nota1 = int(input('Digite a primeira nota:'))
nota2 = int(input('Digite a segunda nota: '))
nota3 = int(input('Digite a terceira nota: '))
nota4 = int(input('Digite a quarta nota: '))

media = (nota1 + nota2 + nota3 + nota4) / 4
print('A sua média de notas é:{}'.format(media))



if media >= 5 and media <=10:
    print('Voce esta aprovado')
elif media<=4:
  print('Voce foi reprovado')

else:
     print('NOTA NÃO CONSIDERADA. DIGITE APENAS NUMEROS ENTRE 0 E 10!!!')







