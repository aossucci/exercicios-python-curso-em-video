# Criando um dicionário vazio
meu_dicionario = {}

# Adicionando chave-valor ao dicionário
meu_dicionario['nome'] = 'João'
meu_dicionario['idade'] = 25
meu_dicionario['cidade'] = 'São Paulo'

# Acessando valores através das chaves
nome = meu_dicionario['nome']
idade = meu_dicionario['idade']
cidade = meu_dicionario['cidade']

# Verificando se uma chave existe no dicionário
if 'email' in meu_dicionario:
    email = meu_dicionario['email']
else:
    email = None

# Obtendo um valor com um valor padrão caso a chave não exista
telefone = meu_dicionario.get('telefone', 'Não informado')

# Atualizando valores de uma chave
meu_dicionario['idade'] = 26

# Removendo um par chave-valor do dicionário
del meu_dicionario['cidade']

# Iterando sobre as chaves do dicionário
for chave in meu_dicionario:
    valor = meu_dicionario[chave]
    print(f'{chave}: {valor}')

# Iterando sobre chaves e valores simultaneamente
for chave, valor in meu_dicionario.items():
    print(f'{chave}: {valor}')

# Obtendo todas as chaves e valores como listas
todas_as_chaves = list(meu_dicionario.keys())
todos_os_valores = list(meu_dicionario.values())

# Verificando o tamanho do dicionário (número de pares chave-valor)
tamanho_do_dicionario = len(meu_dicionario)

# Limpando todos os pares chave-valor do dicionário
meu_dicionario.clear()
