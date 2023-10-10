'''Faça um programa que jogue par ou ímpar com o computador. 
O jogo só será interrompido quando o jogador perder, mostrando o 
total de vitórias consecutivas que ele conquistou no final do jogo.'''

import random
import time

cont = 0
while True:
    print('Vamos jogar par ou ímpar!')
    escolha = str(input('Você que par ou ímpar? ')).upper()
    pc = random.randint(0, 5)
    humano = int(input('Escolha um número de 0 a 5: '))
    time.sleep(0.5)
    print('PAR')
    time.sleep(0.5)
    print('ou')
    time.sleep(0.5)
    print('ÍMPAR')
    soma = pc + humano
    resultado = 'PAR' if soma % 2 == 0 else 'ÍMPAR'
    if escolha == resultado:
        print(f'Voce ganhou! Deu {resultado}!')
        cont += 1
    else:
        print(f'Você perdeu! Deu {resultado}')
        break
    
print(f'Você ganhou {cont} vezes até perder')
