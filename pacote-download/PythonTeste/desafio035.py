from math import fabs
r1 = int(input('Digite o comprimento da 1ª reta: '))
r2 = int(input('Digite o comprimento da 2ª reta: '))
r3 = int(input('Digite o comprimento da 3ª reta: '))
if (r1+r2)>r3 and fabs(r1-r2)<r3 and (r1+r3)>r2 and fabs(r1-r3)<r2:
    if r1==r2 and r2==r3:
        print('O triângulo é EQUILÁTERO!')
    elif r1==r2 or r2==r3:
        print('O triângulo é ISÓCELES!')
    else:
        print('O triângulo é ESCALENO!')
else:
    print('O triângulo NÃO EXISTE!')


