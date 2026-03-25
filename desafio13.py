salario=float(input('Qual o seu salario?'))
aumento=float(input('Quanto % vai ser o aumento?'))
novo_salario= salario + (salario*aumento/100)
print(f'Seu salario è {salario} e voce esta recebendo um aumento de {aumento}%, agora seu novo salario vai ser de {novo_salario:.2f} reais')