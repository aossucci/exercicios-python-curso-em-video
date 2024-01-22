'''Exercício Python 097: Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.     
'''


def escreva(txt):
    # Calcula o tamanho necessário para a linha de separação
    tam = len(txt) + 4

    # Imprime uma linha de "=" para separar o texto
    print('=' * tam)

    # Imprime o texto centralizado com espaços adicionais no início e no final
    print(f'  {txt}')

    # Imprime outra linha de "=" para separar o texto
    print('=' * tam)


# Solicitação de entrada de texto ao usuário
mensagem = str(input('Insira sua mensagem: ')).title()

# Chama a função 'escreva' passando a mensagem como argumento
escreva(mensagem)
