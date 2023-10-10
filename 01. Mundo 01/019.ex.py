'''Um professor quer sortear um dos seus anulos para uma tarefa, faça um programa que leia os nomes dos alunos e sorteie um deles'''
import random

aluno01 = 'Paulo'
aluno02 = 'Marta'
aluno03 = 'Marcio'
aluno04 = 'Pedro'
alunos = [aluno01, aluno02, aluno03, aluno04] #lista []
escolhido = random.choice(alunos)

print(f'O aluno escolhido foi {escolhido}')