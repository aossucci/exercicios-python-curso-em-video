'''Exercício Python 082: Crie um programa que vai ler vários números e colocar em uma lista. 
Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, 
respectivamente. Ao final, mostre o conteúdo das três listas geradas.'''

numeros = []
pares = []
impares = []

while True:
    num = int(input('Digite um número: '))
    numeros.append(num)
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)
    continuar = input('Voce quer continuar? [S|N]: ')
    if continuar in "Nn":
        break

print(f'Lista completa: {numeros}')
print(f'Lista com os valores pares: {pares}')
print(f'Lista com os valores ímpares: {impares}')
