'''Exercício Python 080: 
Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, 
já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.'''

# Inicializa uma lista vazia para armazenar os números
numeros = []

# Loop para solicitar a entrada de 5 números
for c in range(0, 5):
    # Solicita que o usuário digite um número e converte para inteiro
    num = int(input('Digite um número: '))

    # Verifica se a lista está vazia ou se o número é maior que o último elemento
    if c == 0 or num > numeros[-1]:
        # Adiciona o número ao final da lista
        numeros.append(num)
    else:
        # Inicializa a posição como 0
        pos = 0
        # Loop para encontrar a posição correta para inserir o número na lista ordenada
        while pos < len(numeros):
            # Compara o número com cada elemento na lista
            if num <= numeros[pos]:
                # Insere o número na posição correta e sai do loop
                numeros.insert(pos, num)
                break
            # Incrementa a posição para verificar o próximo elemento na próxima iteração
            pos += 1

# Imprime a lista final ordenada
print(numeros)
