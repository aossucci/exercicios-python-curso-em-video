'''Exercício Python 075: Desenvolva um programa que leia quatro valores pelo teclado e 
guarde-os em uma tupla. No final, mostre:

A) Quantas vezes apareceu o valor 9.

B) Em que posição foi digitado o primeiro valor 3.

C) Quais foram os números pares.'''

''''numeros = []
for numero in range(0, 4):

    numero = int(input("Digite um numero: "))
    numeros.append(numero)

print(numeros)'''

# tranformei uma lista em uma tupla com o 'tuple'
numeros = tuple([int(input('Digite um numero: ')) for numero in range(0, 4)])

print(numeros)

indices = []
pares = []
for index, n in enumerate(numeros):
    if n == 3:
        indices.append(index)
    if n % 2 == 0:
        pares.append(n)


print(f'O número 9 aparece {numeros.count(9)} vezes na tupla')
print(f'O número 3 está na posição {indices}')
print(f'Os numeros pares são {pares}')
