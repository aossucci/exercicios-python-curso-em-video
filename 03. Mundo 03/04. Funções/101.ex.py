'''Exercício Python 101: Crie um programa que tenha uma função chamada voto() que vai receber como 
parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa 
tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.
'''


def voto(ano):
    # Importa o módulo datetime para obter a data atual
    import datetime

    # Obtém o ano atual
    data_hoje = datetime.datetime.now().year

    # Calcula a idade subtraindo o ano de nascimento do ano atual
    idade = data_hoje - ano

    # Verifica as condições de voto com base na idade e retorna a mensagem correspondente
    if idade < 16:
        return f'Com {idade} anos: VOTO NEGADO'
    elif idade < 18 or idade > 65:
        return f'Com {idade} anos: VOTO OPCIONAL'
    else:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO'


# Solicita o ano de nascimento ao usuário
ano_nascimento = int(input('Ano de nascimento: '))

# Chama a função voto com o ano de nascimento fornecido pelo usuário
resultado_voto = voto(ano_nascimento)

# Imprime o resultado do voto
print(resultado_voto)
