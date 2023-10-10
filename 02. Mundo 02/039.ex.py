'''Faça um programa que leia o ano de nascimento de um jovem e informe, 
de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, 
se é a hora exata de se alistar ou se já passou do tempo do alistamento. 
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.'''

import datetime
'''ano = datetime.date.today().year'''

ano_nascimento = int(input('Digite seu ano de nascimento: '))
sexo = str(input('Digite seu sexo [M] ou [F]: ')).upper()

if sexo != 'M' and sexo != 'F':
    raise ValueError('Sexo deve ser M ou F')

data_atual = datetime.datetime.now()
ano_atual = data_atual.year
idade = ano_atual - ano_nascimento



if idade < 18 and sexo == 'M':
        tempo = 18 - idade
        print(f'Você tem {idade} em {ano_atual} e precisará se alistar em {tempo} anos, seu alistamento será em {ano_nascimento + 18}')
elif idade > 18 and sexo == 'M':
        tempo = idade - 18
        print(f'Você tem {idade} anos em {ano_atual}, seu alistamento passou do prazo em {tempo} anos, foi no ano de {ano_nascimento + 18}')
elif idade == 18 and sexo == 'M':
        print(f'Você tem 18 anos em {ano_atual}, deve se alistar esse ano!')
else:
        print('Você é mulher, não precisa se alistar')

