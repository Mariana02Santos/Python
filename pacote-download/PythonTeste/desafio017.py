from math import hypot
co = float(input('Digite o comprimento de um dos catetos do triângulo retângulo: '))
ca = float(input('Digite o comprimento do outro cateto do triângulo retângulo: '))
h = hypot(co,ca)
print('O comprimento da hipotenusa desse triângulo retângulo é {: .2f}'.format(h))

