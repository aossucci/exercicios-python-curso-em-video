'''Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a média'''

aluno = str(input('Nome do aluno: '))
nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
media = (nota1 + nota2) / 2

print(f'A média do aluno {aluno} é {media}')
