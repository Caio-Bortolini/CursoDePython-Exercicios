
alunos = {}

alunos['nome'] =  str(input("Digite o nome do aluno: "))
alunos['media'] = float(input("Digite a média: "))
alunos['Situação'] = ''

if alunos['media']>= 7:
    alunos['Situação'] = 'Aprovado'
else:
    alunos['Situação'] = 'Reprovado'

for k, v in alunos.items():
    print(f' {k} é igual a {v}')

