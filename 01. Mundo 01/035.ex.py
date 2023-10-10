try: #usado para corrigir erro
    med1 = int(input('Digite a primeira medida: '))
    med2 = int(input('Digite a segunda medida: '))
    med3 = int(input('Digite a terceira medida: '))

    if med1 +  med2 > med3 and med1 + med3 > med2 and med2 + med3 > med1:
        print(f'As medidas, {med1}, {med2}, {med3}, podem formar um triângulo')
    else:
        print(f'As medidas, {med1}, {med2}, {med3}, não podem formar um triângulo')

except ValueError:
    print('Erro! Verifique os números digitados!')
