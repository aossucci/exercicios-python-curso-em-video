lanche = ['Sorvete', 'Refrigerante', 'Pudim']

# adicionar elemento
lanche.append('Suco')
print(lanche)

# inserir em index especifico
lanche.insert(0, 'Pizza')
lanche.insert(1, 'Hamburguer')
print(lanche)

# apagar elementos
del lanche[2]
lanche.pop(0)  # vazio remove o último elemento
lanche.remove('Hamburguer')  # remove pelo conteúdo
print(lanche)

# função list
valores = list(range(0, 10))
print(valores)

# ordenar valores
lanche.sort()
lanche.sort(reverse=True)
print(lanche)
