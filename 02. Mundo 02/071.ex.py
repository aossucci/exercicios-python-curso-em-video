'''Crie um programa que simule o funcionamento de um caixa eletrônico. No início, 
pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai 
informar quantas cédulas de cada valor serão entregues. OBS:

considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.'''

valor_saque = int(input('Valor saque: R$'))
total = valor_saque
'''
notas_50 = notas_20 = notas_10 = notas_01 = 0

while True:
    if total >= 50:
        notas_50 = int(total/ 50)
        total = total - notas_50 * 50
    elif total >= 20:
        notas_20 = int(total / 20)
        total = total - notas_20 * 20
    elif total >= 10:
        notas_10 = int(total / 10)
        total = total - notas_10 * 10
    elif total >= 1:
        notas_01 = int(total / 1)
        total = total - notas_01 * 1
    if total == 0:
        break
'''
nota = 50
total_nota = 0
while True:
    if total >= nota:
        total -= nota
        total_nota += 1
    else:
        if total_nota > 0:
            print(f'Total de {total_nota} notas de R${nota} ')
        if nota == 50:
            nota = 20
        elif nota == 20:
            nota = 10
        elif nota == 10:
            nota = 1
        total_nota = 0
        if total == 0:
            break