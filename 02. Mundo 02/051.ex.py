'''Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, 
mostre os 10 primeiros termos dessa progressão.'''

termo01 = int(input('Digite o primeiro termo da P.A.: '))
razao = int(input('Digite a razão da P.A.: '))
termos = int(input('Digite o número de termos: '))
ultimo_termo = termo01 + (termos - 1) * razao
soma = 0

for c in range(termo01, ultimo_termo + razao, razao):
    print(c)
    soma += c
print(f'A soma dos {termos} primeiros termos de uma P.A. de razão {razao} e a1 igual a {termo01} é {soma}')