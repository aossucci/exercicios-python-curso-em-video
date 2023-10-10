'''Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros
termos da progressão usando a estrutura while.'''

print('Gerador de P.A.')
print('-=' * 10)
termo01 = int(input('Digite o primeiro termo da P.A.: '))
razao = int(input('Digite a razão da P.A.: '))

termos = 1
p_aritimetica = termo01

while termos <= 10:
    print(p_aritimetica, end=' ')
    p_aritimetica += razao
    termos += 1
    
print('FIM')