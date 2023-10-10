'''Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu 
Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:

– IMC abaixo de 18,5: Abaixo do Peso

– Entre 18,5 e 25: Peso Ideal

– 25 até 30: Sobrepeso

– 30 até 40: Obesidade

– Acima de 40: Obesidade Mórbida'''

altura = int(input('Digite sua altura em [CM]: '))/100
peso = float(input('Digite sem peso em [KG]: '))
imc = round(peso / (altura**2), 2)

if imc <= 18.5:
    print(f'Seu IMC é {imc}kg/m², voce está abaixo do peso ideal')
elif imc <= 25:
    print(f'Seu IMC é {imc}kg/m², voce está no peso ideal')
elif imc <= 30:
    print(f'Seu IMC é {imc}kg/m², voce está com sobrepeso')
elif imc <= 40:
    print(f'Seu IMC é {imc}kg/m², voce está obeso')
else:
    print(f'Seu IMC é {imc}kg/m², voce está com obesidade mórbida')
