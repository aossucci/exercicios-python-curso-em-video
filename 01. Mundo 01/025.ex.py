'''Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.'''

'''nome = str(input('Digite seu nome completo: ')).strip()

print(f'Tem Silva no nome?', {'SILVA' in nome.upper()})'''

nome = str(input('Digiete seu nome completo: ')).strip().upper()

tem_silva = 'SILVA' in nome.split()

print(f'Tem Silva no nome? {tem_silva}')