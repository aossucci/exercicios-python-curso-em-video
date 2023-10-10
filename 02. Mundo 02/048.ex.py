'''Faça um programa que calcule a soma entre todos os números ímpares que são
múltiplos de três e que se encontram no intervalo de 1 até 500.'''

soma = 0
cont = 0
'''for n in range(1, 501):
    if n % 3 == 0 and n % 2 == 1:
        soma += n
'''
for n in range(3, 501, 3):
    if n % 2 == 1:
        soma += n
        cont += 1
print(f'Foram encontrados {cont} números com soma total de {soma}')