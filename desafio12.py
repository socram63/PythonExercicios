valor=float(input('Qual o preco do produto?'))
desconto=float(input('Quanto % vai ser o desconto?'))
calculo=valor-(valor*desconto/100)
print(f'O produto de {valor} reais com {desconto:.0f}% de desconto vai ficar {calculo:.2f}')