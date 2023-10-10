'''Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.'''

lista_pesos = []
for n in range(1, 6):
    peso = float(input(f'Digite o peso em KG da {n}ª pessoa: '))
    lista_pesos.append(peso)

maior_peso = max(lista_pesos)
menor_peso = min(lista_pesos)
indice_maior_peso = lista_pesos.index(maior_peso)
indice_menor_peso = lista_pesos.index(menor_peso)

print(f'A pessoa mais pesada é a {indice_maior_peso + 1}ª e tem {maior_peso}kg')
print(f'A pessoa mais leve é a {indice_menor_peso + 1}ª e tem {menor_peso}kg')
