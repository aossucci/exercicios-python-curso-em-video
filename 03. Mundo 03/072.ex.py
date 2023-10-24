'''Exercício Python 72: Crie um programa que tenha uma dupla 
totalmente preenchida com uma contagem por extenso, de zero até vinte. 
Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.'''

numeros = ('um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze',
           'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')


while True:
    num = int(input('Digite um número entre 1 a 20: '))
    if 1 <= num <= 20:
        break
    print('O número digitado não está entre 1 e 20.', end=' ')

print(f'O número digitado foi o {numeros[num - 1]}')
