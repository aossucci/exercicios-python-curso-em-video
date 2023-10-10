'''Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.'''

salario = float(input('Digite o valor do salário: '))

if salario > 1250:
    novoSalario = salario * (1 + .10)
else:
    novoSalario = salario * (1 + .15)

print(f'O valor do salário reajustado é de R${novoSalario:.2f}')