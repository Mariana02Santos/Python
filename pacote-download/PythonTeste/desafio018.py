import math
a = int(input('Digite o valor do ângulo em graus: '))
s = math.sin(math.radians(a))
c = math.cos(math.radians(a))
t = s/c
print('Seno em radianos: {: .2f} \nCosseno em radianos: {: .2f} \nTangente em radianos:{: .2f}'.format(s,c,t))
