'''Exercício Python 102: Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a calcular e outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.
'''


def fatorial(num, show=False):
    """
    Calcula o fatorial de um número.

    Parâmetros:
    - num (int): O número para o qual calcular o fatorial.
    - show (bool): Se True, exibe a expressão de multiplicação.

    Retorna:
    - int: O resultado do fatorial.
    """

    # Inicializa a variável 'fat' como 1, que será multiplicada pelos números no loop.
    fat = 1

    # Loop reverso começando de 'num' até 1 (inclusive).
    for n in range(num, 0, -1):
        # Multiplica 'fat' pelo número atual do loop.
        fat *= n

        # Verifica se a opção 'show' é True para imprimir a expressão de multiplicação.
        if show:
            # Se o número atual do loop for maior que 1, imprime 'n x '.
            if n > 1:
                print(f'{n} x ', end='')
            # Se o número atual do loop for 1, imprime '1 ' (sem o 'x' no final).
            else:
                print(f'{n} ', end='')

    # Retorna o resultado do fatorial.
    return fat


# Solicita ao usuário que insira um número.
numero = int(input('Digite um número: '))

# Pergunta ao usuário se deseja mostrar a expressão de multiplicação.
mostrar_expressao = input(
    'Deseja mostrar a expressão de multiplicação? (S/N): ').lower()

# Avalia a resposta do usuário.
if mostrar_expressao == 's':
    resultado = fatorial(numero, show=True)
else:
    resultado = fatorial(numero)

# Exibe o resultado do fatorial.
print(f'\nO fatorial de {numero} é {resultado}')
