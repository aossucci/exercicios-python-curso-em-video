'''Exercício Python 100: Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior'''

import random

# Lista para armazenar números sorteados
numeros = []

# Função que sorteia um número entre 1 e 100


def sorteia():
    num = random.randint(1, 100)
    return num


def somaPar(lista):
    soma_pares = 0
    for num in lista:
        if num % 2 == 0:
            soma_pares += num
    return soma_pares


# Loop para sortear 5 números e adicioná-los à lista
for n in range(0, 5):
    num_sorteado = sorteia()
    numeros.append(num_sorteado)

# Mostra a lista de números sorteados
print("Números sorteados:", numeros)

# Mostra a soma dos números pares
print("Soma dos números pares:", somaPar(numeros))
