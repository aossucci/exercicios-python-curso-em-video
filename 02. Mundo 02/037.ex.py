'''Escreva um programa em Python que leia um número inteiro qualquer e 
peça para o usuário escolher qual será a base de conversão: 1 para binário, 
2 para octal e 3 para hexadecimal.'''


num = int(input('Digite um número: '))
escolha = int(input('''Escolha uma das bases para conversão:
[1] - Binário
[2] - Octal
[3] - Hexadecimal
Digite a opção: '''))

if escolha == 1:
    convertido = bin(num)[2:]
    print(f'O número {num} convertido para binário é {convertido}')

elif escolha == 2:
    convertido = oct(num)[2:]
    print(f'O número {num} convertido para octal é {convertido}')
elif escolha == 3:
    convertido = hex(num)[2:]
    print(f'O número {num} convertido para hexadecimal é {convertido}')
else:
    print('Opção inválida!')
