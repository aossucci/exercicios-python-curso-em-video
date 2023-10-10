'''Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”, em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.'''

frase = str(input('Escreva uma frase qualquer: ')).strip().upper()

print(f'Quantas vezes aparece a letra A? {frase.count("A")} vezes, '
      f'a primeira vez na posição {frase.find("A")+1} '
        f'e por último na posição {frase.rfind("A")+1}')
