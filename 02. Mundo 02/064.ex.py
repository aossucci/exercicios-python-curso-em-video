'''Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o
usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram 
digitados e qual foi a soma entre eles (desconsiderando o flag).'''


num = 0
cont = 0
soma = 0

while num != 999:
    num = int(input('Digite um número, para parar digite 999: '))
    if num != 999:
        soma += num 
        cont += 1
    
print(f'Foram digitados {cont} números e a soma entre eles é de {soma}')