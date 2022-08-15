from lib.interface import *
from time import sleep
from lib.arquivo import  *

arq = 'cursoemvideo.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['Pèssoas cadastradas', 'Ver pessoa', 'Sair do sistema'])

    if resposta == 1:
        lerArquivo(arq)    # Ler pessoas cadastradas
    elif resposta == 2:
        cabecalho("NOVO CADASTRO")
        nome = str(input("Nome: "))
        idade = leiaInt("Idade: ")
        cadastrar(arq, nome, idade)



    elif resposta == 3:
        cabecalho("Saindo do sistema")
        break

    else:
        cabecalho("ERRO. digite uma opção válida")
        sleep(2)






