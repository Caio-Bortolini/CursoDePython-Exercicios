# O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
from ast import Str
import random
from random import choice

nome1 = str(input("Digite o seu nome: "))
nome2 = str(input("Digite o seu nome: "))
nome3 = str(input("Digite o seu nome: "))
nome4 = str(input("Digite o seu nome: "))
lista = [nome1, nome2, nome3, nome4]
random.shuffle(lista)

print("A orde da apresentação será:\n {}".format(lista))



for i in range(1,5):
    nome = str(input("Digite seu {}º nome: ".format(i)))

print("Fim")

