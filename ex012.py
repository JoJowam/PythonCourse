price = float(input('Qual é o preço do produto? R$'))

print('O produto que custava R${}, na promoção com desconto de 5% vai custar R${:.2f}!' .format(price, (price - (price * 0.05))))