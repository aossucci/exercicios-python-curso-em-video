'''Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.'''

num = int(input('Digite um número: '))
tot_div = 0

for c in range(1, num + 1):
    if num % c == 0:
        tot_div += 1

if tot_div == 2:
    print(f'O número {num} é primo, pois é dividido por  apenas {tot_div} números')
else:
    print(f'O número {num} não é primo, pois é dividido por {tot_div} números')
