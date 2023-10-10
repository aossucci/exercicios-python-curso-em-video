'''Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: 
a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.'''

lista_idades = []

mulheres_menos_20 = 0
nome_homem_mais_velho = ''
idade_homem_mais_velho = 0

for p in range(1, 5):
    print(f'---- {p}ª PESSOA ----')
    nome = str(input(f'Nome: ')).strip().title()
    idade = int(input(f'Idade: '))
    sexo = str(input(f'Sexo [M/F]: ')).upper().strip()   
    lista_idades.append(idade) 
    if sexo == 'M' and idade > idade_homem_mais_velho:
        idade_homem_mais_velho = idade
        nome_homem_mais_velho = nome           
    if sexo == 'F' and idade < 20:
        mulheres_menos_20 += 1
print()
media_idades = sum(lista_idades) / len(lista_idades)

print(f'A média de idade do grupo é {media_idades} anos')
print()
print(f'O homem mais velho é o {nome_homem_mais_velho} com {idade_homem_mais_velho} anos')
print()
print(f'São {mulheres_menos_20} mulheres com menos de 20 anos')