#Conversor de Medidas
medida = float(input('Digite uma distância em metros: '))
print('A medida de {}m corresponde a {}km, {}hm, {}dam, {}dm, {}cm e {}mm!' .format(medida, (medida / 1000), (medida / 100), (medida / 10), (medida * 10), (medida * 100), (medida * 1000)))