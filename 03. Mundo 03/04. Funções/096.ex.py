'''Exercício Python 096: Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.'''


# Definição de uma função chamada 'area' que calcula a área de um terreno
# Parâmetros:
#   - larg: largura do terreno
#   - comp: comprimento do terreno
def area(larg, comp):
    # Cálculo da área multiplicando a largura pelo comprimento
    area = larg * comp

    # Impressão da mensagem com as dimensões e a área calculada, formatada com duas casas decimais
    print(
        f'A área do terreno com dimensões em metros de {larg} x {comp} é de {area:.2f} m²')


# Solicitação de entrada do comprimento e largura do usuário
c = float(input('Comprimento(m): '))
l = float(input('Largura(m): '))

# Chamada da função 'area' com os valores inseridos pelo usuário
area(l, c)
