money = float(input('Quanto dinheiro você tem na carteira? R$'))

print('Com R${} você pode comprar US${:.2f}!' .format(money, (money / 3.27)))