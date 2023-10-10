'''Faça um algoritimo que leia o salário de um funcionário e mostre seu novo salário com 15% de aumento'''

salario = float(input('Salário: R$'))
reajuste = 15 / 100
novoSalario = salario * (1 + reajuste)

print('Salário atual: R${:.2f},\nSalário com reajuste: R${:.2f}'.format(salario, novoSalario))

print(f'Salário atual: R${salario:.2f}\nSalário com reajuste: R${novoSalario:.2f}')