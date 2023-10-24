# formas de mostrar itens nas tuplas

lanches = ('Hamburguer',  'Batata', 'Pizza', 'Suco')

for comida in lanches:
    print(comida)

for cont in range(0, len(lanches)):
    print(f'O {lanches[cont]} está na posição {cont}')

for pos, comida in enumerate(lanches):
    print(f'{comida} está na posição {pos}')
