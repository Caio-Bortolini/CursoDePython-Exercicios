import datetime

import datetime
dados = {}
atual = datetime.date.today().year

dados['Nome'] = str(input("Digite o nome da pessoa: "))
dados['Nascimento'] = int(input("Ano de nascimento: "))
dados['CTPS'] = int(input("Nº Carteira de Trabalho: (0 não tem)"))
dados['Idade'] = atual - dados['Nascimento']

if dados['CTPS'] != 0:
    dados['Contratação'] = int(input("Ano de contratação: "))
    dados['Salário'] = float(input("Salário: "))
    dados['Aposentadoria'] = dados['Contratação'] + 30



for k, v in dados.items():
    print(f"{k}: {v}")







