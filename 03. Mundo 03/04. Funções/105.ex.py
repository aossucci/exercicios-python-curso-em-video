'''Exercício Python 105: Faça um programa que tenha uma função notas() que pode receber várias notas de 
alunos e vai retornar um dicionário com as seguintes informações:

– Quantidade de notas                   
– A maior nota                             
– A menor nota                                                                                                                                                              – A média da turma                                                                                                                                           
– A situação (opcional)'''


def notas(*nota, sit=False):
    dic_notas = {}  # Inicializa o dicionário
    dic_notas['Total'] = len(nota)
    dic_notas['Maior'] = max(nota)
    dic_notas['Menor'] = min(nota)
    dic_notas['Média'] = sum(nota) / len(nota)

    # Verifica se a opção sit está ativada
    if sit:
        if dic_notas['Média'] >= 6:
            dic_notas['Situação'] = 'Situação ok'
        else:
            dic_notas['Situação'] = 'Situação ruim'

    # Retorna o dicionário com as informações sobre as notas
    return dic_notas


# Chama a função com três notas e situação calculada
resultado = notas(3, 4, 8, sit=True)

# Imprime o resultado
print(resultado)
