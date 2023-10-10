'''Fazer um programa para sortear uma ordem de apresentação entre alguns alunos'''

import random

alunos = ['João', 'Maria', 'Pedro', 'Zé']
print(alunos)
random.shuffle(alunos)
ordenada = alunos
print(f'A ordem será {ordenada}')
