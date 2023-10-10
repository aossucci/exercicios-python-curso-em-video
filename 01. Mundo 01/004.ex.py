'''Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as 
informações possíveis sobre ele'''

a = input('Digite algo: ')

print(f'Qual o tipo primitivo? {type(a)}')
print(f'Só tem espaços? {a.isspace()}')
print(f'É numérico? {a.isnumeric()}')
print(f'É alfabético? {a.isalpha()}')
print(f'É em letras minúsculas? {a.islower()}')
#....