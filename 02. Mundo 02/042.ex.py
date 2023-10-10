'''Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de 
triângulo será formado:
(dizer se 3 segmentos de reta podem formar um triângulo)

– EQUILÁTERO: todos os lados iguais

– ISÓSCELES: dois lados iguais, um diferente

– ESCALENO: todos os lados diferentes'''


try: #usado para corrigir erro
    med1 = int(input('Digite a primeira medida: '))
    med2 = int(input('Digite a segunda medida: '))
    med3 = int(input('Digite a terceira medida: '))

    if med1 +  med2 > med3 and med1 + med3 > med2 and med2 + med3 > med1:
        print(f'As medidas, {med1}, {med2}, {med3}, podem formar um triângulo. ', end='')# [, end=''] para continuar a linha de baixo na mesma frase
        if med1 == med2 == med3:
            print('O triângulo é equilátero')
        elif med1 == med2 != med3 or med1 == med3 != med2 or med2 == med3 !=med1:
            print('O triângulo é isósceles')
        elif med1 != med2 != med3 !=med1:
            print('O trângulo é escaleno')
    else:
        print(f'As medidas, {med1}, {med2}, {med3}, não podem formar um triângulo')
except ValueError:
    print('Erro! Verifique os números digitados!')