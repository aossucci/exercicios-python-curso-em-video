'''Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não 
atingiram a maioridade e quantas já são maiores.'''

import datetime

cont_menor = 0
cont_maior = 0
for n in range(1, 8):
    ano = int(input(f'Digite o ano de nacimento da {n}ª pessoa: '))
    ano_atual = datetime.datetime.now().year
    idade = ano_atual - ano
    if idade < 18:
        cont_menor += 1
    else:       
        cont_maior += 1
        
print(f'São {cont_menor} pessoas menores de idade')
print(f'São {cont_maior} pessoas maiores de idade')
