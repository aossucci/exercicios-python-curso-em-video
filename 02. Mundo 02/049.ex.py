'''Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só 
que agora utilizando um laço for.'''

titulo = 'BORA ESTUDAR A TABUADA!'
print(titulo.center(30))
print('=' * 30)
num = int(input('Digite um númnero inteiro: '))

for c in range(1, 11):
    tab = c * num
    print(f'{c:2} x {num:2} = {tab:2}')