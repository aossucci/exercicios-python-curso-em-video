'''Exercício Python 099: Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.'''


def maior(*num):
    # Calcula o maior número entre os argumentos
    num_maior = max(num)

    # Imprime o resultado
    print(f'O maior numero é o {num_maior}')


# Exemplo de chamada da função com os números 2, 13, 15, 1, 100
maior(2, 13, 15, 1, 100)
