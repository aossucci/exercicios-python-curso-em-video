'''Exercício Python 63: Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N 
primeiros elementos de uma Sequência de Fibonacci. Exemplo:

0  1  1  2  3  5  8'''

n = int(input('Quantos termos da sequência você quer mostrar? '))

cont = 0
fib = []

while cont < n:
    if cont <=1:
        fib.append(cont)
    else:
        fib.append(fib[-1] + fib[-2])
        
    cont += 1
    
for num in fib:
    print(num, end = '-')
