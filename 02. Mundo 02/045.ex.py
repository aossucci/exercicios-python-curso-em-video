'''Crie um programa que faça o computador jogar Jokenpô com você'''

import random
from time import sleep

print(f"{' Jogo Jokempô ':=^40}")
print()

opcoes = ['Pedra', 'Papel', 'Tesoura']
computador = random.choice(opcoes)

pessoa = int(input('''Vamos jogar Jokempo! Escolha a opção que deseja:
[0] Pedra
[1] Papel
[2] Tesoura
Digite a opção: '''))
sleep(1)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')

if computador == 'Pedra':
    if pessoa == 0:
        print(f'''Computador ({computador}) x ({opcoes[pessoa]}) Você. Putz! Empatamos!''')
    elif pessoa == 1:
        print(f'''Computador ({computador}) x ({opcoes[pessoa]}) Você. Putz! Você venceu!''')
    elif pessoa == 2:
        print(f'''Computador ({computador}) x ({opcoes[pessoa]}) Você. HAHA! Ganhei!''')
    else:
        print('Número escolhido inválido, presta atenção pô!')
elif computador == 'Papel':
    if pessoa == 0:
        print(f'''Computador ({computador}) x ({opcoes[pessoa]}) Você. HAHA! Ganhei!''')
    elif pessoa == 1:
        print(f'''Computador ({computador}) x ({opcoes[pessoa]}) Você. Putz! Empatamos!''')
    elif pessoa == 2:
        print(f'''Computador ({computador}) x ({opcoes[pessoa]}) Você. Putz! Você venceu!''')
    else:
        print('Número escolhido inválido, presta atenção pô!')
elif computador == 'Tesoura':
    if pessoa == 0:
        print(f'''Computador ({computador}) x ({opcoes[pessoa]}) Você. Putz! Você venceu!''')
    elif pessoa == 1:
        print(f'''Computador ({computador}) x ({opcoes[pessoa]}) Você. HAHA! Ganhei!''')
    elif pessoa == 2:
        print(f'''Computador ({computador}) x ({opcoes[pessoa]}) Você. Putz! Empatamos!''')
    else:
        print('Número escolhido inválido, presta atenção pô!')