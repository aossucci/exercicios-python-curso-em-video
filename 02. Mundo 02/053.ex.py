'''Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, 
desconsiderando os espaços. Exemplos de palíndromos:
APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.'''

frase = str(input('Digite uma frase qualquer: ')).strip().upper()
frase_junta = frase.replace(' ', '')
inverso = frase_junta[::-1]

print(frase_junta)
print(inverso)              

if frase_junta == inverso:
    print('É um palíndromo!')
else:
    print('Não é um palíndromo!')