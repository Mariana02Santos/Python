s = float(input('Salário do funcionário: '))
if s > 1250:
    print('Aumento: R${: .2f}'.format(0.1 * s))
else:
    print('Aumento: R${: .2f}'.format(0.15 * s))
