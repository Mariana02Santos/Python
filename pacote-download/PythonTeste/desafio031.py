d = int(input('Distância da viagem em Km: '))
if d <= 200:
    print('Valor da passagem:', 0.5 * d)
else:
    print('Valor da passagem: R$', 0.45 * d)
