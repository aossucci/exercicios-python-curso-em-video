'''Exercício Python 087: Aprimore o desafio anterior, mostrando no final: 
A) A soma de todos os valores pares digitados.          
B) A soma dos valores da terceira coluna.             
C) O maior valor da segunda linha.
'''

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

# Solicita ao usuário que insira valores para preencher a matriz
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f"Digite um valor para [{l}, {c}]: "))

# Exibe a matriz formatada na tela
print('-='*30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()

# Calcula a soma dos números pares na matriz
somaPares = 0
for l in range(3):
    for c in range(3):
        if matriz[l][c] % 2 == 0:
            num = matriz[l][c]
            somaPares += num

# Calcula a soma dos números na terceira coluna
soma_c3 = 0
for l in range(3):
    num = matriz[l][2]  # A terceira coluna tem índice 2
    soma_c3 += num

# Encontra o maior valor na segunda linha da matriz
maior_valor_segunda_linha = max(matriz[1])

# Exibe os resultados
print(f'A soma dos números pares da matriz é {somaPares}')
print(f'A soma dos números da 3ª coluna é {soma_c3}')
print(f'O maior valor da segunda linha é {maior_valor_segunda_linha}')
