p=float(input('Qual o preco do produto?'))
d=float(input('Quanto % vai ser o desconto?'))
print(f'O produto de {p} reais vai ficar {p-(p*(d/p))} com {d:.0f} de desconto')