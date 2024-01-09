'''Exemplo do uso de listas dentro de listas'''

galera = list()
dado = list()
for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])  # [:] cria cópia
    dado.clear()
