'''print(f"O mairo numero da lista é o {max(numeros)}  e está na posição {max(numeros)[index]}")
'''

numeros = [int(input('Digite um número: ')) for num in range(0, 5)]

print(numeros)

maior_num = max(numeros)
menor_num = min(numeros)


print(
    f"O maior numero da lista é o {maior_num} e está na posição", end=' ')
for i, num in enumerate(numeros):
    if num == maior_num:
        print(f'{i}...', end=' ')

print()

print(f"O menor numero da lista é o {menor_num} e está na posição", end=' ')
for i, num in enumerate(numeros):
    if num == menor_num:
        print(f'{i}...', end=' ')
