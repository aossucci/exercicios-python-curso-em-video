'''Crie um programa que leia o nome completo de umapessoa e mostre:
-> O nome com todas as letras maiúsculas e minusculas
-> Quantas letras ao todo (sem espaços)
-> Quantas letras tem o primeiro nome'''

nome = str(input('Digite seu nome completo: ')).strip()

print(f'Nome em maiusculas: {nome.upper()}')
print(f'Nome em minusculas: {nome.lower()}')
nomeJunto = nome.replace(' ', '')
print(f'Seu nome tem {len(nomeJunto)} letras')
nomeSeparado = nome.split()
print(f'Seu primeiro nome tem {len(nomeSeparado[0])} letras')

