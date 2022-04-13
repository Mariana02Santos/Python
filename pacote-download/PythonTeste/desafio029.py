v = float(input('Velocidade do carro (Km/h): '))
m = (int(v) - 80) * 7
if v > 80:
    print('Você foi multado no valor de R$', m, ',00')
else:
    print('OK')
