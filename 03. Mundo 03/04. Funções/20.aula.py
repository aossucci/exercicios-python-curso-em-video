# Definição de uma função simples sem parâmetros
def saudacao():
    """Esta função imprime uma saudação."""
    print("Olá! Bem-vindo!")


# Chamada da função
saudacao()

# ---------------------------------------------

# Função com parâmetros


def somar(a, b):
    """Esta função recebe dois números e retorna a soma."""
    resultado = a + b
    return resultado


# Chamada da função com argumentos
resultado_soma = somar(5, 3)
print("A soma é:", resultado_soma)

# ---------------------------------------------

# Parâmetros com valores padrão


def saudacao_personalizada(nome, saudacao="Olá"):
    """Esta função imprime uma saudação personalizada."""
    print(f"{saudacao}, {nome}!")


# Chamada da função com apenas um argumento
saudacao_personalizada("Maria")

# Chamada da função com dois argumentos
saudacao_personalizada("João", "Oi")

# ---------------------------------------------

# Função com retorno múltiplo


def operacoes_matematicas(x, y):
    """Esta função retorna a soma e o produto de dois números."""
    soma = x + y
    produto = x * y
    return soma, produto


# Chamada da função e desempacotamento dos resultados
resultado_soma, resultado_produto = operacoes_matematicas(4, 6)
print("Soma:", resultado_soma)
print("Produto:", resultado_produto)

# ---------------------------------------------

# Funções com argumentos arbitrários


def lista_argumentos(*args):
    """Esta função recebe um número variável de argumentos e os imprime."""
    for arg in args:
        print(arg)


# Chamada da função com diferentes números de argumentos
lista_argumentos(1, 2, 3)
lista_argumentos("a", "b", "c", "d")

# ---------------------------------------------

# Função com argumentos de palavra-chave arbitrários


def info_pessoa(**kwargs):
    """Esta função recebe argumentos de palavra-chave e os imprime."""
    for chave, valor in kwargs.items():
        print(f"{chave}: {valor}")


# Chamada da função com argumentos de palavra-chave
info_pessoa(nome="Alice", idade=25, cidade="São Paulo")

# ---------------------------------------------

# Função lambda (função anônima)


def quadrado(x): return x ** 2


print("Quadrado de 4:", quadrado(4))
