'''Elabore um programa que calcule o valor a ser pago por um produto, considerando o
seu preço normal e condição de pagamento:

– à vista dinheiro/cheque: 10% de desconto

– à vista no cartão: 5% de desconto

– em até 2x no cartão: preço normal 

– 3x ou mais no cartão: 20% de juros'''

print(f"{' Lojas Americanas ':=^40}") #formatação para centralizar o título e adicionar = no espaço vazio
print()
preco_normal = float(input('Valor das compras: R$'))
pagamento = int(input('''Formas de pagamento:
[1] à vista dinheiro ou cheque
[2] à vista no cartão
[3] 2x no cartão
[4] 3x ou mais no cartão] 
Digite o número da forma de pagamento escolhida: '''))

if pagamento == 1:
    valor = preco_normal * 0.9 #10% de desconto
    print(f'A vista no dinheiro ou cheque, o valor a ser pago é de R${valor}')
elif pagamento == 2:
    valor = preco_normal * 0.95 # 5% de desconto
    print(f'A vista no cartão, o valor a ser pago é de R${valor}')
elif pagamento == 3:
    valor = preco_normal
    valor_parcelas = valor / 2
    print(f'Em 2x no cartão, o valor a ser pago é de R${valor}, em 2x de R${valor_parcelas}')
elif pagamento == 4:
    valor = preco_normal * 1.2 # 20% de acrescimo
    parcelas = int(input('Digite o número de parcelas: '))
    valor_parcelas = valor / parcelas
    print(f'Em 3x ou mais no cartão, o valor a ser pago é de R${valor}, em {parcelas} de R${valor_parcelas:.2f}')
else:
    print('Opção não encontrada, tente novamente')