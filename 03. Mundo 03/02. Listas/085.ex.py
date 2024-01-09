'''Exercício Python 085: Crie um programa onde o usuário possa digitar sete 
valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. 
No final, mostre os valores pares e ímpares em ordem crescente.'''

numeros = []
for num in range(1, 8):
    num = int(input(f'Digite o {num}º número: '))
    numeros.append(num)

print(f'Os números digitados foram {numeros}')

pares = []
ímpares = []
for num in numeros:
    if num % 2 == 0:
        pares.append(num)
    else:
        ímpares.append(num)

print(f'Os números pares são {pares}')
print(f'Os números ímpares são {ímpares}')

# resolução do Guanabara
print('-=' * 30)

núm = [[], []]
valor = 0
for c in range(1, 8):
    valor = int(input(f'Digite o {c}º valor: '))
    if valor % 2 == 0:
        núm[0].append(valor)
    else:
        núm[1].append(valor)

print('-=' * 30)
print(f'Os valores pares digitados foram: {sorted(núm[0])}')
print(f'Os valores ímpares digitados fora: {sorted(núm[1])}')
