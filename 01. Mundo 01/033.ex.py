'''Faça um programa que leia três números e mostre qual é o maior e qual é o menor.'''

num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo número: '))
num3 = float(input('Digite o terceiro número: '))

lista = [num1, num2, num3]

maior = max(lista)
menor = min(lista)

print(f'O maior valor da lista é o {maior}')
print(f'O menor valor da lista é o {menor}')
