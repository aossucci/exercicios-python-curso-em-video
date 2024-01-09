'''Exercício Python 081: Crie um programa que vai ler vários números e colocar em uma lista. 
Depois disso, mostre:               
A) Quantos números foram digitados.  
B) A lista de valores, ordenada de forma decrescente.                                                                                          
C) Se o valor 5 foi digitado e está ou não na lista.'''

numeros = []

while True:
    '''num = int(input('Digite um número: '))
    numeros.append(num)'''
    numeros.append(int(input('Digite um número: ')))
    continuar = input('Voce quer continuar? [S|N]: ')
    if continuar in "Nn":
        break

print(numeros)
# Quantos numeros foram digitado
print(f"Foram digitados {len(numeros)} números")
# números em ordem decrescente
numeros.sort(reverse=True)
print(f'Os números em ordem decrescente são {numeros}')
# verificar se o número 5 está na lista
if 5 in numeros:
    print('O números 5 está na lista')
else:
    print('O números 5 não está na lista')
