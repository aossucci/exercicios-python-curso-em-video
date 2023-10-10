'''Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada,
o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:

A) quantas pessoas tem 18 anos ou mais.

B) quantos homens foram cadastrados.

C) quantas mulheres tem menos de 20 anos.'''

cont18 = 0
homens = 0
mulheresMenos20 = 0
while True:
    idade = int(input('Digite a idade: '))
    sexo = str(input('Digite o sexo [M/F]: ')).strip().upper()[0]
    while sexo not in 'MF':
        sexo = str(input('Digite o sexo [M/F]: ')).strip().upper()[0]
    pergunta = str(input('Você quer continuar [S/N]? ')).strip().upper()[0]
    if idade >= 18:
        cont18 += 1
    if sexo == 'M':
        homens += 1  
    if sexo == 'F' and idade < 20:
        mulheresMenos20 += 1
    if pergunta == 'N':
        break
print('-'*30)
print(f'{cont18} pessoas tem mais de 18 anos')
print(f'{homens} homens foram cadastrados')
print(f'{mulheresMenos20} tem menos de 20 anos')