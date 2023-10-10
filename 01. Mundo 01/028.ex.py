'''Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.'''
import random

num_escolhido = int(input('Whats up! Tente adivinhar o número que estou pensando, entre 0 e 5: '))
num = random.randint(0,5) #gera um numero em um intervalo estiupulado


if num_escolhido == num:
    print('Parabéns, você acertou!')
else:
    print(f'Você errou! O número que pensei foi o {num}')