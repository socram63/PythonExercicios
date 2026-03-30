dias=float(input('O carros foi alugado por quantos Dias?'))
km=float(input('Quantos KMs foi rodado com o carro?'))
valor=dias*60+km*0.15
print(f'Foram {dias:.0f} dias e {km} Kms rodados o total ficou R${valor:.2f}')