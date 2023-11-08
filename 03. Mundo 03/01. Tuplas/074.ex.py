'''Exercício Python 074: Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. 
Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que 
estão na tupla.'''


import random


'''numeros = ((randint(1, 10), randint(1, 10), randint(
    1, 10), randint(1, 10), randint(1, 10)))'''

# numeros = tuple(randint(1, 10) for n in range(5))

numeros = tuple(random.sample(range(1, 10), 5))

print(numeros)

maior = max(numeros)
menor = min(numeros)

print(maior)
print(menor)
