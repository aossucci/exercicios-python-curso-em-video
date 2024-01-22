# Exemplo de escopo global
global_variable = 10


def exemplo_escopo_global():
    # Podemos acessar variáveis globais dentro de uma função
    print("Dentro da função - Escopo global:", global_variable)


exemplo_escopo_global()
print("Fora da função - Escopo global:", global_variable)
# Resultado: Dentro da função - Escopo global: 10
#           Fora da função - Escopo global: 10


# Exemplo de escopo local
def exemplo_escopo_local():
    local_variable = 5
    print("Dentro da função - Escopo local:", local_variable)


exemplo_escopo_local()
# Tentar acessar uma variável local fora da função resultará em um erro
# print("Fora da função - Escopo local:", local_variable)
# Resultado: Dentro da função - Escopo local: 5
#           NameError: name 'local_variable' is not defined


# Exemplo de função com retorno
def soma(a, b):
    result = a + b
    return result


# Chamando a função e atribuindo o resultado a uma variável
resultado_soma = soma(3, 4)
print("Resultado da soma:", resultado_soma)
# Resultado: Resultado da soma: 7
