
alunos = {}

alunos['Nome'] = str(input("Digite o nome: "))
alunos['Media'] = float(input(f"Digite a média de {alunos['Nome']}: "))

if alunos['Media'] <5:
    alunos['Situacao'] = 'Reprovado'
elif alunos['Media'] == 5:
    alunos['Situacao'] = 'Recuperação'
else:
    alunos['Situacao'] = 'Aprovado'


#print(f"Nome: {alunos['Nome']}")
#print(f"Media: {alunos['Media']}")
#print(f"Situação {alunos['Situacao']}")

for k, v in alunos.items():
    print(f"{k}: {v}")




