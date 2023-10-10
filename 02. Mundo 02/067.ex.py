'''Faça um programa que mostre a tabuada de vários números, um de cada vez, 
para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.'''

while True:
    num = int(input('Você quer ver a tabuada de qual número? '))
    if num < 0:
        break
    print(f'Tabuada do {num}')
    for c in range(1, 11):
        tab = c * num
        print(f'{c:2} x {num:2} = {tab:2}')
print('FIM')