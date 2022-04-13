print(' ')
print(' CÁLCULO IMC')
print('-------=-------')
p = float(input('Peso (Kg): '))
a = float(input('Altura (m): '))
i = p/a**2
if i<18.5:
    print('Abaixo do peso ({:.2f})'.format(i))
elif i >= 18.5 and i <25:
    print('Peso ideal ({:.2f})'.format(i))
elif i>=25 and i<=30:
    print('Sobrepeso ({:.2f})'.format(i))
elif i>30 and i<=40:
    print('Obesidade ({:.2f})'.format(i))
else:
    print('Obesidade mórbida ({:.2f})'.format(i))

