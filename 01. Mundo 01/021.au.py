frase = 'Curso em vídeo Python'

# Mostrar de terminadas letras ou trechos dentro de uma string [inicio:fim:intervalo]
print(frase[2:15:2])  

# len-> mostrar o tamanho da string
print(len(frase))  

# .count -> contar quantas vezes aparece determinada letra
print(frase.count('o', 0, 13)) # (a se buscar, inicio, fim)

# .find -> procurar se existe determinado trecho ou letra na string, volta com a posição de inicio
print(frase.find('deo'))
print(frase.rfind('A')) #pra pesquisar a última posição em que aparece

# in -> retorna true or false para determinada existencia na string
print('Curso' in frase)

# .recplace -> substituição na string
print(frase.replace('Curso', 'Aula'))

# .upper -> colocar em maiusculas
print(frase.upper())

# .lower -> colocar em minusculas
print(frase.lower())

# .capitalize -> somente a primeira letra da string em maiuscula
print(frase.capitalize())

# .title -> colocar em maiuscula as primeiras letras de cada palavra
print(frase.title())

# .strip -> remover espaços excedentes, com variações .rstrip (direita) e .lstrip (esquerda)
print(frase.strip())

# .split -> dividir a frase em palavras e colocar em uma lista
frase2 = frase.split()
print(frase2)

# .join -> unir em uma unica string uma lista de palavras
print('-'.join(frase2))

# .replace -> substitui algo na str
print(frase.replace(' ', ''))