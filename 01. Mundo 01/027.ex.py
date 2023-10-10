'''Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente'''

nome_completo = str(input('Digiete seu nome completo: ')).strip().title()

nome_separado = nome_completo.split()

print(f'Primeiro nome: {nome_separado[0]}\nSegundo nome: {nome_separado[-1]}')