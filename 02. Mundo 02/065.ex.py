'''Crie um programa que leia vários números inteiros pelo teclado. No final da execução, 
mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. 
O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.'''



numeros = []
while True:
    num = int(input('Digite um número: '))
    numeros.append(num)  # Adicionar o número à lista 
    continuar = int(input('Você gostaria de continuar? Digite 1 para continuar e 0 para sair: '))
    if continuar == 0:
        break

maior = max(numeros)
menor = min(numeros)
media = sum(numeros) / len(numeros)

print(f'''
Fora digitados {len(numeros)} números
Média = {media:.2f}
Menor = {menor}
Maior = {maior}''')