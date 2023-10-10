'''A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:

– Até 9 anos: MIRIM

– Até 14 anos: INFANTIL

– Até 19 anos: JÚNIOR

– Até 25 anos: SÊNIOR

– Acima de 25 anos: MASTER'''

import datetime

nascimento = int(input('Digite o ano do seu nascimento: '))
ano_atual = datetime.date.today().year
idade = ano_atual - nascimento

if idade <= 9:
    print(f'Categoria MIRIM, idade até 9 anos, idadde atual {idade} anos')
elif idade <=14:
    print(f'Categoria INFANTIL, idade entre 10 e 14 anos, idadde atual {idade} anos')
elif idade <= 19:
    print(f'Categoria JÚNIOR, idade entre 15 e 19 anos, idadde atual {idade} anos')
elif idade <= 25:
    print(f'Categoria SÊNIOR, idade entre 20 e 25 anos, idadde atual {idade} anos')
else:
    print(f'Categoria MASTER, idade acima de 25 anos, idadde atual {idade} anos')
