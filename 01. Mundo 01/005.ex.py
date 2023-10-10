'''Faça um programa que leia um número inteiro e mostre na tela o seu sucesor e seu antecessor'''

num = int(input('Digite um número: '))
antecessor = num - 1
sucessor = num + 1

print(f'O número digitado foi o {num}, seu antecessor é o {num-1}, seu sucessor é o {num+1}') #alternativa sem variáveis

print('O número digitado foi o {}, seu antecessor é o {}, seu sucessor é o {}'.format(num, antecessor, sucessor))
