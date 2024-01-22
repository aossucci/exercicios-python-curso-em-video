'''Exercício Python 098: Faça um programa que tenha uma função chamada contador(), 
que receba três parâmetros: início, fim e passo. Seu programa tem que realizar três contagens 
através da função criada:          
a) de 1 até 10, de 1 em 1                                                                                                                                              
b) de 10 até 0, de 2 em 2                                                                                                                                            
c) uma contagem personalizada'''

import time


def contador(i, f, p):
    print('\n' + '-' * 30)
    print(f'Contagem de {i} até {f} de {p} em {p}')
    print('Início')

    # Ajuste para permitir uma contagem decrescente se p for negativo
    if p > 0 and i <= f:
        for num in range(i, f+1, p):
            print(f'{num}', end=" ", flush=True)
            time.sleep(0.5)
    elif p < 0 and i >= f:
        for num in range(i, f-1, p):
            print(f'{num}', end=" ", flush=True)
            time.sleep(0.5)
    else:
        print("Entrada inválida para uma contagem decrescente.")

    # Movido a impressão para depois da contagem para que não haja '-' após os números
    print('\nFim')
    print('\n' + '-' * 30)


# Solicitar valores de início, fim e passo ao usuário
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))

# Validar se o passo é zero, positivo ou negativo
if passo == 0:
    print("Passo não pode ser zero.")
else:
    # Chamada da função com os valores fornecidos pelo usuário
    contador(inicio, fim, passo)
