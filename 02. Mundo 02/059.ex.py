'''Crie um programa que leia dois valores e mostre um menu na tela:

[ 1 ] somar

[ 2 ] multiplicar

[ 3 ] maior

[ 4 ] novos números

[ 5 ] sair do programa

Seu programa deverá realizar a operação solicitada em cada caso.'''

num01 = int(input('Digite o primeiro número: '))
num02 = int(input('Digite o segundo número: '))
print()

while True:
    print('''
Selecione a opção desejada:
      
[ 1 ] Somar
[ 2 ] Multiplicar
[ 3 ] Maior
[ 4 ] Novos números
[ 5 ] Sair do programa
''')

    selecao = int(input('Digite a a opção escolhida: '))
    
    if selecao == 1:
        soma = num01 + num02
        print(f'A soma de {num01} e {num02} é {soma}')
    elif selecao == 2:
        multiplicar = num01 * num02
        print(f'A multiplicação de {num01} e {num02} é {multiplicar}')
    elif selecao == 3:
        if num01 > num02:
            print(f'O número {num01} é maior que o número {num02}')
        elif num02 > num01:
            print(f'O número {num02} é maior que o número {num01}')
        else:
            print('Os números são iguais')
    elif selecao == 4:
        num01 = int(input('Digite o primeiro número:'))
        num02 = int(input('Digite o segundo número:'))
    elif selecao == 5:
        break
    else: 
        print('Opção inválida!')
        
print('Programa encerrado')
            