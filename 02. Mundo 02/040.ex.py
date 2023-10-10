'''Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:'''

nota_1bim = float(input('Digite a nota do 1º bimestre: '))
nota_2bim = float(input('digite a nota do 2º bimestre: '))
media_final = round((nota_1bim + nota_2bim) / 2, 2)

if media_final >= 7.0:
    print(f'Sua média final foi {media_final}. Parabéns você está aprovado!')
elif media_final < 5.0:
    print(f'Sua média final foi {media_final}. Você está reprovado!')
elif media_final >= 5 and media_final < 7:
    print(f'Sua média final está em {media_final}. Você está em recuperação!')

