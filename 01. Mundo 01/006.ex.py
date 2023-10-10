'''Crie um algoritimo que leia um número e mostre o seu dobro, triplo e raiz quadrada'''

num = int(input('Digite um número: '))

print(f'O dobro de {num} é {num*2}')
print(f'O triplo de {num} é {num*3}')
print(f'A raiz quadra de {num} é {pow(num, 1/2):.0f}') 
# (:.f) serve para formatar casas decimais depois da virgula