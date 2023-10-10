'''Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. 
O programa encerrará quando ele disser que quer mostrar 0 termos.'''


print('Gerador de P.A.')
print('-=' * 10)
termo01 = int(input('Digite o primeiro termo da P.A.: '))
razao = int(input('Digite a razão da P.A.: '))

termos = 1
p_aritimetica = termo01
total = 0
mais = 10

while mais != 0:
    total = total + mais
    while termos <= total:
        print(p_aritimetica, end=' ')
        p_aritimetica += razao
        termos += 1
    print('PAUSA')
    mais = int(input('Quantos termos voce quer mostrar a mais? '))
print(f'A progressão foi finalizada com {total} mostrados')