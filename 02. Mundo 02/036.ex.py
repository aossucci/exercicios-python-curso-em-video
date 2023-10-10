'''Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. 
Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. 
A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado'''

valor_casa = float(input('Digite o valor da casa: R$ '))
salario = float(input('Digite o valor do seu salário: R$ '))
anos_emprestimo = int(input('Digite em quantos pretende pagar o empréstimo: '))
meses = anos_emprestimo * 12

valor_emprestimo = valor_casa * (1 + 0.2 * anos_emprestimo)
parcela_mensal = valor_emprestimo / meses

print(f'{valor_emprestimo:.2f}')

print(f'Para pagar uma casa de {valor_casa:,.2f} reais em {anos_emprestimo} anos, totalizando um valor corrigido de {valor_emprestimo:,.2f} reais, a prestação'
      f' será de {parcela_mensal:,.2f} reais')

if parcela_mensal > (salario * .3):
    print('Empréstimo negado! Pois o valor da parcela é maior que 30% do seu salário')
else:
    print('Empréstimo concedido, pois o valor da parcela não ultrapassa 30% do salário')