'''Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. 
Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos 
palpites foram necessários para vencer.'''

import random

num = random.randint(0, 10)
num_escolhido = int(input('Digite um número de 0 a 10: '))
cont = 0

while num_escolhido != num:
    if num_escolhido < num:
        num_escolhido = int(input('Errou! É maior! Tente de novo: '))
        cont += 1
    if num_escolhido > num:
        num_escolhido = int(input('Errou! É menor! Tente de novo: '))
        cont += 1

print(f'Você acertou! Foram {cont + 1} tentativas!')
